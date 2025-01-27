"""Tests for the player model class."""
import unittest

from sportsball.data.player_model import PlayerModel


class TestSocialModel(unittest.TestCase):

    def setUp(self):
        self._player_model = PlayerModel(
            identifier="a",
            jersey="45",
            kicks=None,
            fumbles=None,
            fumbles_lost=None,
            field_goals=None,
            field_goals_attempted=10,
        )

    def test_field_goals_attempted(self):
        self.assertEqual(self._player_model.field_goals_attempted, 10)
