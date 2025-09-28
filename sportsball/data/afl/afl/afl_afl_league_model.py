"""AFL AFL league model."""

# pylint: disable=too-many-statements,protected-access,too-many-locals,bare-except,too-many-branches,duplicate-code
import datetime
import logging
import re
import urllib.parse
from typing import Iterator

from bs4 import BeautifulSoup, Tag
from dateutil.parser import parse
from playwright.sync_api import Playwright, sync_playwright
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....playwright import ensure_install
from ...game_model import VERSION, GameModel
from ...league import League
from ...league_model import SHUTDOWN_FLAG, LeagueModel, needs_shutdown
from ..position import Position, position_from_str
from .afl_afl_game_model import create_afl_afl_game_model, parse_players_v1


def _parse_v1(
    soup: BeautifulSoup,
    session: ScrapeSession,
    ladder: list[str],
    html_url: str,
    playwright: Playwright,
) -> Iterator[GameModel]:
    for div in soup.find_all("div", {"class": re.compile(".*js-match-list-item.*")}):
        if needs_shutdown():
            return
        team_names = []
        for span in div.find_all(
            "span", {"class": re.compile(".*team-lineups__team-name.*")}
        ):
            team_names.append(span.get_text().strip())
        teams_players = parse_players_v1(div)
        dt = None
        for time in div.find_all(
            "time", {"class": re.compile(".*match-list-alt__header-time.*")}
        ):
            dt = datetime.datetime.fromtimestamp(float(time.get("data-date")) / 1000.0)
        for span_tz in div.find_all(
            "span", {"class": re.compile(".*match-list-alt__header-timezone.*")}
        ):
            tz_text = span_tz.get_text().strip().replace("(", "").replace(")", "")
            dt = parse(" ".join([str(dt), tz_text]))
        venue_name: str | None = None
        for span in div.find_all(
            "span", {"class": re.compile(".*match-list-alt__header-venue.*")}
        ):
            venue_name = span.get_text().strip().replace(",", "")
        if venue_name is None:
            raise ValueError("venue_name is null")
        if dt is None:
            raise ValueError("dt is null")
        url = None
        for a in div.find_all(
            "a", {"class": re.compile(".*match-list-alt__header-mc-link.*")}
        ):
            url = urllib.parse.urljoin(html_url, a.get("href"))
        yield create_afl_afl_game_model(
            team_names=team_names,
            players=teams_players,
            dt=dt,
            venue_name=venue_name,
            session=session,
            ladder=ladder,
            url=url,
            playwright=playwright,
            version=VERSION,
            umpires=[],
        )


