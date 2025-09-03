"""Tests for the sportsdb game model class."""
import datetime
import os
import unittest

import requests_mock
from scrapesession.scrapesession import ScrapeSession
from sportsball.data.sportsdb.sportsdb_game_model import create_sportsdb_game_model
from sportsball.data.league import League
from sportsball.data.season_type import SeasonType


class TestSportsDBVenueModel(unittest.TestCase):

    def setUp(self):
        self._session = ScrapeSession(backend="memory")
        self.dir = os.path.dirname(__file__)

    def test_identifier(self):
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "venue_16094.json"), "rb") as f:
                m.get("https://www.thesportsdb.com/api/v1/json/3/lookupvenue.php?id=16094", content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=39.9013695&longitude=-75.1700964&start_date=2023-09-14&end_date=2023-09-15&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FNew_York&format=flatbuffers")
            m.get("https://news.google.com/rss/search?q=%22Philadelphia+Eagles%22+%2B+%28sport+OR+nfl+OR+%22National+Football+League%22%29+after%3A2023-09-13+before%3A2023-09-14&ceid=US:en&hl=en&gl=US")
            m.get("https://news.google.com/rss/search?q=%22Minnesota+Vikings%22+%2B+%28sport+OR+nfl+OR+%22National+Football+League%22%29+after%3A2023-09-13+before%3A2023-09-14&ceid=US:en&hl=en&gl=US")
            game_model = create_sportsdb_game_model(
                self._session,
                {
                    "strTimestamp": "2023-09-15T00:15:00",
                    "idVenue": "16094",
                    "intHomeScore": "34",
                    "intAwayScore": "28",
                    "idHomeTeam": "134936",
                    "strHomeTeam": "Philadelphia Eagles",
                    "idAwayTeam": "134941",
                    "strAwayTeam": "Minnesota Vikings",
                },
                0,
                0,
                League.NFL,
                2019,
                SeasonType.REGULAR,
            )
            self.assertEqual(game_model.dt, datetime.datetime(2023, 9, 15, 0, 15))
