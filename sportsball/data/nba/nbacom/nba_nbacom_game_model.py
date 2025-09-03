"""NBA NBA.com game model."""

# pylint: disable=too-many-statements,protected-access,too-many-arguments,bare-except,duplicate-code
import datetime
from typing import Any

import extruct  # type: ignore
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...game_model import GameModel
from ...league import League
from ...team_model import VERSION as TEAM_VERSION
from ...venue_model import VERSION
from .nba_nbacom_team_model import create_nba_nbacom_team_model
from .nba_nbacom_venue_model import create_nba_nbacom_venue_model


def create_nba_nbacom_game_model(
    game: dict[str, Any],
    session: ScrapeSession,
    version: str,
) -> GameModel:
    """Create a game model from AFL Tables."""
    game_id = game["gameId"]
    venue_name: str | None = None
    dt = None
    with session.cache_disabled():
        response = session.get(f"https://www.nba.com/game/{game_id}")
        response.raise_for_status()
        data = extruct.extract(response.text, base_url=response.url)
        for jsonld in data["json-ld"]:
            location = jsonld.get("location")
            if location is not None:
                venue_name = location["name"]
            start_date = jsonld.get("startDate")
            if start_date is not None:
                dt = datetime.datetime.fromisoformat(start_date)

    if venue_name is None:
        raise ValueError("venue_name is null")
    if dt is None:
        raise ValueError("dt is null")
    venue_model = create_nba_nbacom_venue_model(
        venue_name=venue_name, session=session, dt=dt, version=VERSION
    )
    return GameModel(
        dt=dt,
        week=None,
        game_number=None,
        venue=venue_model,
        teams=[
            create_nba_nbacom_team_model(
                team=game["homeTeam"], session=session, dt=dt, version=TEAM_VERSION
            ),
            create_nba_nbacom_team_model(
                team=game["awayTeam"], session=session, dt=dt, version=TEAM_VERSION
            ),
        ],
        end_dt=None,
        attendance=None,
        league=League.NBA,
        year=datetime.datetime.today().year,
        season_type=None,
        postponed=None,
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        version=version,
        umpires=[],
    )
