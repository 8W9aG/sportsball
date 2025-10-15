"""Footballdata odds model."""

from ..bet import Bet
from ..team_model import OddsModel
from .footballdata_bookie_model import create_footballdata_bookie_model


def create_footballdata_odds_model(odds: str, draw_odds: str) -> OddsModel:
    """Create an odds model based off footballdata."""
    odds_number = float(odds)
    draw_odds_number = float(draw_odds)
    final_odds = (odds_number * draw_odds_number) / (odds_number + draw_odds_number)
    bookie = create_footballdata_bookie_model()
    return OddsModel(
        odds=final_odds, bookie=bookie, dt=None, canonical=True, bet=str(Bet.WIN)
    )
