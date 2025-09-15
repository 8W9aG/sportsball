"""NBA NBA API game model."""

# pylint: disable=too-many-arguments,line-too-long,duplicate-code
import datetime

import pandas as pd
import pytest_is_running
import pytz
import requests_cache
from dateutil.parser import parse

from ....cache import MEMORY
from ...game_model import VERSION, GameModel
from ...league import League
from ...season_type import SeasonType
from .nba_nba_team_model import create_nba_nba_team_model

_SEASON_TYPE_MAP = {
    "1": SeasonType.PRESEASON,
    "2": SeasonType.REGULAR,
    "3": SeasonType.OFFSEASON,
    "4": SeasonType.POSTSEASON,
    "5": SeasonType.POSTSEASON,
    "6": SeasonType.OFFSEASON,
}


def _create_nba_nba_game_model(
    row: pd.Series,
    league: League,
    week: int,
    game_number: int,
    session: requests_cache.CachedSession,
    league_id: str,
    version: str,
) -> GameModel:
    season_id = row["SEASON_ID"]
    dt = pytz.timezone("EST").localize(parse(row["GAME_DATE"]))
    return GameModel(
        dt=dt,
        week=week,
        game_number=game_number,
        venue=None,
        teams=[
            x
            for x in [
                create_nba_nba_team_model(row, True, session, dt, league, league_id),  # type: ignore
                create_nba_nba_team_model(row, False, session, dt, league, league_id),  # type: ignore
            ]
            if x is not None
        ],
        end_dt=None,
        attendance=None,
        league=str(league),
        year=int(season_id[1:]),
        season_type=_SEASON_TYPE_MAP[season_id[0]],
        postponed=None,
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        umpires=[],
        version=version,
        best_of=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_nba_nba_game_model(
    row: pd.Series,
    league: League,
    week: int,
    game_number: int,
    session: requests_cache.CachedSession,
    league_id: str,
    version: str,
) -> GameModel:
    """Create a game model from NBA API."""
    return _create_nba_nba_game_model(
        row,
        league,
        week,
        game_number,
        session,
        league_id,
        version=version,
    )


def create_nba_nba_game_model(
    row: pd.Series,
    league: League,
    week: int,
    game_number: int,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league_id: str,
) -> GameModel:
    """Create a game model from NBA API."""
    if (
        not pytest_is_running.is_running()
        and dt < datetime.datetime.now() - datetime.timedelta(days=7)
    ):
        return _cached_create_nba_nba_game_model(
            row,
            league,
            week,
            game_number,
            session,
            league_id,
            version=VERSION,
        )
    with session.cache_disabled():
        return _create_nba_nba_game_model(
            row,
            league,
            week,
            game_number,
            session,
            league_id,
            version=VERSION,
        )
