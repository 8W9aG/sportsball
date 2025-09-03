"""Aussportsbetting game model."""

# pylint: disable=too-many-arguments,duplicate-code
import datetime

import pytest_is_running
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..game_model import VERSION as GAME_VERSION
from ..game_model import GameModel
from ..league import League
from ..team_model import VERSION as TEAM_VERSION
from ..venue_model import VERSION
from .aussportsbetting_team_model import create_aussportsbetting_team_model
from .aussportsbetting_venue_model import create_aussportsbetting_venue_model


def _create_aussportsbetting_game_model(
    dt: datetime.datetime,
    home_team: str,
    away_team: str,
    venue: str | None,
    session: ScrapeSession,
    home_points: float,
    away_points: float,
    home_odds: float,
    away_odds: float,
    league: League,
    play_off: bool,
    version: str,
) -> GameModel:
    venue_model = None
    if venue is not None:
        venue_model = create_aussportsbetting_venue_model(
            venue=venue, session=session, dt=dt, version=VERSION
        )
    home_team_model = create_aussportsbetting_team_model(
        name=home_team,
        points=home_points,
        odds=home_odds,
        session=session,
        dt=dt,
        league=league,
        version=TEAM_VERSION,
    )
    away_team_model = create_aussportsbetting_team_model(
        name=away_team,
        points=away_points,
        odds=away_odds,
        session=session,
        dt=dt,
        league=league,
        version=TEAM_VERSION,
    )
    return GameModel(
        dt=dt,
        week=None,
        game_number=None,
        venue=venue_model,
        teams=[home_team_model, away_team_model],  # pyright: ignore
        end_dt=None,
        attendance=None,
        league=str(league),
        year=None,
        season_type=None,
        postponed=None,
        play_off=play_off,
        distance=None,
        dividends=[],
        pot=None,
        version=version,
        umpires=[],
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_aussportsbetting_game_model(
    dt: datetime.datetime,
    home_team: str,
    away_team: str,
    venue: str | None,
    session: ScrapeSession,
    home_points: float,
    away_points: float,
    home_odds: float,
    away_odds: float,
    league: League,
    play_off: bool,
    version: str,
) -> GameModel:
    return _create_aussportsbetting_game_model(
        dt,
        home_team,
        away_team,
        venue,
        session,
        home_points,
        away_points,
        home_odds,
        away_odds,
        league,
        play_off,
        version=version,
    )


def create_aussportsbetting_game_model(
    dt: datetime.datetime,
    home_team: str,
    away_team: str,
    venue: str | None,
    session: ScrapeSession,
    home_points: float,
    away_points: float,
    home_odds: float,
    away_odds: float,
    league: League,
    play_off: bool,
) -> GameModel:
    """Create a game model based off aus sports betting."""
    if not pytest_is_running.is_running() and dt < datetime.datetime.now().replace(
        tzinfo=dt.tzinfo
    ) - datetime.timedelta(days=7):
        return _cached_create_aussportsbetting_game_model(
            dt=dt,
            home_team=home_team,
            away_team=away_team,
            venue=venue,
            session=session,
            home_points=home_points,
            away_points=away_points,
            home_odds=home_odds,
            away_odds=away_odds,
            league=league,
            play_off=play_off,
            version=GAME_VERSION,
        )
    with session.cache_disabled():
        return _create_aussportsbetting_game_model(
            dt=dt,
            home_team=home_team,
            away_team=away_team,
            venue=venue,
            session=session,
            home_points=home_points,
            away_points=away_points,
            home_odds=home_odds,
            away_odds=away_odds,
            league=league,
            play_off=play_off,
            version=GAME_VERSION,
        )
