"""Tests for the combined game model class."""
import datetime
import os
import unittest

import requests_mock
import requests_cache
from sportsball.data.combined.combined_game_model import create_combined_game_model
from sportsball.data.league import League
from sportsball.data.season_type import SeasonType
from sportsball.data.game_model import GameModel, VERSION


class TestCombinedGameModel(unittest.TestCase):

    def setUp(self):
        self._session = requests_cache.CachedSession(backend="memory")
        self.dir = os.path.dirname(__file__)

    def test_dt(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        with requests_mock.Mocker() as m:
            game_model = GameModel(
                dt=dt,
                week=None,
                game_number=None,
                venue=None,
                teams=[],
                end_dt=None,
                attendance=None,
                league=str(League.NBA),
                year=None,
                season_type=SeasonType.REGULAR,
                postponed=True,
                play_off=None,
                distance=None,
                dividends=[],
                pot=None,
                umpires=[],
                version=VERSION,
                best_of=None,
            )
            names = {}
            coach_names = {}
            players_ffill = {}
            teams_ffill = {}
            coaches_ffill = {}
            umpires_ffill = {}
            combined_game_model = create_combined_game_model(
                game_models=[game_model],
                venue_identity_map={},
                team_identity_map={},
                player_identity_map={},
                session=self._session,
                names=names,
                coach_names=coach_names,
                last_game_number=None,
                player_ffill=players_ffill,
                team_ffill=teams_ffill,
                coach_ffill=coaches_ffill,
                umpire_ffill=umpires_ffill,
            )
            self.assertEqual(combined_game_model.dt, dt)
