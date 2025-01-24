"""NFL SportsDB team model."""

# pylint: disable=too-many-arguments
import datetime

import pytest_is_running
import requests_cache

from ....cache import MEMORY
from ...google.google_news_model import create_google_news_models
from ...league import League
from ...team_model import TeamModel
from ...x.x_social_model import create_x_social_model


def _create_nfl_sportsdb_team_model(
    team_id: str,
    name: str,
    points: float,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
) -> TeamModel:
    return TeamModel(
        identifier=team_id,
        name=name,
        points=points,
        players=[],
        odds=[],
        ladder_rank=None,
        location=None,
        news=create_google_news_models(name, session, dt, league),
        social=create_x_social_model(team_id, session, dt),
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_nfl_sportsdb_team_model(
    team_id: str,
    name: str,
    points: float,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
) -> TeamModel:
    return _create_nfl_sportsdb_team_model(team_id, name, points, session, dt, league)


def create_nfl_sportsdb_team_model(
    team_id: str,
    name: str,
    points: float,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
) -> TeamModel:
    """Create a team model based off the sportsdb NFL response."""
    if (
        not pytest_is_running.is_running()
        and dt < datetime.datetime.now() - datetime.timedelta(days=7)
    ):
        return _cached_create_nfl_sportsdb_team_model(
            team_id, name, points, session, dt, league
        )
    with session.cache_disabled():
        return _create_nfl_sportsdb_team_model(
            team_id, name, points, session, dt, league
        )
