"""Tests for the ESPN team model class."""
import datetime
import json
import os
import unittest

import requests_mock
from scrapesession.scrapesession import ScrapeSession
from sportsball.data.espn.espn_team_model import create_espn_team_model
from sportsball.data.league import League
from sportsball.data.season_type import SeasonType


class TestESPNTeamModel(unittest.TestCase):

    def setUp(self):
        self._session = ScrapeSession(backend="memory")
        self.dir = os.path.dirname(__file__)

    def test_total_giveaways(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-5.json")) as f:
            statistics_dict = json.load(f)
        roster_dict = {}
        with open(os.path.join(self.dir, "356_roster.json")) as f:
            roster_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "356_score.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "356_teams.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "0_statistics-7.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/events/401752795/competitions/401752795/competitors/356/roster/4429960/statistics/0?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "356_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2025/teams/356/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "559947_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2025/coaches/559947?lang=en&region=us", content=f.read())
            
            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.NCAAF,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.total_giveaways, 0)
