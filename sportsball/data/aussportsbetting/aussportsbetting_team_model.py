"""Aussportsbetting team model."""

from ...cache import MEMORY
from ..team_model import TeamModel
from .aussportsbetting_odds_model import create_aussportsbetting_odds_model


@MEMORY.cache
def create_aussportsbetting_team_model(
    name: str, points: float, odds: float
) -> TeamModel:
    """Create a team model based off aus sports betting."""
    odds_model = create_aussportsbetting_odds_model(odds)
    return TeamModel(
        identifier=name,
        name=name,
        location=None,
        players=[],
        odds=[odds_model],  # pyright: ignore
        points=points,
        ladder_rank=None,
    )
