"""NBA API team model."""

# pylint: disable=too-many-arguments,unused-argument
import datetime

import pandas as pd
import pytest_is_running
import requests_cache

from ....cache import MEMORY
from ...google.google_news_model import create_google_news_models
from ...league import League
from ...team_model import TeamModel
from ...x.x_social_model import create_x_social_model


def _create_nba_nba_team_model(
    row: pd.Series,
    home: bool,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
    league_id: str,
) -> TeamModel | None:
    """Create a team model from NBA API."""
    suffix = "_A" if home else "_B"
    # game_rotation = gamerotation.GameRotation(game_id=row["GAME_ID"])
    # player_dict = {}
    # for _, gr_row in game_rotation.get_data_frames()[int(home)].iterrows():
    #     player_dict[gr_row["PERSON_ID"]] = gr_row
    identifier = row["TEAM_ID" + suffix]
    if identifier is None:
        return None
    name = row["TEAM_NAME" + suffix]

    return TeamModel(
        identifier=str(identifier),
        name=name,
        players=[  # type: ignore
            # create_nba_nba_player_model(v, player_index) for v in player_dict.values()
        ],
        odds=[],
        points=float(row["PTS" + suffix]),
        ladder_rank=None,
        location=None,
        news=create_google_news_models(name, session, dt, league),
        social=create_x_social_model(str(identifier), session, dt),
        field_goals=row["FGM" + suffix],
        field_goals_attempted=row["FGA" + suffix],
        offensive_rebounds=row["OREB" + suffix],
        assists=row["AST" + suffix],
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_nba_nba_team_model(
    row: pd.Series,
    home: bool,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
    league_id: str,
) -> TeamModel | None:
    return _create_nba_nba_team_model(row, home, session, dt, league, league_id)


def create_nba_nba_team_model(
    row: pd.Series,
    home: bool,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
    league_id: str,
) -> TeamModel | None:
    """Create a team model from NBA API."""
    if not pytest_is_running.is_running() and dt < datetime.datetime.now().replace(
        tzinfo=dt.tzinfo
    ) - datetime.timedelta(days=7):
        return _cached_create_nba_nba_team_model(
            row, home, session, dt, league, league_id
        )
    with session.cache_disabled():
        return _create_nba_nba_team_model(row, home, session, dt, league, league_id)
