"""Tests for the ESPN game model class."""
import datetime
import os
import unittest

import requests_mock
import requests_cache
from sportsball.data.espn.espn_game_model import create_espn_game_model
from sportsball.data.league import League
from sportsball.data.season_type import SeasonType


class TestESPNGameModel(unittest.TestCase):

    def setUp(self):
        self._session = requests_cache.CachedSession(backend="memory")
        self.dir = os.path.dirname(__file__)

    def test_dt(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        with requests_mock.Mocker() as m:

            game_model = create_espn_game_model(
                competition={
                    "date": dt.isoformat(),
                },
                week=1,
                game_number=1,
                session=self._session,
                league=League.NFL,
                year=2016,
                season_type=SeasonType.REGULAR,
                positions_validator={},
            )

            self.assertEqual(game_model.dt, dt)
