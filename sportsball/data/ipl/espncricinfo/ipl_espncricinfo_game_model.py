"""ESPNCricInfo game model."""

# pylint: disable=duplicate-code,too-many-locals
import json

import pytest_is_running
from bs4 import BeautifulSoup
from dateutil.parser import parse
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....cache import MEMORY
from ...game_model import VERSION, GameModel
from ...league import League
from .ipl_espncricinfo_team_model import create_espncricinfo_team_model
from .ipl_espncricinfo_venue_model import create_espncricinfo_venue_model

_LEAGUE_NAMES = {
    "IPL": League.IPL,
}


def _create_espncricinfo_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    positions_validator: dict[str, str],
    version: str,
) -> GameModel | None:
    response = session.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    for script in soup.find_all("script", id="__NEXT_DATA__"):
        data = json.loads(script.get_text())
        data_dict = data["props"]["appPageProps"]["data"]
        game = data_dict["match"]
        if league != _LEAGUE_NAMES.get(game["series"]["name"]):
            return None
        dt = parse(game["startTime"])
        end_dt = parse(game["endTime"])
        grounds = game["grounds"]
        content = data_dict["content"]
        teams_players = content["matchPlayers"]["teamPlayers"]
        innings = content["innings"]
        teams = []
        for team in sorted(game["teams"], key=lambda x: x["isHome"], reverse=True):
            teams.append(
                create_espncricinfo_team_model(
                    session=session,
                    dt=dt,
                    league=league,
                    team=team,
                    positions_validator=positions_validator,
                    teams_players=teams_players,
                    innings=innings,
                    url=url,
                )
            )
        return GameModel(
            dt=dt,
            week=None,
            game_number=None,
            venue=create_espncricinfo_venue_model(grounds, session, dt),
            teams=teams,
            league=str(league),
            year=dt.year,
            season_type=None,
            end_dt=end_dt,
            attendance=None,
            postponed=None,
            play_off=None,
            distance=None,
            dividends=[],
            pot=None,
            version=version,
            umpires=[],
            best_of=None,
        )
    return None


@MEMORY.cache(ignore=["session"])
def _cached_create_espncricinfo_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    positions_validator: dict[str, str],
    version: str,
) -> GameModel | None:
    return _create_espncricinfo_game_model(
        session=session,
        url=url,
        league=league,
        positions_validator=positions_validator,
        version=version,
    )


def create_espncricinfo_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    positions_validator: dict[str, str],
) -> GameModel | None:
    """Create a sports reference game model."""
    if not pytest_is_running.is_running():
        return _cached_create_espncricinfo_game_model(
            session=session,
            url=url,
            league=league,
            positions_validator=positions_validator,
            version=VERSION,
        )
    with session.cache_disabled():
        return _create_espncricinfo_game_model(
            session=session,
            url=url,
            league=league,
            positions_validator=positions_validator,
            version=VERSION,
        )
