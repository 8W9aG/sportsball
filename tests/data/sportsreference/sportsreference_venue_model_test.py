"""Tests for the sportsreference venue model class."""
import datetime
import os
import unittest

import requests_mock
from scrapesession.scrapesession import ScrapeSession
from sportsball.data.sportsreference.sportsreference_venue_model import create_sportsreference_venue_model


class TestSportsReferenceVenueModel(unittest.TestCase):

    def setUp(self):
        self.session = ScrapeSession(backend="memory")
        self.dir = os.path.dirname(__file__)

    def test_identifier(self):
        name = "Golden 1 Center - Sacramento, California - United States"
        with requests_mock.Mocker() as m:
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=38.580361&longitude=-121.499611&start_date=2010-10-09&end_date=2010-10-10&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FLos_Angeles&format=flatbuffers")
            venue_model = create_sportsreference_venue_model(
                name,
                self.session,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(venue_model.identifier, name)
