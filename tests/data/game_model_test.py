"""Tests for the game model class."""
import datetime
import unittest

from sportsball.data.game_model import GameModel, VERSION
from sportsball.data.league import League


class TestGameModel(unittest.TestCase):

    def setUp(self):
        self._game_model = GameModel(
            dt=datetime.datetime(2010, 1, 1, 10, 10, 0),
            week=None,
            game_number=None,
            venue=None,
            teams=[],
            end_dt=None,
            attendance=None,
            league=str(League.NBA),
            year=None,
            season_type=None,
            postponed=True,
            play_off=None,
            distance=None,
            dividends=[],
            pot=None,
            umpires=[],
            version=VERSION,
            best_of=None,
        )

    def test_postponed(self):
        self.assertTrue(self._game_model.postponed)
