"""Footballdata game model."""

# pylint: disable=too-many-arguments,duplicate-code
import datetime

import pytest_is_running
from dateutil.parser import parse
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..game_model import VERSION as GAME_VERSION
from ..game_model import GameModel
from ..league import League
from ..team_model import VERSION as TEAM_VERSION
from ..umpire_model import VERSION as UMPIRE_VERSION
from .footballdata_team_model import create_footballdata_team_model
from .footballdata_umpire_model import create_footballdata_umpire_model


def _create_footballdata_game_model(
    session: ScrapeSession,
    league: League,
    dt: datetime.datetime,
    home_team: str,
    away_team: str,
    full_time_home_goals: str,
    full_time_away_goals: str,
    referee: str | None,
    home_shots: str | None,
    away_shots: str,
    home_shots_on_target: str,
    away_shots_on_target: str,
    home_fouls: str,
    away_fouls: str,
    home_yellow_cards: str,
    away_yellow_cards: str,
    home_red_cards: str,
    away_red_cards: str,
    home_odds: str,
    away_odds: str,
    version: str,
) -> GameModel:
    home_team_model = create_footballdata_team_model(
        session=session,
        league=league,
        dt=dt,
        name=home_team,
        full_time_goals=full_time_home_goals,
        shots=home_shots,
        shots_on_target=home_shots_on_target,
        fouls=home_fouls,
        yellow_cards=home_yellow_cards,
        red_cards=home_red_cards,
        odds=home_odds,
        version=TEAM_VERSION,
    )
    away_team_model = create_footballdata_team_model(
        session=session,
        league=league,
        dt=dt,
        name=away_team,
        full_time_goals=full_time_away_goals,
        shots=away_shots,
        shots_on_target=away_shots_on_target,
        fouls=away_fouls,
        yellow_cards=away_yellow_cards,
        red_cards=away_red_cards,
        odds=away_odds,
        version=TEAM_VERSION,
    )
    return GameModel(
        dt=dt,
        week=None,
        game_number=None,
        venue=None,
        teams=[home_team_model, away_team_model],
        end_dt=None,
        attendance=None,
        league=str(league),
        year=None,
        season_type=None,
        postponed=None,
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        version=version,
        umpires=[
            create_footballdata_umpire_model(name=referee, version=UMPIRE_VERSION)  # type: ignore
        ]
        if referee is not None
        else [],
        best_of=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_footballdata_game_model(
    session: ScrapeSession,
    league: League,
    dt: datetime.datetime,
    home_team: str,
    away_team: str,
    full_time_home_goals: str,
    full_time_away_goals: str,
    referee: str | None,
    home_shots: str | None,
    away_shots: str,
    home_shots_on_target: str,
    away_shots_on_target: str,
    home_fouls: str,
    away_fouls: str,
    home_yellow_cards: str,
    away_yellow_cards: str,
    home_red_cards: str,
    away_red_cards: str,
    home_odds: str,
    away_odds: str,
    version: str,
) -> GameModel:
    return _create_footballdata_game_model(
        session=session,
        league=league,
        dt=dt,
        home_team=home_team,
        away_team=away_team,
        full_time_home_goals=full_time_home_goals,
        full_time_away_goals=full_time_away_goals,
        referee=referee,
        home_shots=home_shots,
        away_shots=away_shots,
        home_shots_on_target=home_shots_on_target,
        away_shots_on_target=away_shots_on_target,
        home_fouls=home_fouls,
        away_fouls=away_fouls,
        home_yellow_cards=home_yellow_cards,
        away_yellow_cards=away_yellow_cards,
        home_red_cards=home_red_cards,
        away_red_cards=away_red_cards,
        home_odds=home_odds,
        away_odds=away_odds,
        version=version,
    )


def create_footballdata_game_model(
    session: ScrapeSession,
    league: League,
    date: str,
    time: str,
    home_team: str,
    away_team: str,
    full_time_home_goals: str,
    full_time_away_goals: str,
    referee: str | None,
    home_shots: str | None,
    away_shots: str,
    home_shots_on_target: str,
    away_shots_on_target: str,
    home_fouls: str,
    away_fouls: str,
    home_yellow_cards: str,
    away_yellow_cards: str,
    home_red_cards: str,
    away_red_cards: str,
    home_odds: str,
    away_odds: str,
) -> GameModel:
    """Create a game model based off footballdata."""
    dt = parse(" ".join([date, time]))
    if not pytest_is_running.is_running() and dt < datetime.datetime.now().replace(
        tzinfo=dt.tzinfo
    ) - datetime.timedelta(days=7):
        return _cached_create_footballdata_game_model(
            session=session,
            league=league,
            dt=dt,
            home_team=home_team,
            away_team=away_team,
            full_time_home_goals=full_time_home_goals,
            full_time_away_goals=full_time_away_goals,
            referee=referee,
            home_shots=home_shots,
            away_shots=away_shots,
            home_shots_on_target=home_shots_on_target,
            away_shots_on_target=away_shots_on_target,
            home_fouls=home_fouls,
            away_fouls=away_fouls,
            home_yellow_cards=home_yellow_cards,
            away_yellow_cards=away_yellow_cards,
            home_red_cards=home_red_cards,
            away_red_cards=away_red_cards,
            home_odds=home_odds,
            away_odds=away_odds,
            version=GAME_VERSION,
        )
    with session.cache_disabled():
        return _create_footballdata_game_model(
            session=session,
            league=league,
            dt=dt,
            home_team=home_team,
            away_team=away_team,
            full_time_home_goals=full_time_home_goals,
            full_time_away_goals=full_time_away_goals,
            referee=referee,
            home_shots=home_shots,
            away_shots=away_shots,
            home_shots_on_target=home_shots_on_target,
            away_shots_on_target=away_shots_on_target,
            home_fouls=home_fouls,
            away_fouls=away_fouls,
            home_yellow_cards=home_yellow_cards,
            away_yellow_cards=away_yellow_cards,
            home_red_cards=home_red_cards,
            away_red_cards=away_red_cards,
            home_odds=home_odds,
            away_odds=away_odds,
            version=GAME_VERSION,
        )
