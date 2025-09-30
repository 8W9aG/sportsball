"""WNBA WNBA.com game model."""

import datetime
from typing import Any

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...game_model import GameModel
from ...league import League
from ...team_model import VERSION
from ...venue_model import VERSION as VENUE_VERSION
from .wnba_wnbacom_team_model import create_wnba_wnbacom_team_model
from .wnba_wnbacom_venue_model import create_wnba_wnbacom_venue_model


def create_wnba_wnbacom_game_model(
    game_dict: dict[str, Any],
    session: ScrapeSession,
    version: str,
) -> GameModel:
    """Create a game model from WNBA.com."""
    dt = datetime.datetime.fromisoformat(game_dict["utcTime"])
    venue_name = " - ".join(
        [game_dict["arenaName"], game_dict["arenaCity"], game_dict["arenaState"]]
    )
    venue_model = create_wnba_wnbacom_venue_model(
        venue_name=venue_name, session=session, dt=dt, version=VENUE_VERSION
    )
    teams = []
    for team_key in ["home", "visitor"]:
        team_dict = game_dict[team_key]
        team_name = " ".join([team_dict["city"], team_dict["name"]])
        teams.append(
            create_wnba_wnbacom_team_model(
                team_name=team_name,
                identifier=str(team_dict["tid"]),
                dt=dt,
                session=session,
                version=VERSION,
            )
        )

    return GameModel(
        dt=dt,
        week=None,
        game_number=None,
        venue=venue_model,
        teams=teams,
        end_dt=None,
        attendance=None,
        league=League.WNBA,
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
