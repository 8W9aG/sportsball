"""AFL AFLTables team model."""

# pylint: disable=too-many-arguments,too-many-locals,duplicate-code,line-too-long
import datetime
import os
from urllib.parse import urlparse

import pytest_is_running
import requests_cache
from bs4 import BeautifulSoup

from ....cache import MEMORY
from ...google.google_news_model import create_google_news_models
from ...league import League
from ...team_model import TeamModel
from ...x.x_social_model import create_x_social_model
from .afl_afltables_player_model import create_afl_afltables_player_model

_TEAM_NAME_MAP = {
    "Melbourne": ["ME"],
    "Geelong": ["GE"],
    "Fitzroy": ["FI"],
    "Collingwood": ["CW"],
    "Essendon": ["ES"],
    "South Melbourne": ["SM"],
    "St Kilda": ["SK"],
    "Carlton": ["CA"],
    "Sydney": ["SM", "SY"],
    "University": ["UN"],
    "Richmond": ["RI"],
    "North Melbourne": ["NM"],
    "Western Bulldogs": ["WB", "FO"],
    "Hawthorn": ["HW"],
    "Brisbane Bears": ["BB"],
    "West Coast": ["WC"],
    "Adelaide": ["AD"],
    "Fremantle": ["FR"],
    "Brisbane Lions": ["BL"],
    "Port Adelaide": ["PA"],
    "Gold Coast": ["GC"],
    "Greater Western Sydney": ["GW"],
}


def _create_afl_afltables_team_model(
    team_url: str,
    players: list[
        tuple[
            str,
            str,
            int | None,
            str,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            float | None,
        ]
    ],
    points: float,
    session: requests_cache.CachedSession,
    last_ladder_ranks: dict[str, int] | None,
    dt: datetime.datetime,
    league: League,
) -> TeamModel:
    response = session.get(team_url)
    soup = BeautifulSoup(response.text, "lxml")
    o = urlparse(team_url)
    last_component = o.path.split("/")[-1]
    identifier, _ = os.path.splitext(last_component)
    h1 = soup.find("h1")
    if h1 is None:
        raise ValueError("h1 is null.")
    name = h1.get_text()
    last_ladder_rank = None
    if last_ladder_ranks is not None and last_ladder_ranks:
        short_names = _TEAM_NAME_MAP[name]
        for short_name in short_names:
            if short_name in last_ladder_ranks:
                last_ladder_rank = last_ladder_ranks[short_name]
                break
    return TeamModel(
        identifier=identifier,
        name=name,
        players=[  # pyright: ignore
            create_afl_afltables_player_model(
                player_url,
                jersey,
                kicks,
                dt,
                session,
                name,
                marks,
                handballs,
                disposals,
                goals,
                behinds,
                hit_outs,
                tackles,
                rebounds,
                insides,
                clearances,
                clangers,
                free_kicks_for,
                free_kicks_against,
                brownlow_votes,
                contested_possessions,
                uncontested_possessions,
                contested_marks,
                marks_inside,
                one_percenters,
                bounces,
                goal_assists,
                percentage_played,
            )
            for player_url, jersey, kicks, name, marks, handballs, disposals, goals, behinds, hit_outs, tackles, rebounds, insides, clearances, clangers, free_kicks_for, free_kicks_against, brownlow_votes, contested_possessions, uncontested_possessions, contested_marks, marks_inside, one_percenters, bounces, goal_assists, percentage_played in players
        ],
        odds=[],
        points=points,
        ladder_rank=last_ladder_rank,
        location=None,
        news=create_google_news_models(name, session, dt, league),
        social=create_x_social_model(identifier, session, dt),
        field_goals=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_afl_afltables_team_model(
    team_url: str,
    players: list[
        tuple[
            str,
            str,
            int | None,
            str,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            float | None,
        ]
    ],
    points: float,
    session: requests_cache.CachedSession,
    last_ladder_ranks: dict[str, int] | None,
    dt: datetime.datetime,
    league: League,
) -> TeamModel:
    return _create_afl_afltables_team_model(
        team_url,
        players,
        points,
        session,
        last_ladder_ranks,
        dt,
        league,
    )


def create_afl_afltables_team_model(
    team_url: str,
    players: list[
        tuple[
            str,
            str,
            int | None,
            str,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            int | None,
            float | None,
        ]
    ],
    points: float,
    session: requests_cache.CachedSession,
    last_ladder_ranks: dict[str, int] | None,
    dt: datetime.datetime,
    league: League,
) -> TeamModel:
    """Create a team model from AFL Tables."""
    if (
        not pytest_is_running.is_running()
        and dt < datetime.datetime.now() - datetime.timedelta(days=7)
    ):
        return _cached_create_afl_afltables_team_model(
            team_url, players, points, session, last_ladder_ranks, dt, league
        )
    with session.cache_disabled():
        return _create_afl_afltables_team_model(
            team_url, players, points, session, last_ladder_ranks, dt, league
        )
