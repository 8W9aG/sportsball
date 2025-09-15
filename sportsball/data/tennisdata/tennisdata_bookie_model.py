"""Tennisdata bookie model."""

from ..bookie_model import BookieModel


def create_tennisdata_bookie_model() -> BookieModel:
    """Create bookie model from tennisdata."""
    return BookieModel(identifier="bet365", name="Bet365")
