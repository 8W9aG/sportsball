"""ESPN league model."""

# pylint: disable=too-many-locals,too-many-arguments,line-too-long,too-many-branches,too-many-statements
import datetime
import logging
from typing import Any, Iterator
from urllib.parse import urlparse

import requests
import tqdm
from dateutil.parser import parse
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ..game_model import GameModel
from ..league import League
from ..league_model import SHUTDOWN_FLAG, LeagueModel, needs_shutdown
from ..season_type import SeasonType
from .espn_game_model import create_espn_game_model


def _season_type_from_name(name: str) -> SeasonType:
    if (
        name == "Regular Season"
        or "English Premier League" in name
        or "Group Stage" in name
        or "Spring Regular Season" in name
        or "Round of" in name
        or "Second Round" in name
        or "2015-2016 Barclays Premier League" in name
        or "2014-2015 Barclays Premier League" in name
        or "2013-2014 Barclays Premier League" in name
    ):
        return SeasonType.REGULAR
    if name == "Preseason" or "Spring Training" in name:
        return SeasonType.PRESEASON
    if (
        name == "Postseason"
        or "Quarterfinals" in name
        or "Semifinals" in name
        or "3rd-Place" in name
        or "Final" in name
        or "Third Place" in name
        or "Quarter-finals" in name
        or "Semi-finals" in name
        or "Play-In Season" in name
        or "Spring Postseason" in name
    ):
        return SeasonType.POSTSEASON
    if name == "Off Season":
        return SeasonType.OFFSEASON
    raise ValueError(f"Unrecognised season name: {name}")


