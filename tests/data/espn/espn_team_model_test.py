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

    def test_homeruns(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-8.json")) as f:
            statistics_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "10_score.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "10_teams.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "10_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/teams/10/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "2_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/hockey/leagues/nhl/seasons/2025/teams/2/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "165_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/coaches/165?lang=en&region=us", content=f.read())

            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.MLB,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.home_runs, 1)

    def test_even_strength_saves(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-9.json")) as f:
            statistics_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "2_score.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "2_teams.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "2_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/hockey/leagues/nhl/seasons/2025/teams/2/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "2018453_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/hockey/leagues/nhl/seasons/2025/coaches/2018453?lang=en&region=us", content=f.read())

            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.NHL,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.even_strength_saves, 0)

    def test_doubles(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-10.json")) as f:
            statistics_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "15_score.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "15_teams.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "15_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/teams/15/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "157_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/coaches/157?lang=en&region=us", content=f.read())
            

            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.MLB,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.doubles, 4)

    def test_second_chance_points(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-11.json")) as f:
            statistics_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "2305_score.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "2305_teams.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "2305_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/teams/2305/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "71332_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/coaches/71332?lang=en&region=us", content=f.read())
            
            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.NCAAB,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.second_chance_points, 5.0)

    def test_ytd_goals(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-12.json")) as f:
            statistics_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "23_score.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "23_teams.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "23_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/hockey/leagues/nhl/seasons/2025/teams/23/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "4873586_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/hockey/leagues/nhl/seasons/2025/coaches/4873586?lang=en&region=us", content=f.read())
            
            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.NHL,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.ytd_goals, 0.0)

    def test_pitcher_notes(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-13.json")) as f:
            statistics_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "19_score.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "19_teams.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "19_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/teams/19/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "154_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/coaches/154?lang=en&region=us", content=f.read())
            
            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.MLB,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.name, "Dodgers")

    def test_sac_fly(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-14.json")) as f:
            statistics_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "9_score.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "9_teams.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "9_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/teams/9/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "170_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/coaches/170?lang=en&region=us", content=f.read())
            
            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.MLB,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.name, "Twins")

    def test_picked_off(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-16.json")) as f:
            statistics_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "9_score-2.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "9_teams-2.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "9_coaches-2.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/teams/9/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "170_coaches-2.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/seasons/2025/coaches/170?lang=en&region=us", content=f.read())
            
            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.MLB,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.name, "Twins")

    def test_plus_minus(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        statistics_dict = {}
        with open(os.path.join(self.dir, "0_statistics-17.json")) as f:
            statistics_dict = json.load(f)
        score_dict = {}
        with open(os.path.join(self.dir, "5_score.json")) as f:
            score_dict = json.load(f)
        team_dict = {}
        with open(os.path.join(self.dir, "5_teams.json")) as f:
            team_dict = json.load(f)
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "5_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/basketball/leagues/wnba/seasons/2025/teams/5/coaches?lang=en&region=us", content=f.read())
            with open(os.path.join(self.dir, "524_coaches.json"), "rb") as f:
                m.get("http://sports.core.api.espn.com/v2/sports/basketball/leagues/wnba/seasons/2025/coaches/524?lang=en&region=us", content=f.read())
            
            team_model = create_espn_team_model(
                session=self._session,
                team=team_dict,
                roster_dict={},
                odds=[],
                score_dict=score_dict,
                dt=dt,
                league=League.WNBA,
                positions_validator={},
                statistics_dict=statistics_dict,
            )
            self.assertEqual(team_model.plus_minus, 0.0)
