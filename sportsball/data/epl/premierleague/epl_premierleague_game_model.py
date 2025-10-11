"""EPL PremierLeague game model."""

from typing import Any

from dateutil.parser import parse
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...game_model import GameModel
from ...league import League
from ...team_model import VERSION as TEAM_VERSION
from ...venue_model import VERSION
from .epl_premierleague_team_model import create_epl_premierleague_team_model
from .epl_premierleague_venue_model import create_epl_premierleague_venue_model


def create_epl_premierleague_game_model(
    game: dict[str, Any],
    session: ScrapeSession,
    version: str,
) -> GameModel:
    """Create a game model from the EPL premierleague site."""
    dt = parse(game["kickoff"] + game["kickoffTimezone"])
    return GameModel(
        dt=dt,
        week=game["matchWeek"],
        game_number=None,
        venue=create_epl_premierleague_venue_model(
            venue_name=game["ground"], session=session, dt=dt, version=VERSION
        ),
        teams=[
            create_epl_premierleague_team_model(
                team=game["homeTeam"], session=session, dt=dt, version=TEAM_VERSION
            ),
            create_epl_premierleague_team_model(
                team=game["awayTeam"], session=session, dt=dt, version=TEAM_VERSION
            ),
        ],
        end_dt=None,
        attendance=game.get("attendance"),
        league=League.EPL,
        year=dt.year,
        season_type=None,
        postponed=None,
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        version=version,
        umpires=[],
        best_of=None,
    )