class ESPNLeagueModel(LeagueModel):
    """ESPN implementation of the league model."""

    def __init__(
        self,
        start_url: str,
        league: League,
        session: ScrapeSession,
        position: int | None = None,
    ) -> None:
        super().__init__(league, session, position=position)
        self._start_url = start_url

    @classmethod
    def name(cls) -> str:
        return "espn-league-model"

    @classmethod
    def position_validator(cls) -> dict[str, str]:
        """A dictionary that contains the mapping from positions to standard positions."""
        raise NotImplementedError(
            "position_validator is not implemented by parent class"
        )

    def _produce_game(
        self,
        cache_disabled: bool,
        event_item: dict[str, Any],
        week_count: int | None,
        game_number: int,
        season_type_json: dict[str, Any],
        pbar: tqdm.tqdm,
    ) -> Iterator[GameModel]:
        if cache_disabled:
            with self.session.cache_disabled():
                event_response = self.session.get(event_item["$ref"])
        else:
            event_response = self.session.get(event_item["$ref"])
        event_response.raise_for_status()
        event = event_response.json()
        for competition in event["competitions"]:
            game_model = create_espn_game_model(
                competition,
                week_count,
                game_number,
                self.session,
                self.league,
                season_type_json.get("year"),
                _season_type_from_name(season_type_json["name"]),
                self.position_validator(),
            )
            game_number += 1
            pbar.update(1)
            pbar.set_description(
                f"ESPN {game_model.year} - {game_model.season_type} - {game_model.dt}"
            )
            yield game_model

    def _produce_games(
        self,
        week: dict[str, Any],
        week_count: int,
        season_type_json: dict[str, Any],
        pbar: tqdm.tqdm,
        cache_disabled: bool,
    ) -> Iterator[GameModel]:
        events_page = 1
        events_count = 0
        while True:
            if "events" not in week:
                break
            events_response = self.session.get(
                week["events"]["$ref"] + f"&page={events_page}"
            )
            events_response.raise_for_status()
            events = events_response.json()
            for event_item in events["items"]:
                for game_model in self._produce_game(
                    event_item=event_item,
                    game_number=events_count,
                    week_count=week_count,
                    cache_disabled=cache_disabled,
                    season_type_json=season_type_json,
                    pbar=pbar,
                ):
                    events_count += 1
                    yield game_model
            if events_page >= events["pageCount"]:
                break
            events_page += 1
        qbr_page = 1
        qbr_count = 0
        while True:
            if "qbr" not in week:
                break
            qbr_response = self.session.get(week["qbr"]["$ref"] + f"&page={qbr_page}")
            qbr = qbr_response.json()
            for qbr_item in qbr["items"]:
                for game_model in self._produce_game(
                    event_item=qbr_item["event"],
                    game_number=qbr_count,
                    week_count=week_count,
                    cache_disabled=cache_disabled,
                    season_type_json=season_type_json,
                    pbar=pbar,
                ):
                    yield game_model
                    qbr_count += 1
            if qbr_page >= qbr["pageCount"]:
                break
            qbr_page += 1

    def _produce_week_games(
        self,
        season_type_json: dict[str, Any],
        page: int,
        pbar: tqdm.tqdm,
        cache_disabled: bool,
    ) -> Iterator[GameModel]:
        found_pages = False
        if "weeks" in season_type_json:
            game_page = 1
            week_count = 0
            while True:
                if cache_disabled:
                    with self.session.cache_disabled():
                        weeks_response = self.session.get(
                            season_type_json["weeks"]["$ref"] + f"&page={page}"
                        )
                else:
                    weeks_response = self.session.get(
                        season_type_json["weeks"]["$ref"] + f"&page={page}"
                    )
                weeks_response.raise_for_status()
                weeks = weeks_response.json()
                for item in weeks["items"]:
                    if needs_shutdown():
                        return
                    if cache_disabled:
                        with self.session.cache_disabled():
                            week_response = self.session.get(item["$ref"])
                    else:
                        week_response = self.session.get(item["$ref"])
                    week_response.raise_for_status()
                    week = week_response.json()
                    for game_model in self._produce_games(
                        week, week_count, season_type_json, pbar, cache_disabled
                    ):
                        yield game_model
                        found_pages = True
                    week_count += 1
                if game_page >= weeks["pageCount"]:
                    break
                game_page += 1
        if not found_pages and self.league != League.NFL:
            # Lets check the scoreboards via the calendar
            o = urlparse(season_type_json["$ref"])
            path_components = o.path.split("/")
            sport_slug = path_components[3]
            league_slug = path_components[5]
            start_date = parse(season_type_json["startDate"]).date()
            end_date = parse(season_type_json["endDate"]).date()
            calendar_dates = {
                (start_date + datetime.timedelta(days=x))
                for x in range((end_date - start_date).days)
            }
            events_count = 0
            while calendar_dates:
                calendar_date = calendar_dates.pop()
                if calendar_date > datetime.datetime.now().date() - datetime.timedelta(
                    days=2
                ):
                    continue
                dt = calendar_date.strftime("%Y%m%d")
                url = f"https://site.api.espn.com/apis/site/v2/sports/{sport_slug}/{league_slug}/scoreboard?lang=en&region=us&calendartype=whitelist&limit=100&dates={dt}&league={league_slug}"
                scoreboard_response = self.session.get(url)
                scoreboard_response.raise_for_status()
                try:
                    scoreboard = scoreboard_response.json()
                    calendar_list = scoreboard["leagues"][0]["calendar"]
                    if calendar_list:
                        if isinstance(calendar_list[0], str):
                            declared_calendar_dates = {
                                parse(x).date() for x in calendar_list
                            }
                            calendar_dates &= declared_calendar_dates
                    for event in scoreboard["events"]:
                        event_id = event["id"]
                        event_response = self.session.get(
                            f"https://sports.core.api.espn.com/v2/sports/{sport_slug}/leagues/{league_slug}/events/{event_id}?lang=en&region=us"
                        )
                        event_response.raise_for_status()
                        for game_model in self._produce_game(
                            event_item=event_response.json(),
                            game_number=events_count,
                            season_type_json=season_type_json,
                            pbar=pbar,
                            cache_disabled=False,
                            week_count=None,
                        ):
                            yield game_model
                            events_count += 1
                except (requests.exceptions.JSONDecodeError, KeyError) as exc:
                    logging.error(scoreboard_response.text)
                    logging.error(url)
                    logging.error(str(exc))

    @property
    def games(self) -> Iterator[GameModel]:
        try:
            with self.session.wayback_disabled():
                page = 1
                first = True
                with tqdm.tqdm(position=self.position) as pbar:
                    while True:
                        if page == 1:
                            with self.session.cache_disabled():
                                response = self.session.get(
                                    self._start_url + f"&page={page}"
                                )
                        else:
                            response = self.session.get(
                                self._start_url + f"&page={page}"
                            )
                        response.raise_for_status()
                        seasons = response.json()
                        for item in seasons.get("items", []):
                            season_response = self.session.get(item["$ref"])
                            season_response.raise_for_status()
                            season_json = season_response.json()

                            for season_item in season_json["types"]["items"]:
                                season_type_response = self.session.get(
                                    season_item["$ref"]
                                )
                                season_type_response.raise_for_status()
                                season_type_json = season_type_response.json()

                                yield from self._produce_week_games(
                                    season_type_json, page, pbar, first
                                )
                            first = False

                        if page >= seasons.get("pageCount", 0):
                            break
                        page += 1
        except Exception as exc:
            SHUTDOWN_FLAG.set()
            raise exc