def _parse_v2_soup(
    soup: BeautifulSoup, html_url: str
) -> Iterator[
    tuple[
        list[str], list[list[tuple[str, str, str, str, Position]]], str, str, list[str]
    ]
]:
    for div in soup.find_all("div", {"class": "team-lineups__item"}):
        if needs_shutdown():
            return
        team_names = []
        for span in div.find_all(
            "span", {"class": re.compile(".*team-lineups-header__name.*")}
        ):
            team_names = [x.strip() for x in span.get_text().strip().split(" v ")]
        team_players: list[list[tuple[str, str, str, str, Position]]] = [[], []]

        def process_a_player(
            a: Tag,
            idx: int,
            team_players: list[list[tuple[str, str, str, str, Position]]],
            div: Tag,
        ) -> list[list[tuple[str, str, str, str, Position]]]:
            href = a.get("href")
            if not isinstance(href, str):
                raise ValueError("href is not a str")
            player_id = "afl:" + href.split("/")[2]
            name = a.get("title")
            if not isinstance(name, str):
                raise ValueError("name is not a str")
            first_name, sur_name = name.split()
            jersey = None
            for div_shirt in a.find_all(
                "div", {"class": re.compile(".*team-lineups__player-entry--shirt.*")}
            ):
                jersey = div_shirt.get_text().strip()
            if jersey is None:
                raise ValueError("jersey is null")
            position = None
            for span in div.find_all(
                "span", {"class": re.compile(".*team-lineups__position-meta-label.*")}
            ):
                position = position_from_str(span.get_text().strip())
            if position is None:
                raise ValueError("position is null")
            team_players[idx].append(
                (player_id, first_name, sur_name, jersey, position)
            )
            return team_players

        for a in div.find_all(
            "a", {"class": re.compile(".*team-lineups__player-entry--home-team.*")}
        ):
            team_players = process_a_player(a, 0, team_players, div)
        for a in div.find_all(
            "a", {"class": re.compile(".*team-lineups__player-entry--away-team.*")}
        ):
            team_players = process_a_player(a, 1, team_players, div)

        venue_name: str | None = None
        for div_info in div.find_all("div", {"class": "team-lineups-header__info"}):
            header_info = div_info.get_text().strip()
            venue_name = header_info.split("･")[1].strip()
        if venue_name is None:
            raise ValueError("venue_name is null")

        url = None
        for a in div.find_all("a", {"class": "team-lineups-header"}):
            url = urllib.parse.urljoin(html_url, a.get("href"))
        if url is None:
            raise ValueError("url is null")

        umpires = []
        for div_umpires in div.find_all("div", {"class": "team-lineups__umpires"}):
            for player in div_umpires.find_all(
                "div", {"class": "team-lineups__player"}
            ):
                umpires.append(player.get_text().strip().split(",")[0].strip())

        yield (team_names, team_players, venue_name, url, umpires)


def _parse_v2(
    soup: BeautifulSoup,
    session: ScrapeSession,
    ladder: list[str],
    html_url: str,
    playwright: Playwright,
) -> Iterator[GameModel]:
    for team_names, team_players, venue_name, url, umpires in _parse_v2_soup(
        soup, html_url
    ):
        yield create_afl_afl_game_model(
            team_names=team_names,
            players=team_players,
            dt=None,
            venue_name=venue_name,
            session=session,
            ladder=ladder,
            url=url,
            playwright=playwright,
            version=VERSION,
            umpires=umpires,
        )


def _parse_game_info(
    html: str,
    session: ScrapeSession,
    ladder: list[str],
    html_url: str,
    playwright: Playwright,
) -> Iterator[GameModel]:
    soup = BeautifulSoup(html, "lxml")
    found = False
    for game_model in _parse_v1(soup, session, ladder, html_url, playwright):
        found = True
        yield game_model
    if not found:
        yield from _parse_v2(soup, session, ladder, html_url, playwright)


class AFLAFLLeagueModel(LeagueModel):
    """AFL AFL implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(League.AFL, session, position=position)

    @classmethod
    def name(cls) -> str:
        return "afl-afl-league-model"

    @property
    def _ladder(self) -> list[str]:
        ladder = []
        ensure_install()
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context()
            page = context.new_page()
            try:
                page.goto(
                    "https://www.afl.com.au/ladder",
                    wait_until="networkidle",
                    timeout=60000.0,
                )
            except:  # noqa: E722
                pass
            soup = BeautifulSoup(page.content(), "lxml")
            for span in soup.find_all(
                "span", {"class": re.compile(".*stats-table__club-name.*")}
            ):
                team_name = span.get_text().strip()
                if team_name in ladder:
                    continue
                ladder.append(team_name)
            logging.info("Found ladder: %s", ",".join(ladder))
        return ladder

    @property
    def games(self) -> Iterator[GameModel]:
        try:
            ladder = self._ladder
            ensure_install()
            with sync_playwright() as p:
                browser = p.chromium.launch()
                context = browser.new_context()
                page = context.new_page()
                url = "https://www.afl.com.au/matches/team-lineups"
                page.goto(url, wait_until="load")
                yield from _parse_game_info(
                    page.content(), self.session, ladder, url, p
                )
        except Exception as exc:
            SHUTDOWN_FLAG.set()
            raise exc
