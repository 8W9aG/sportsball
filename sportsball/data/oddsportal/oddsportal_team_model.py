"""Odds Portal team model."""

# pylint: disable=too-many-arguments,duplicate-code,line-too-long,too-many-locals
import datetime
from typing import Any

import pytest_is_running
import requests_cache

from ...cache import MEMORY
from ..google.google_news_model import create_google_news_models
from ..league import League
from ..team_model import TeamModel
from ..x.x_social_model import create_x_social_model
from .oddsportal_odds_model import create_oddsportal_odds_model


def _create_oddsportal_team_model(
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    team_name: str,
    league: League,
    points: float | None,
    default_bet_id: str,
    default_scope_id: str,
    bookie_names: dict[str, str],
    team_idx: int,
    parsed_data: dict[str, Any],
) -> TeamModel:
    try:
        odds_data = parsed_data["d"]["oddsdata"]["back"][
            f"E-{default_bet_id}-{default_scope_id}-0-0-0"
        ]
    except KeyError:
        back = parsed_data["d"]["oddsdata"]["back"]
        odds_data = back[sorted(list(back.keys()))[0]]
    try:
        outcome_id = odds_data["outcomeId"][team_idx]
    except KeyError:
        outcome_id = odds_data["outcomeId"][str(team_idx)]
    history = odds_data["history"][outcome_id]
    odds_models = []
    for bookie_id, bookie_name in bookie_names.items():
        for odds, _, timestamp in history.get(bookie_id, []):
            odds_models.append(
                create_oddsportal_odds_model(
                    odds,
                    datetime.datetime.fromtimestamp(timestamp),
                    bookie_name,
                    bookie_id,  # type: ignore
                )
            )

    return TeamModel(
        identifier=team_name,
        name=team_name,
        points=points,
        players=[],
        odds=odds_models,
        ladder_rank=None,
        location=None,
        news=create_google_news_models(team_name, session, dt, league),
        social=create_x_social_model(team_name, session, dt),
        field_goals=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_oddsportal_team_model(
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    team_name: str,
    league: League,
    points: float | None,
    default_bet_id: str,
    default_scope_id: str,
    bookie_names: dict[str, str],
    team_idx: int,
    parsed_data: dict[str, Any],
) -> TeamModel:
    return _create_oddsportal_team_model(
        session,
        dt,
        team_name,
        league,
        points,
        default_bet_id,
        default_scope_id,
        bookie_names,
        team_idx,
        parsed_data,
    )


def create_oddsportal_team_model(
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    team_name: str,
    league: League,
    points: float | None,
    default_bet_id: str,
    default_scope_id: str,
    bookie_names: dict[str, str],
    team_idx: int,
    parsed_data: dict[str, Any],
) -> TeamModel:
    """Create a team model based off the odds portal response."""
    if not pytest_is_running.is_running() and dt < datetime.datetime.now().replace(
        tzinfo=dt.tzinfo
    ) - datetime.timedelta(days=7):
        return _cached_create_oddsportal_team_model(
            session,
            dt,
            team_name,
            league,
            points,
            default_bet_id,
            default_scope_id,
            bookie_names,
            team_idx,
            parsed_data,
        )
    with session.cache_disabled():
        return _create_oddsportal_team_model(
            session,
            dt,
            team_name,
            league,
            points,
            default_bet_id,
            default_scope_id,
            bookie_names,
            team_idx,
            parsed_data,
        )
