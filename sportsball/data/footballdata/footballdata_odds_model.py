"""Footballdata odds model."""

from ..bet import Bet
from ..team_model import OddsModel
from .footballdata_bookie_model import create_footballdata_bookie_model


def create_footballdata_odds_model(odds: str) -> OddsModel:
    """Create an odds model based off footballdata."""
    bookie = create_footballdata_bookie_model()
    return OddsModel(
        odds=float(odds), bookie=bookie, dt=None, canonical=True, bet=str(Bet.WIN)
    )
