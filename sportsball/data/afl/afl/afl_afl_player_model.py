"""AFL AFL player model."""

# pylint: disable=duplicate-code
from ...player_model import PlayerModel


def create_afl_afl_player_model(
    identifier: str,
    player_number: str,
    name: str,
) -> PlayerModel:
    """Create a player model from AFL AFL."""
    return PlayerModel(
        identifier=identifier,
        jersey=player_number,
        kicks=None,
        fumbles=None,
        fumbles_lost=None,
        field_goals=None,
        field_goals_attempted=None,
        offensive_rebounds=None,
        assists=None,
        turnovers=None,
        name=name,
        marks=None,
        handballs=None,
        disposals=None,
        goals=None,
        behinds=None,
        hit_outs=None,
        tackles=None,
        rebounds=None,
        insides=None,
        clearances=None,
        clangers=None,
        free_kicks_for=None,
        free_kicks_against=None,
        brownlow_votes=None,
        contested_possessions=None,
        uncontested_possessions=None,
        contested_marks=None,
        marks_inside=None,
        one_percenters=None,
        bounces=None,
        goal_assists=None,
        percentage_played=None,
    )
