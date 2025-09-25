"""Footballdata bookie model."""

from ..bookie_model import BookieModel


def create_footballdata_bookie_model() -> BookieModel:
    """Create bookie model from footballdata."""
    return BookieModel(identifier="bet365", name="Bet365")
