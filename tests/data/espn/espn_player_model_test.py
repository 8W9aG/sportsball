"""Tests for the ESPN player model class."""
import datetime
import os
import unittest

import requests_mock
from scrapesession.scrapesession import ScrapeSession
from sportsball.data.espn.espn_player_model import create_espn_player_model


class TestESPNPlayerModel(unittest.TestCase):

    def setUp(self):
        self._session = ScrapeSession(backend="memory")
        self.dir = os.path.dirname(__file__)

    def test_identifier(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        identifier = "a"
        statistics_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/401671855/competitions/401671855/competitors/5/roster/16837/statistics/0?lang=en&region=us"
        athletes_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/athletes/16837?lang=en&region=us"
        position_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/positions/32?lang=en&region=us"
        college_url = "http://sports.core.api.espn.com/v2/colleges/2287?lang=en&region=us"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "16837_statistics.json"), "rb") as f:
                m.get(statistics_url, content=f.read())
            with open(os.path.join(self.dir, "16837_athletes.json"), "rb") as f:
                m.get(athletes_url, content=f.read())
            with open(os.path.join(self.dir, "32_positions.json"), "rb") as f:
                m.get(position_url, content=f.read())
            with open(os.path.join(self.dir, "2287_colleges.json"), "rb") as f:
                m.get(college_url, content=f.read())
            m.get('https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=40.511&longitude=-88.993&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FChicago&start_date=2023-09-14&end_date=2023-09-15&format=flatbuffers')
            player_model = create_espn_player_model(
                session=self._session,
                player={
                    "playerId": identifier,
                    "period": 0,
                    "active": False,
                    "starter": True,
                    "forPlayerId": 0,
                    "jersey": "93",
                    "valid": True,
                    "athlete": {
                        "$ref": athletes_url,
                    },
                    "position": {
                        "$ref": position_url,
                    },
                    "statistics": {
                        "$ref": statistics_url,
                    },
                    "didNotPlay": False,
                    "displayName": "S. Harris",
                },
                dt=dt,
                positions_validator={"DT": "DT"},
            )

            self.assertEqual(player_model.identifier, identifier)

    def test_no_birth_date(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        identifier = "a"
        statistics_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/401671855/competitions/401671855/competitors/5/roster/16837/statistics/0?lang=en&region=us"
        athletes_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2024/athletes/102597?lang=en&region=us"
        position_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/positions/32?lang=en&region=us"
        college_url = "http://sports.core.api.espn.com/v2/colleges/264?lang=en&region=us"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "16837_statistics.json"), "rb") as f:
                m.get(statistics_url, content=f.read())
            with open(os.path.join(self.dir, "102597_athletes.json"), "rb") as f:
                m.get(athletes_url, content=f.read())
            with open(os.path.join(self.dir, "32_positions.json"), "rb") as f:
                m.get(position_url, content=f.read())
            with open(os.path.join(self.dir, "264_colleges.json"), "rb") as f:
                m.get(college_url, content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=39.218056&longitude=-76.069444&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FNew_York&start_date=2023-09-14&end_date=2023-09-15&format=flatbuffers")
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=47.0&longitude=-120.0&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FLos_Angeles&start_date=2023-09-14&end_date=2023-09-15&format=flatbuffers")
            player_model = create_espn_player_model(
                session=self._session,
                player={
                    "playerId": identifier,
                    "period": 0,
                    "active": False,
                    "starter": True,
                    "forPlayerId": 0,
                    "jersey": "93",
                    "valid": True,
                    "athlete": {
                        "$ref": athletes_url,
                    },
                    "position": {
                        "$ref": position_url,
                    },
                    "statistics": {
                        "$ref": statistics_url,
                    },
                    "didNotPlay": False,
                    "displayName": "S. Harris",
                },
                dt=dt,
                positions_validator={"DT": "DT"},
            )

            self.assertIsNone(player_model.birth_date)

    def test_kick_extra_points(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        identifier = "4565184"
        statistics_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/events/401756846/competitions/401756846/competitors/2306/roster/4565184/statistics/0?lang=en&region=us"
        athletes_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2025/athletes/4565184?lang=en&region=us"
        position_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/positions/1?lang=en&region=us"
        college_url = "http://sports.core.api.espn.com/v2/colleges/2306?lang=en&region=us"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "4565184_statistics.json"), "rb") as f:
                m.get(statistics_url, content=f.read())
            with open(os.path.join(self.dir, "4565184_athletes.json"), "rb") as f:
                m.get(athletes_url, content=f.read())
            with open(os.path.join(self.dir, "1_positions.json"), "rb") as f:
                m.get(position_url, content=f.read())
            with open(os.path.join(self.dir, "2306_colleges.json"), "rb") as f:
                m.get(college_url, content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=39.1914&longitude=-96.5809&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FChicago&start_date=2023-09-14&end_date=2023-09-15&format=flatbuffers")
            player_model = create_espn_player_model(
                session=self._session,
                player={
                    "playerId": identifier,
                    "period": 0,
                    "active": False,
                    "starter": False,
                    "forPlayerId": 0,
                    "jersey": "5",
                    "valid": False,
                    "athlete": {
                        "$ref": athletes_url,
                    },
                    "position": {
                        "$ref": position_url,
                    },
                    "statistics": {
                        "$ref": statistics_url,
                    },
                    "didNotPlay": False,
                    "displayName": "J. Bradley",
                },
                dt=dt,
                positions_validator={"WR": "WR"},
            )

            self.assertEqual(player_model.kick_extra_points, 0.0)

    def test_attempts_in_box(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        identifier = "291609"
        statistics_url = "http://sports.core.api.espn.com/v2/sports/soccer/leagues/eng.1/events/740617/competitions/740617/competitors/331/roster/291609/statistics/0?lang=en&region=us"
        athletes_url = "http://sports.core.api.espn.com/v2/sports/soccer/leagues/eng.1/seasons/2025/athletes/291609?lang=en&region=us"
        position_url = "http://sports.core.api.espn.com/v2/sports/soccer/leagues/eng.1/positions/1?lang=en&region=us"
        college_url = "http://sports.core.api.espn.com/v2/colleges/2306?lang=en&region=us"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "0_statistics.json"), "rb") as f:
                m.get(statistics_url, content=f.read())
            with open(os.path.join(self.dir, "291609_athletes.json"), "rb") as f:
                m.get(athletes_url, content=f.read())
            with open(os.path.join(self.dir, "1_positions-2.json"), "rb") as f:
                m.get(position_url, content=f.read())
            player_model = create_espn_player_model(
                session=self._session,
                player={
                    "playerId": identifier,
                    "period": 0,
                    "active": True,
                    "starter": True,
                    "jersey": "1",
                    "athlete": {
                        "$ref": athletes_url,
                    },
                    "position": {
                        "$ref": position_url,
                    },
                    "statistics": {
                        "$ref": statistics_url,
                    },
                    "subbedIn": {
                        "didSub": False,
                    },
                    "subbedOut": {
                        "didSub": False
                    },
                    "formationPlace": "1",
                },
                dt=dt,
                positions_validator={"G": "G"},
            )

            self.assertEqual(player_model.attempts_in_box, 8)

    def test_second_assists(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        identifier = "141438"
        statistics_url = "http://sports.core.api.espn.com/v2/sports/soccer/leagues/fifa.world/events/633826/competitions/633826/competitors/628/roster/141438/statistics/0?lang=en&region=us"
        athletes_url = "http://sports.core.api.espn.com/v2/sports/soccer/leagues/fifa.world/seasons/2022/athletes/141438?lang=en&region=us"
        position_url = "http://sports.core.api.espn.com/v2/sports/soccer/leagues/fifa.world/positions/1?lang=en&region=us"
        college_url = "http://sports.core.api.espn.com/v2/colleges/2306?lang=en&region=us"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "0_statistics-2.json"), "rb") as f:
                m.get(statistics_url, content=f.read())
            with open(os.path.join(self.dir, "141438_athletes.json"), "rb") as f:
                m.get(athletes_url, content=f.read())
            with open(os.path.join(self.dir, "1_positions-3.json"), "rb") as f:
                m.get(position_url, content=f.read())
            player_model = create_espn_player_model(
                session=self._session,
                player={
                    "playerId": identifier,
                    "period": 0,
                    "active": True,
                    "starter": True,
                    "jersey": "1",
                    "athlete": {
                        "$ref": athletes_url,
                    },
                    "position": {
                        "$ref": position_url,
                    },
                    "statistics": {
                        "$ref": statistics_url,
                    },
                    "subbedIn": {
                        "didSub": False,
                    },
                    "subbedOut": {
                        "didSub": False
                    },
                    "formationPlace": "1",
                },
                dt=dt,
                positions_validator={"G": "G"},
            )
            self.assertEqual(player_model.second_assists, 0.0)

    def test_qbr(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        identifier = "4870857"
        statistics_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/events/401756846/competitions/401756846/competitors/2306/roster/4870857/statistics/0?lang=en&region=us"
        athletes_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2025/athletes/4870857?lang=en&region=us"
        position_url = "http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/positions/8?lang=en&region=us"
        college_url = "http://sports.core.api.espn.com/v2/colleges/2306?lang=en&region=us"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "0_statistics-3.json"), "rb") as f:
                m.get(statistics_url, content=f.read())
            with open(os.path.join(self.dir, "4870857_athletes.json"), "rb") as f:
                m.get(athletes_url, content=f.read())
            with open(os.path.join(self.dir, "8_positions.json"), "rb") as f:
                m.get(position_url, content=f.read())
            with open(os.path.join(self.dir, "2306_colleges.json"), "rb") as f:
                m.get(college_url, content=f.read())
            player_model = create_espn_player_model(
                session=self._session,
                player={
                    "playerId": identifier,
                    "period": 0,
                    "active": False,
                    "starter": False,
                    "forPlayerId": 0,
                    "jersey": "2",
                    "valid": False,
                    "athlete": {
                        "$ref": athletes_url,
                    },
                    "position": {
                        "$ref": position_url,
                    },
                    "statistics": {
                        "$ref": statistics_url,
                    },
                    "didNotPlay": False,
                    "displayName": "Av. Johnson",
                },
                dt=dt,
                positions_validator={"QB": "QB"},
            )
            self.assertEqual(player_model.qbr, 72.85)

    def test_turnover_points(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        identifier = "4433569"
        statistics_url = "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/events/401708406/competitions/401708406/competitors/2/roster/4433569/statistics/0?lang=en&region=us"
        athletes_url = "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/athletes/4433569?lang=en&region=us"
        position_url = "http://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/positions/2?lang=en&region=us"
        college_url = "http://sports.core.api.espn.com/v2/colleges/2?lang=en&region=us"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "0_statistics-4.json"), "rb") as f:
                m.get(statistics_url, content=f.read())
            with open(os.path.join(self.dir, "4433569_athletes.json"), "rb") as f:
                m.get(athletes_url, content=f.read())
            with open(os.path.join(self.dir, "2_positions.json"), "rb") as f:
                m.get(position_url, content=f.read())
            with open(os.path.join(self.dir, "2_colleges.json"), "rb") as f:
                m.get(college_url, content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=32.603&longitude=-85.486&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FChicago&start_date=2023-09-14&end_date=2023-09-15&format=flatbuffers")
            player_model = create_espn_player_model(
                session=self._session,
                player={
                    "playerId": identifier,
                    "period": 0,
                    "active": False,
                    "starter": True,
                    "forPlayerId": 0,
                    "jersey": "4",
                    "valid": False,
                    "athlete": {
                        "$ref": athletes_url,
                    },
                    "position": {
                        "$ref": position_url,
                    },
                    "statistics": {
                        "$ref": statistics_url,
                    },
                    "didNotPlay": False,
                    "displayName": "J. Broome",
                    "ejected": False,
                },
                dt=dt,
                positions_validator={"F": "F"},
            )
            self.assertEqual(player_model.turnover_points, 0.0)

    def test_penalty_kill_percentage(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        identifier = "5767"
        statistics_url = "http://sports.core.api.espn.com/v2/sports/hockey/leagues/nhl/events/401685276/competitions/401685276/competitors/16/roster/5767/statistics/0?lang=en&region=us"
        athletes_url = "http://sports.core.api.espn.com/v2/sports/hockey/leagues/nhl/seasons/2025/athletes/5767?lang=en&region=us"
        position_url = "http://sports.core.api.espn.com/v2/sports/hockey/leagues/nhl/positions/3?lang=en&region=us"
        college_url = "http://sports.core.api.espn.com/v2/colleges/103?lang=en&region=us"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "0_statistics-6.json"), "rb") as f:
                m.get(statistics_url, content=f.read())
            with open(os.path.join(self.dir, "5767_athletes.json"), "rb") as f:
                m.get(athletes_url, content=f.read())
            with open(os.path.join(self.dir, "3_positions.json"), "rb") as f:
                m.get(position_url, content=f.read())
            with open(os.path.join(self.dir, "103_colleges.json"), "rb") as f:
                m.get(college_url, content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=42.335&longitude=-71.170278&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FNew_York&start_date=2023-09-14&end_date=2023-09-15&format=flatbuffers")
            player_model = create_espn_player_model(
                session=self._session,
                player={
                    "playerId": identifier,
                    "jersey": "13",
                    "athlete": {
                        "$ref": athletes_url,
                    },
                    "position": {
                        "$ref": position_url,
                    },
                    "statistics": {
                        "$ref": statistics_url,
                    },
                    "displayName": "K. Hayes",
                    "scratched": False,
                },
                dt=dt,
                positions_validator={"RW": "RW"},
            )
            self.assertEqual(player_model.penalty_kill_percentage, 0.0)

    def test_team_rebounds(self):
        dt = datetime.datetime(2023, 9, 15, 0, 15)
        identifier = "3142055"
        statistics_url = "http://sports.core.api.espn.com/v2/sports/basketball/leagues/wnba/events/401736120/competitions/401736120/competitors/3/roster/3142055/statistics/0?lang=en&region=us"
        athletes_url = "http://sports.core.api.espn.com/v2/sports/basketball/leagues/wnba/seasons/2025/athletes/3142055?lang=en&region=us"
        position_url = "http://sports.core.api.espn.com/v2/sports/basketball/leagues/wnba/positions/7?lang=en&region=us"
        college_url = "http://sports.core.api.espn.com/v2/colleges/97?lang=en&region=us"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "0_statistics-15.json"), "rb") as f:
                m.get(statistics_url, content=f.read())
            with open(os.path.join(self.dir, "3142055_athletes.json"), "rb") as f:
                m.get(athletes_url, content=f.read())
            with open(os.path.join(self.dir, "7_positions.json"), "rb") as f:
                m.get(position_url, content=f.read())
            with open(os.path.join(self.dir, "97_colleges.json"), "rb") as f:
                m.get(college_url, content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=38.256111&longitude=-85.751389&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FKentucky%2FLouisville&start_date=2023-09-14&end_date=2023-09-15&format=flatbuffers")
            player_model = create_espn_player_model(
                session=self._session,
                player={
                    "playerId": identifier,
                    "jersey": "13",
                    "athlete": {
                        "$ref": athletes_url,
                    },
                    "position": {
                        "$ref": position_url,
                    },
                    "statistics": {
                        "$ref": statistics_url,
                    },
                    "displayName": "K. Hayes",
                    "scratched": False,
                },
                dt=dt,
                positions_validator={"F": "F"},
            )
            self.assertEqual(player_model.team_rebounds, 0.0)
