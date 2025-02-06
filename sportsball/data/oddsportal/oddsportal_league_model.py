"""Odds Portal league model."""

# pylint: disable=too-many-locals,too-many-branches,too-many-statements,protected-access,too-many-arguments,line-too-long
import http
import json
import logging
import urllib.parse
from typing import Iterator

import extruct  # type: ignore
import requests
import requests_cache
import tqdm
from bs4 import BeautifulSoup

from ...proxy_session import X_NO_WAYBACK
from ..game_model import GameModel
from ..league import League
from ..league_model import LeagueModel
from .decrypt import fetch_data
from .oddsportal_game_model import create_oddsportal_game_model

# Sports
AMERICAN_FOOTBALL = "american-football"
BASKETBALL = "basketball"

# Countries
USA = "usa"

# Leagues
NCAA = "ncaa"


def _process_results_pages(
    url: str,
    session: requests_cache.CachedSession,
    soup: BeautifulSoup,
    league: League,
    pbar: tqdm.tqdm,
    response: requests.Response,
) -> Iterator[GameModel]:
    # Fetch first page
    sanitised_text = response.text[response.text.find("var pageOutrightsVar = '") :]
    sanitised_text = sanitised_text[: sanitised_text.find("'")]
    page_outrights = json.loads(sanitised_text)
    sports_id = page_outrights["sid"]
    oddsportal_id = page_outrights["id"]

    current_page = 1
    total_pages = None
    while (current_page == 1 and total_pages is None) or (
        current_page <= 0 if total_pages is None else total_pages
    ):
        dat_url = f"https://www.oddsportal.com/ajax-sport-country-tournament-archive_/{sports_id}/{oddsportal_id}/X134529032X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X512X32X0X0X0X0X0X0X131072X0X2048/1/-5/page/{current_page}//"
        parsed_data = fetch_data(dat_url, session, url, soup)
        d = parsed_data["d"]
        for row in d["rows"]:
            game_model = create_oddsportal_game_model(
                session, urllib.parse.urljoin(url, row["url"]), league, False
            )
            pbar.update(1)
            pbar.set_description(f"OddsPortal {game_model.dt}")
            yield game_model
        total_pages = d["pagination"]["pages"]
        current_page += 1


class OddsPortalLeagueModel(LeagueModel):
    """Odds Portal implementation of the league model."""

    @property
    def _path(self) -> str:
        match self.league:
            case League.AFL:
                return "/".join(["aussie-rules", "australia", "afl", ""])
            case League.NBA:
                return "/".join([BASKETBALL, USA, "nba", ""])
            case League.NCAAB:
                return "/".join([BASKETBALL, USA, NCAA, ""])
            case League.NCAAF:
                return "/".join([AMERICAN_FOOTBALL, USA, NCAA, ""])
            case League.NFL:
                return "/".join([AMERICAN_FOOTBALL, USA, "nfl", ""])
            case _:
                raise ValueError(f"Unsupported league: {self.league}")

    def _find_next(self, pbar: tqdm.tqdm) -> Iterator[GameModel]:
        base_url = "https://www.oddsportal.com/" + self._path
        with self.session.cache_disabled():
            response = self.session.get(base_url)
        response.raise_for_status()
        data = extruct.extract(response.text, base_url=base_url)
        for jsonld in data["json-ld"]:
            if jsonld["@type"] != "SportsEvent":
                continue
            try:
                game_model = create_oddsportal_game_model(
                    self.session,
                    urllib.parse.urljoin(base_url, jsonld["url"]),
                    self.league,
                    True,
                )
                pbar.update(1)
                pbar.set_description(
                    f"OddsPortal {game_model.year} - {game_model.season_type} - {game_model.dt}"
                )
                yield game_model
            except requests.exceptions.HTTPError as exc:
                if exc.response.status_code == http.HTTPStatus.NOT_FOUND:
                    logging.warning("Failed to find game at: %s", jsonld["url"])
                    continue
                raise exc

    def _find_previous(self, pbar: tqdm.tqdm) -> Iterator[GameModel]:
        standard_suffix = self._path + "results/"
        seen_urls = set()
        queued_urls = {"https://www.oddsportal.com/" + standard_suffix}
        while queued_urls:
            url = queued_urls.pop()
            if url in seen_urls:
                continue
            logging.debug("processing url: %s", url)
            seen_urls.add(url)

            response = self.session.get(url, headers={X_NO_WAYBACK: "1"})
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "xml")

            # Find next URLs
            for option in soup.find_all("option"):
                next_url = urllib.parse.urljoin(url, option.get("value"))
                if next_url.endswith("/results/") and self._path[:-1] in next_url:
                    queued_urls.add(next_url)

            yield from _process_results_pages(
                url,
                self.session,
                soup,
                self.league,
                pbar,
                response,
            )

    @property
    def games(self) -> Iterator[GameModel]:
        with tqdm.tqdm(position=self.position) as pbar:
            yield from self._find_next(pbar)
            yield from self._find_previous(pbar)
