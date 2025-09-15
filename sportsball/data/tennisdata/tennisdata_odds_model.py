"""Tennisdata odds model."""

from ..bet import Bet
from ..team_model import OddsModel
from .tennisdata_bookie_model import create_tennisdata_bookie_model


def create_tennisdata_odds_model(odds: str) -> OddsModel:
    """Create an odds model based off tennisdata."""
    bookie = create_tennisdata_bookie_model()
    return OddsModel(
        odds=float(odds), bookie=bookie, dt=None, canonical=True, bet=str(Bet.WIN)
    )
