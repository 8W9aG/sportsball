"""AFL AFL game model."""

# pylint: disable=too-many-statements,protected-access,too-many-arguments,bare-except,duplicate-code,too-many-locals
import datetime
import re

import pytest_is_running
from bs4 import BeautifulSoup, Tag
from playwright.sync_api import Playwright
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....playwright import ensure_install
from ...game_model import GameModel
from ...league import League
from ...team_model import VERSION
from ...venue_model import VERSION as VENUE_VERSION
from ..position import Position, position_from_str
from .afl_afl_team_model import create_afl_afl_team_model
from .afl_afl_umpire_model import create_afl_afl_umpire_model
from .afl_afl_venue_model import create_afl_afl_venue_model


def parse_players_v1(div: Tag) -> list[list[tuple[str, str, str, str, Position]]]:
    """Parses the players from a v1 format."""
    teams_players: list[list[tuple[str, str, str, str, Position]]] = [[], []]
    for div_positions_row in div.find_all(
        "div", {"class": re.compile(".*team-lineups__positions-row.*")}
    ):
        row_players: list[list[tuple[str, str, str, str, Position]]] = [[], []]
        for count, div_team_players in enumerate(
            div_positions_row.find_all(
                "div",
                {"class": re.compile(".*team-lineups__positions-players-container.*")},
            )
        ):
            team_players: list[tuple[str, str, str, str, Position]] = []
            position = None
            for span in div_team_players.find_all(
                "span", {"class": re.compile(".*team-lineups__position-meta-label.*")}
            ):
                position = position_from_str(span.get_text().strip())
            if position is None:
                raise ValueError("position is null")
            for a in div_team_players.find_all(
                "a", {"class": re.compile(".*js-player-profile-link.*")}
            ):
                player_id = "afl:" + a.get("data-player-id")
                first_name = a.get("data-first-name")
                second_name = a.get("data-surname")
                player_number = None
                for span_player_number in a.find_all(
                    "span",
                    {"class": re.compile(".*team-lineups__player-number.*")},
                ):
                    player_number = (
                        span_player_number.get_text()
                        .strip()
                        .replace("[", "")
                        .replace("]", "")
                    )
                if player_number is None:
                    raise ValueError("player_number is null")
                team_players.append(
                    (player_id, player_number, first_name, second_name, position)
                )
            row_players[count].extend(team_players)
        for count, row_players_list in enumerate(row_players):
            teams_players[count].extend(row_players_list)
    return teams_players


def _extract_odds(soup: BeautifulSoup) -> list[float]:
    odds = []
    for span in soup.find_all("span", {"class": "betting-button__money"}):
        odds.append(float(span.get_text().strip().replace("$", "")))
    return odds


def _extract_dt(soup: BeautifulSoup, url: str) -> datetime.datetime:
    for div in soup.find_all("div", {"class": re.compile(".*js-match-start-time.*")}):
        start_time = div.get("data-start-time")
        return datetime.datetime.fromisoformat(start_time)
    raise ValueError(f"Unable to find datetime for {url}")


def _extract_players(
    soup: BeautifulSoup, players: list[list[tuple[str, str, str, str, Position]]]
) -> list[list[tuple[str, str, str, str, Position]]]:
    def is_players_empty() -> bool:
        nonlocal players
        if not players:
            return True
        for team in players:
            if not team:
                return True
        return False

    if not is_players_empty():
        return players

    for div in soup.find_all("div", {"class": re.compile(".*js-match-list-item.*")}):
        players = parse_players_v1(div)
        if not is_players_empty():
            return players

    return players


def _parse(
    html: str, players: list[list[tuple[str, str, str, str, Position]]], url: str
) -> tuple[
    list[float], datetime.datetime, list[list[tuple[str, str, str, str, Position]]]
]:
    soup = BeautifulSoup(html, "lxml")
    return _extract_odds(soup), _extract_dt(soup, url), _extract_players(soup, players)


def create_afl_afl_game_model(
    team_names: list[str],
    players: list[list[tuple[str, str, str, str, Position]]],
    dt: datetime.datetime | None,
    venue_name: str,
    session: ScrapeSession,
    ladder: list[str],
    url: str | None,
    playwright: Playwright,
    version: str,
    umpires: list[str],
) -> GameModel:
    """Create a game model from AFL Tables."""
    odds: list[float] = []
    if url is not None and not pytest_is_running.is_running():
        ensure_install()
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto(url + "#line-ups", wait_until="networkidle")
        except:  # noqa: E722
            pass
        odds, dt, players = _parse(page.content(), players, url)
    if dt is None:
        raise ValueError("dt is null")

    venue_model = create_afl_afl_venue_model(
        venue_name=venue_name, session=session, dt=dt, version=VENUE_VERSION
    )
    teams = [
        create_afl_afl_team_model(
            team_name=x,
            players=players[count],
            session=session,
            dt=dt,
            ladder=ladder,
            odds=odds[count] if count < len(odds) else None,
            version=VERSION,
        )
        for count, x in enumerate(team_names)
    ]
    return GameModel(
        dt=dt,
        week=None,
        game_number=None,
        venue=venue_model,
        teams=teams,
        end_dt=None,
        attendance=None,
        league=League.AFL,
        year=datetime.datetime.today().year,
        season_type=None,
        postponed=None,
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        version=version,
        umpires=[create_afl_afl_umpire_model(name=x) for x in umpires],
    )
