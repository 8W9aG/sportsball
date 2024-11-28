"""Helper functions for columns."""

import pandas as pd

from ...data.columns import COLUMN_SEPARATOR
from ...data.game_model import GAME_ATTENDANCE_COLUMN, GAME_COLUMN_PREFIX
from ...data.player_model import PLAYER_COLUMN_SUFFIX, PLAYER_IDENTIFIER_COLUMN
from ...data.team_model import (TEAM_COLUMN_SUFFIX, TEAM_IDENTIFIER_COLUMN,
                                TEAM_POINTS_COLUMN)
from ...data.venue_model import VENUE_COLUMN_PREFIX, VENUE_IDENTIFIER_COLUMN


def team_column_prefix(team_idx: int) -> str:
    """Generate a prefix for a team column at a given index."""
    return COLUMN_SEPARATOR.join(
        [
            GAME_COLUMN_PREFIX,
            str(team_idx),
            TEAM_COLUMN_SUFFIX,
        ]
    )


def team_identifier_column(team_idx: int) -> str:
    """Generate a team identifier column at a given index."""
    return COLUMN_SEPARATOR.join([team_column_prefix(team_idx), TEAM_IDENTIFIER_COLUMN])


def team_points_column(team_idx: int) -> str:
    """Generate a team points column at a given index."""
    return COLUMN_SEPARATOR.join([team_column_prefix(team_idx), TEAM_POINTS_COLUMN])


def player_column_prefix(team_idx: int, player_idx: int | None) -> str:
    """Generate a prefix for a player column at a given index."""
    if player_idx is None:
        return COLUMN_SEPARATOR.join(
            [
                team_column_prefix(team_idx),
                PLAYER_COLUMN_SUFFIX,
            ]
        )
    return COLUMN_SEPARATOR.join(
        [
            team_column_prefix(team_idx),
            str(player_idx),
            PLAYER_COLUMN_SUFFIX,
        ]
    )


def player_identifier_column(team_idx: int, player_idx: int) -> str:
    """Generate a team points column at a given index."""
    return COLUMN_SEPARATOR.join(
        [player_column_prefix(team_idx, player_idx), PLAYER_IDENTIFIER_COLUMN]
    )


def attendance_column() -> str:
    """Generate an attendance column."""
    return COLUMN_SEPARATOR.join([GAME_COLUMN_PREFIX, GAME_ATTENDANCE_COLUMN])


def find_team_count(df: pd.DataFrame) -> int:
    """Find the number of teams in the dataframe."""
    team_count = 0
    while True:
        if team_identifier_column(team_count) not in df.columns.values:
            break
        team_count += 1
    return team_count


def venue_identifier_column() -> str:
    """Generate a venue identifier column."""
    return COLUMN_SEPARATOR.join(
        [GAME_COLUMN_PREFIX, VENUE_COLUMN_PREFIX, VENUE_IDENTIFIER_COLUMN]
    )
