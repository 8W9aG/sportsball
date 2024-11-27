"""Tests for the skill feature class."""
import datetime
import unittest

import sportsball as spb
import pandas as pd
from sportsball.strategy.features.columns import team_identifier_column, team_points_column, player_identifier_column
from sportsball.strategy.features.skill_feature import _find_matches, SkillFeature, _find_player_team, _create_player_teams, _rank_player_predictions
from openskill.models import PlackettLuce


class TestSkillFeatureClass(unittest.TestCase):

    def setUp(self):
        self._skill_feature = SkillFeature(year_slices=[1])

    def test_process(self):
        df = pd.DataFrame(data={
            spb.data.game_model.FULL_GAME_DT_COLUMN: [datetime.datetime(2009, 12, 31, 0, 0, 0), datetime.datetime(2010, 1, 1, 0, 0, 0)],
            team_identifier_column(0): ["1", "1"],
            team_identifier_column(1): ["2", "2"],
            team_points_column(0): [0, 1],
            team_points_column(1): [2, 3],
            player_identifier_column(0, 0): ["1", "1"],
            player_identifier_column(1, 0): ["2", "2"],
        })
        df = self._skill_feature.process(df)
        self.assertIsNotNone(df)

    def test_find_matches(self):
        df = pd.DataFrame(data={
            spb.data.game_model.FULL_GAME_DT_COLUMN: [datetime.datetime(2009, 12, 31, 0, 0, 0), datetime.datetime(2010, 1, 1, 0, 0, 0)],
            team_identifier_column(0): ["1", "1"],
            team_identifier_column(1): ["2", "2"],
            team_points_column(0): [0, 1],
            team_points_column(1): [2, 3],
            player_identifier_column(0, 0): ["1", "1"],
            player_identifier_column(1, 0): ["2", "2"],
        })
        team_model = PlackettLuce()
        player_model = PlackettLuce()
        teams = {
            "1": team_model.rating(name="1"),
        }
        players = {
            "1": player_model.rating(name="1"),
        }
        for _, row in df.iterrows():
            _find_matches(row, 1, 5, teams, players)

    def test_find_player_team(self):
        df = pd.DataFrame(data={
            spb.data.game_model.FULL_GAME_DT_COLUMN: [datetime.datetime(2009, 12, 31, 0, 0, 0), datetime.datetime(2010, 1, 1, 0, 0, 0)],
            team_identifier_column(0): ["1", "1"],
            team_identifier_column(1): ["2", "2"],
            team_points_column(0): [0, 1],
            team_points_column(1): [2, 3],
            player_identifier_column(0, 0): ["1", "1"],
            player_identifier_column(1, 0): ["2", "2"],
        })
        players = {}
        for _, row in df.iterrows():
            _find_player_team(1, players, row, "all", 0)

    def test_find_player_team_without_player_index_column(self):
        df = pd.DataFrame(data={
            spb.data.game_model.FULL_GAME_DT_COLUMN: [datetime.datetime(2009, 12, 31, 0, 0, 0), datetime.datetime(2010, 1, 1, 0, 0, 0)],
            team_identifier_column(0): ["1", "1"],
            team_identifier_column(1): ["2", "2"],
            team_points_column(0): [0, 1],
            team_points_column(1): [2, 3],
            player_identifier_column(0, 0): ["1", "1"],
            player_identifier_column(1, 0): ["2", "2"],
        })
        players = {}
        for _, row in df.iterrows():
            _find_player_team(5, players, row, "all", 0)

    def test_create_player_teams(self):
        df = pd.DataFrame(data={
            spb.data.game_model.FULL_GAME_DT_COLUMN: [datetime.datetime(2009, 12, 31, 0, 0, 0), datetime.datetime(2010, 1, 1, 0, 0, 0)],
            team_identifier_column(0): ["1", "1"],
            team_identifier_column(1): ["2", "2"],
            team_points_column(0): [0, 1],
            team_points_column(1): [2, 3],
            player_identifier_column(0, 0): ["1", "1"],
            player_identifier_column(1, 0): ["2", "2"],
        })
        _, players = _create_player_teams(df, 2, 2)
        self.assertSetEqual(set(players.keys()), {"1", "2"})

    def test_rank_player_predictions(self):
        df = pd.DataFrame(data={
            spb.data.game_model.FULL_GAME_DT_COLUMN: [datetime.datetime(2009, 12, 31, 0, 0, 0), datetime.datetime(2010, 1, 1, 0, 0, 0)],
            team_identifier_column(0): ["1", "1"],
            team_identifier_column(1): ["2", "2"],
            team_points_column(0): [0, 1],
            team_points_column(1): [2, 3],
            player_identifier_column(0, 0): ["1", "1"],
            player_identifier_column(1, 0): ["2", "2"],
        })
        player_model, _ = _create_player_teams(df, 2, 2)
        for _, row in df.iterrows():
            _rank_player_predictions(row, player_model, [[], []], "all")