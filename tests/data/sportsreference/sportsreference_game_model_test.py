"""Tests for the sportsreference game model class."""
import datetime
import os
import unittest

import requests_mock
import requests_cache
from sportsball.data.sportsreference.sportsreference_game_model import create_sportsreference_game_model
from sportsball.data.league import League


class TestSportsReferenceGameModel(unittest.TestCase):

    def setUp(self):
        self.session = requests_cache.CachedSession(backend="memory")
        self.dir = os.path.dirname(__file__)

    def test_dt(self):
        url = "https://www.basketball-reference.com/boxscores/202501230ATL.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "202501230ATL.html"), "rb") as f:
                m.get(url, content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=33.757222&longitude=-84.396389&start_date=2025-01-22&end_date=2025-01-23&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FNew_York&format=flatbuffers")
            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(2025, 1, 23, 19, 30))

    def test_dt_old_style(self):
        url = "http://www.basketball-reference.com/boxscores/201606190GSW.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "201606190GSW.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "2016.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/CLE/2016.html", content=f.read())
            with open(os.path.join(self.dir, "shumpim01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/shumpim01.html", content=f.read())
            with open(os.path.join(self.dir, "mcraejo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mcraejo01.html", content=f.read())
            with open(os.path.join(self.dir, "jefferi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/jefferi01.html", content=f.read())
            with open(os.path.join(self.dir, "varejan01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/v/varejan01.html", content=f.read())
            with open(os.path.join(self.dir, "loveke01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/loveke01.html", content=f.read())
            with open(os.path.join(self.dir, "thomptr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/thomptr01.html", content=f.read())
            with open(os.path.join(self.dir, "curryst01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/curryst01.html", content=f.read())
            with open(os.path.join(self.dir, "kaunsa01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/k/kaunsa01.html", content=f.read())
            with open(os.path.join(self.dir, "jamesle01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/jamesle01.html", content=f.read())
            with open(os.path.join(self.dir, "willima01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/willima01.html", content=f.read())
            with open(os.path.join(self.dir, "irvinky01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/i/irvinky01.html", content=f.read())
            with open(os.path.join(self.dir, "smithjr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/smithjr01.html", content=f.read())
            with open(os.path.join(self.dir, "GSW_2016.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/GSW/2016.html", content=f.read())
            with open(os.path.join(self.dir, "greendr01.html"), "rb") as f:
                m.get("https://www.basketball-reference.com/players/g/greendr01.html", content=f.read())
            with open(os.path.join(self.dir, "barbole01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/barbole01.html", content=f.read())
            with open(os.path.join(self.dir, "barneha02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/barneha02.html", content=f.read())
            with open(os.path.join(self.dir, "thompkl01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/thompkl01.html", content=f.read())
            with open(os.path.join(self.dir, "thompkl01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/thompkl01.html", content=f.read())
            with open(os.path.join(self.dir, "ezelife01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/e/ezelife01.html", content=f.read())
            with open(os.path.join(self.dir, "livinsh01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/livinsh01.html", content=f.read())
            with open(os.path.join(self.dir, "greendr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/g/greendr01.html", content=f.read())
            with open(os.path.join(self.dir, "bogutan01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/bogutan01.html", content=f.read())
            with open(os.path.join(self.dir, "looneke01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/looneke01.html", content=f.read())
            with open(os.path.join(self.dir, "speigma01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/speigma01.html", content=f.read())
            with open(os.path.join(self.dir, "iguodan01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/i/iguodan01.html", content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=37.750278&longitude=-122.203056&start_date=2016-06-18&end_date=2016-06-19&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FLos_Angeles&format=flatbuffers")
            
            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(2016, 6, 19, 20, 0))

    def test_dt_old_style_2(self):
        url = "http://www.basketball-reference.com/boxscores/201604160ATL.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "201604160ATL.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "BOS_2016.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/BOS/2016.html", content=f.read())
            with open(os.path.join(self.dir, "olynyke01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/o/olynyke01.html", content=f.read())
            with open(os.path.join(self.dir, "crowdja01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/crowdja01.html", content=f.read())
            with open(os.path.join(self.dir, "thomais02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/thomais02.html", content=f.read())
            with open(os.path.join(self.dir, "smartma01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/smartma01.html", content=f.read())
            with open(os.path.join(self.dir, "mickejo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mickejo01.html", content=f.read())
            with open(os.path.join(self.dir, "youngja01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/y/youngja01.html", content=f.read())
            with open(os.path.join(self.dir, "johnsam01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/johnsam01.html", content=f.read())
            with open(os.path.join(self.dir, "zellety01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/z/zellety01.html", content=f.read())
            with open(os.path.join(self.dir, "roziete01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/r/roziete01.html", content=f.read())
            with open(os.path.join(self.dir, "hunterj01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hunterj01.html", content=f.read())
            with open(os.path.join(self.dir, "turneev01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/turneev01.html", content=f.read())
            with open(os.path.join(self.dir, "hollajo02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hollajo02.html", content=f.read())
            with open(os.path.join(self.dir, "sullija01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/sullija01.html", content=f.read())
            with open(os.path.join(self.dir, "bradlav01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/bradlav01.html", content=f.read())
            with open(os.path.join(self.dir, "jerebjo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/jerebjo01.html", content=f.read())
            with open(os.path.join(self.dir, "ATL_2016.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/ATL/2016.html", content=f.read())
            with open(os.path.join(self.dir, "schrode01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/schrode01.html", content=f.read())
            with open(os.path.join(self.dir, "bazemke01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/bazemke01.html", content=f.read())
            with open(os.path.join(self.dir, "pattela01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/p/pattela01.html", content=f.read())
            with open(os.path.join(self.dir, "splitti01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/splitti01.html", content=f.read())
            with open(os.path.join(self.dir, "horfoal01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/horfoal01.html", content=f.read())
            with open(os.path.join(self.dir, "hardati02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hardati02.html", content=f.read())
            with open(os.path.join(self.dir, "millspa01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/millspa01.html", content=f.read())
            with open(os.path.join(self.dir, "scottmi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/scottmi01.html", content=f.read())
            with open(os.path.join(self.dir, "hinriki01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hinriki01.html", content=f.read())
            with open(os.path.join(self.dir, "muscami01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/muscami01.html", content=f.read())
            with open(os.path.join(self.dir, "korveky01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/k/korveky01.html", content=f.read())
            with open(os.path.join(self.dir, "tavarwa01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/tavarwa01.html", content=f.read())
            with open(os.path.join(self.dir, "teaguje01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/teaguje01.html", content=f.read())
            with open(os.path.join(self.dir, "sefolth01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/sefolth01.html", content=f.read())
            with open(os.path.join(self.dir, "humphkr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/humphkr01.html", content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=33.757222&longitude=-84.396389&start_date=2016-04-15&end_date=2016-04-16&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FNew_York&format=flatbuffers")
            
            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(2016, 4, 16, 19, 0))

    def test_dt_old_style_3(self):
        url = "http://www.basketball-reference.com/boxscores/201604130MIL.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "201604130MIL.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "IND_2016.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/IND/2016.html", content=f.read())
            with open(os.path.join(self.dir, "youngjo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/y/youngjo01.html", content=f.read())
            with open(os.path.join(self.dir, "allenla01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/allenla01.html", content=f.read())
            with open(os.path.join(self.dir, "robingl02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/r/robingl02.html", content=f.read())
            with open(os.path.join(self.dir, "hilljo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hilljo01.html", content=f.read())
            with open(os.path.join(self.dir, "ellismo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/e/ellismo01.html", content=f.read())
            with open(os.path.join(self.dir, "mahinia01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mahinia01.html", content=f.read())
            with open(os.path.join(self.dir, "milescj01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/milescj01.html", content=f.read())
            with open(os.path.join(self.dir, "stuckro01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/stuckro01.html", content=f.read())
            with open(os.path.join(self.dir, "chrisra01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/chrisra01.html", content=f.read())
            with open(os.path.join(self.dir, "antetgi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/antetgi01.html", content=f.read())
            with open(os.path.join(self.dir, "turnemy01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/turnemy01.html", content=f.read())
            with open(os.path.join(self.dir, "lawsoty01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/lawsoty01.html", content=f.read())
            with open(os.path.join(self.dir, "hillge01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hillge01.html", content=f.read())
            with open(os.path.join(self.dir, "whittsh01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/whittsh01.html", content=f.read())
            with open(os.path.join(self.dir, "georgpa01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/g/georgpa01.html", content=f.read())
            with open(os.path.join(self.dir, "hillso01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hillso01.html", content=f.read())
            with open(os.path.join(self.dir, "MIL_2016.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/MIL/2016.html", content=f.read())
            with open(os.path.join(self.dir, "novakst01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/n/novakst01.html", content=f.read())
            with open(os.path.join(self.dir, "plumlmi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/p/plumlmi01.html", content=f.read())
            with open(os.path.join(self.dir, "middlkh01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/middlkh01.html", content=f.read())
            with open(os.path.join(self.dir, "obryajo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/o/obryajo01.html", content=f.read())
            with open(os.path.join(self.dir, "cartemi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/cartemi01.html", content=f.read())
            with open(os.path.join(self.dir, "ennisty01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/e/ennisty01.html", content=f.read())
            with open(os.path.join(self.dir, "bayleje01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/bayleje01.html", content=f.read())
            with open(os.path.join(self.dir, "inglida01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/i/inglida01.html", content=f.read())
            with open(os.path.join(self.dir, "parkeja01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/p/parkeja01.html", content=f.read())
            with open(os.path.join(self.dir, "vasqugr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/v/vasqugr01.html", content=f.read())
            with open(os.path.join(self.dir, "mayooj01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mayooj01.html", content=f.read())
            with open(os.path.join(self.dir, "hensojo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hensojo01.html", content=f.read())
            with open(os.path.join(self.dir, "vaughra01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/v/vaughra01.html", content=f.read())
            with open(os.path.join(self.dir, "monrogr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/monrogr01.html", content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=33.757222&longitude=-84.396389&start_date=2016-04-15&end_date=2016-04-16&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FNew_York&format=flatbuffers")
            
            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(2016, 4, 13, 20, 0))

    def test_dt_old_style_4(self):
        url = "http://www.basketball-reference.com/boxscores/201210300CLE.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "201210300CLE.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "WAS_2013.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/WAS/2013.html", content=f.read())
            with open(os.path.join(self.dir, "crawfjo02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/crawfjo02.html", content=f.read())
            with open(os.path.join(self.dir, "okafoem01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/o/okafoem01.html", content=f.read())
            with open(os.path.join(self.dir, "webstma02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/webstma02.html", content=f.read())
            with open(os.path.join(self.dir, "booketr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/booketr01.html", content=f.read())
            with open(os.path.join(self.dir, "bealbr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/bealbr01.html", content=f.read())
            with open(os.path.join(self.dir, "veselja01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/v/veselja01.html", content=f.read())
            with open(os.path.join(self.dir, "singlch01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/singlch01.html", content=f.read())
            with open(os.path.join(self.dir, "pargoja01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/p/pargoja01.html", content=f.read())
            with open(os.path.join(self.dir, "arizatr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/arizatr01.html", content=f.read())
            with open(os.path.join(self.dir, "barroea01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/barroea01.html", content=f.read())
            with open(os.path.join(self.dir, "priceaj01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/p/priceaj01.html", content=f.read())
            with open(os.path.join(self.dir, "CLE_2013.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/CLE/2013.html", content=f.read())
            with open(os.path.join(self.dir, "milescj01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/milescj01.html", content=f.read())
            with open(os.path.join(self.dir, "gibsoda01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/g/gibsoda01.html", content=f.read())
            with open(os.path.join(self.dir, "waitedi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/waitedi01.html", content=f.read())
            with open(os.path.join(self.dir, "irvinky01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/i/irvinky01.html", content=f.read())
            with open(os.path.join(self.dir, "zellety01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/z/zellety01.html", content=f.read())
            with open(os.path.join(self.dir, "geeal01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/g/geeal01.html", content=f.read())
            with open(os.path.join(self.dir, "varejan01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/v/varejan01.html", content=f.read())
            with open(os.path.join(self.dir, "sloando01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/sloando01.html", content=f.read())
            with open(os.path.join(self.dir, "thomptr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/thomptr01.html", content=f.read())
            with open(os.path.join(self.dir, "waltolu01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/waltolu01.html", content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=41.496389&longitude=-81.688056&start_date=2012-10-29&end_date=2012-10-30&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=America%2FNew_York&format=flatbuffers")

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(2012, 10, 30, 0, 0))

    def test_dt_old_style_5(self):
        url = "http://www.basketball-reference.com/boxscores/201206210MIA.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "201206210MIA.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "OKC_2012.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/OKC/2012.html", content=f.read())
            with open(os.path.join(self.dir, "jamesle01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/jamesle01.html", content=f.read())
            with open(os.path.join(self.dir, "westbru01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/westbru01.html", content=f.read())
            with open(os.path.join(self.dir, "cookda02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/cookda02.html", content=f.read())
            with open(os.path.join(self.dir, "perkike01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/p/perkike01.html", content=f.read())
            with open(os.path.join(self.dir, "ibakase01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/i/ibakase01.html", content=f.read())
            with open(os.path.join(self.dir, "sefolth01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/sefolth01.html", content=f.read())
            with open(os.path.join(self.dir, "fishede01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/f/fishede01.html", content=f.read())
            with open(os.path.join(self.dir, "haywala01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/haywala01.html", content=f.read())
            with open(os.path.join(self.dir, "hardeja01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hardeja01.html", content=f.read())
            with open(os.path.join(self.dir, "collini01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/collini01.html", content=f.read())
            with open(os.path.join(self.dir, "aldrico01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/aldrico01.html", content=f.read())
            with open(os.path.join(self.dir, "duranke01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/d/duranke01.html", content=f.read())
            with open(os.path.join(self.dir, "iveyro01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/i/iveyro01.html", content=f.read())
            with open(os.path.join(self.dir, "MIA_2012.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/MIA/2012.html", content=f.read())
            with open(os.path.join(self.dir, "howarju01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/howarju01.html", content=f.read())
            with open(os.path.join(self.dir, "hasleud01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hasleud01.html", content=f.read())
            with open(os.path.join(self.dir, "battish01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/battish01.html", content=f.read())
            with open(os.path.join(self.dir, "millemi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/millemi01.html", content=f.read())
            with open(os.path.join(self.dir, "turiaro01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/turiaro01.html", content=f.read())
            with open(os.path.join(self.dir, "wadedw01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/wadedw01.html", content=f.read())
            with open(os.path.join(self.dir, "coleno01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/coleno01.html", content=f.read())
            with open(os.path.join(self.dir, "harrite01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/harrite01.html", content=f.read())
            with open(os.path.join(self.dir, "boshch01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/boshch01.html", content=f.read())
            with open(os.path.join(self.dir, "jonesja02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/jonesja02.html", content=f.read())
            with open(os.path.join(self.dir, "chalmma01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/chalmma01.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(2012, 6, 21, 0, 0))

    def test_dt_old_style_6(self):
        url = "http://www.basketball-reference.com/boxscores/201112260DAL.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "201112260DAL.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "DEN_2012.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/DEN/2012.html", content=f.read())
            with open(os.path.join(self.dir, "koufoko01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/k/koufoko01.html", content=f.read())
            with open(os.path.join(self.dir, "millean02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/millean02.html", content=f.read())
            with open(os.path.join(self.dir, "fernaru01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/f/fernaru01.html", content=f.read())
            with open(os.path.join(self.dir, "afflaar01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/afflaar01.html", content=f.read())
            with open(os.path.join(self.dir, "gallida01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/g/gallida01.html", content=f.read())
            with open(os.path.join(self.dir, "hilarne01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hilarne01.html", content=f.read())
            with open(os.path.join(self.dir, "lawsoty01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/lawsoty01.html", content=f.read())
            with open(os.path.join(self.dir, "harrial01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/harrial01.html", content=f.read())
            with open(os.path.join(self.dir, "anderch01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/anderch01.html", content=f.read())
            with open(os.path.join(self.dir, "breweco01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/breweco01.html", content=f.read())
            with open(os.path.join(self.dir, "mozgoti01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mozgoti01.html", content=f.read())
            with open(os.path.join(self.dir, "DAL_2012.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/DAL/2012.html", content=f.read())
            with open(os.path.join(self.dir, "westde01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/westde01.html", content=f.read())
            with open(os.path.join(self.dir, "beaubro01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/beaubro01.html", content=f.read())
            with open(os.path.join(self.dir, "kiddja01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/k/kiddja01.html", content=f.read())
            with open(os.path.join(self.dir, "willise01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/willise01.html", content=f.read())
            with open(os.path.join(self.dir, "haywobr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/haywobr01.html", content=f.read())
            with open(os.path.join(self.dir, "mahinia01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mahinia01.html", content=f.read())
            with open(os.path.join(self.dir, "cardibr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/cardibr01.html", content=f.read())
            with open(os.path.join(self.dir, "jonesdo02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/jonesdo02.html", content=f.read())
            with open(os.path.join(self.dir, "odomla01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/o/odomla01.html", content=f.read())
            with open(os.path.join(self.dir, "mariosh01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mariosh01.html", content=f.read())
            with open(os.path.join(self.dir, "cartevi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/cartevi01.html", content=f.read())
            with open(os.path.join(self.dir, "nowitdi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/n/nowitdi01.html", content=f.read())
            with open(os.path.join(self.dir, "terryja01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/terryja01.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(2011, 12, 26, 0, 0))

    def test_dt_old_style_7(self):
        url = "http://www.basketball-reference.com/boxscores/200310310LAC.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "200310310LAC.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "SEA_2004.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/SEA/2004.html", content=f.read())
            with open(os.path.join(self.dir, "frahmri01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/f/frahmri01.html", content=f.read())
            with open(os.path.join(self.dir, "boothca01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/boothca01.html", content=f.read())
            with open(os.path.join(self.dir, "evansre01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/e/evansre01.html", content=f.read())
            with open(os.path.join(self.dir, "murraro01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/murraro01.html", content=f.read())
            with open(os.path.join(self.dir, "sesayan01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/sesayan01.html", content=f.read())
            with open(os.path.join(self.dir, "radmavl01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/r/radmavl01.html", content=f.read())
            with open(os.path.join(self.dir, "lewisra02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/lewisra02.html", content=f.read())
            with open(os.path.join(self.dir, "jamesje01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/jamesje01.html", content=f.read())
            with open(os.path.join(self.dir, "ridnolu01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/r/ridnolu01.html", content=f.read())
            with open(os.path.join(self.dir, "barrybr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/barrybr01.html", content=f.read())
            with open(os.path.join(self.dir, "LAC_2004.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/LAC/2004.html", content=f.read())
            with open(os.path.join(self.dir, "richaqu01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/r/richaqu01.html", content=f.read())
            with open(os.path.join(self.dir, "zhizhwa01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/z/zhizhwa01.html", content=f.read())
            with open(os.path.join(self.dir, "doolike01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/d/doolike01.html", content=f.read())
            with open(os.path.join(self.dir, "kamanch01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/k/kamanch01.html", content=f.read())
            with open(os.path.join(self.dir, "elyme01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/e/elyme01.html", content=f.read())
            with open(os.path.join(self.dir, "drobnpr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/d/drobnpr01.html", content=f.read())
            with open(os.path.join(self.dir, "maggeco01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/maggeco01.html", content=f.read())
            with open(os.path.join(self.dir, "simmobo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/simmobo01.html", content=f.read())
            with open(os.path.join(self.dir, "jaricma01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/jaricma01.html", content=f.read())
            with open(os.path.join(self.dir, "houseed01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/houseed01.html", content=f.read())
            with open(os.path.join(self.dir, "wilcoch01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/wilcoch01.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(2003, 10, 31, 19, 0))

    def test_dt_old_style_8(self):
        url = "http://www.basketball-reference.com/boxscores/198304270BOS.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "198304270BOS.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "MIL_1983.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/MIL/1983.html", content=f.read())
            with open(os.path.join(self.dir, "bridgju01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/bridgju01.html", content=f.read())
            with open(os.path.join(self.dir, "listeal01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/listeal01.html", content=f.read())
            with open(os.path.join(self.dir, "catchha01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/catchha01.html", content=f.read())
            with open(os.path.join(self.dir, "presspa01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/p/presspa01.html", content=f.read())
            with open(os.path.join(self.dir, "crissch01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/crissch01.html", content=f.read())
            with open(os.path.join(self.dir, "mokespa01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mokespa01.html", content=f.read())
            with open(os.path.join(self.dir, "wintebr01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/wintebr01.html", content=f.read())
            with open(os.path.join(self.dir, "laniebo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/laniebo01.html", content=f.read())
            with open(os.path.join(self.dir, "fordph01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/f/fordph01.html", content=f.read())
            with open(os.path.join(self.dir, "johnsma01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/johnsma01.html", content=f.read())
            with open(os.path.join(self.dir, "moncrsi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/moncrsi01.html", content=f.read())
            with open(os.path.join(self.dir, "BOS_1983.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/BOS/1983.html", content=f.read())
            with open(os.path.join(self.dir, "carrml01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/carrml01.html", content=f.read())
            with open(os.path.join(self.dir, "parisro01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/p/parisro01.html", content=f.read())
            with open(os.path.join(self.dir, "mchalke01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mchalke01.html", content=f.read())
            with open(os.path.join(self.dir, "birdla01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/birdla01.html", content=f.read())
            with open(os.path.join(self.dir, "maxwece01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/maxwece01.html", content=f.read())
            with open(os.path.join(self.dir, "bucknqu01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/bucknqu01.html", content=f.read())
            with open(os.path.join(self.dir, "hendege01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/h/hendege01.html", content=f.read())
            with open(os.path.join(self.dir, "architi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/architi01.html", content=f.read())
            with open(os.path.join(self.dir, "wedmasc01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/wedmasc01.html", content=f.read())
            with open(os.path.join(self.dir, "aingeda01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/aingeda01.html", content=f.read())
            with open(os.path.join(self.dir, "bradlch01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/bradlch01.html", content=f.read())
            with open(os.path.join(self.dir, "robeyri01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/r/robeyri01.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(1983, 4, 27, 0, 0))

    def test_dt_old_style_9(self):
        url = "http://www.basketball-reference.com/boxscores/197504230KCO.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "197504230KCO.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "CHI_1975.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/CHI/1975.html", content=f.read())
            with open(os.path.join(self.dir, "garrero01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/g/garrero01.html", content=f.read())
            with open(os.path.join(self.dir, "wilsobo03.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/wilsobo03.html", content=f.read())
            with open(os.path.join(self.dir, "thurmna01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/t/thurmna01.html", content=f.read())
            with open(os.path.join(self.dir, "guokama02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/g/guokama02.html", content=f.read())
            with open(os.path.join(self.dir, "boerwto01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/boerwto01.html", content=f.read())
            with open(os.path.join(self.dir, "adelmri01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/adelmri01.html", content=f.read())
            with open(os.path.join(self.dir, "lovebo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/lovebo01.html", content=f.read())
            with open(os.path.join(self.dir, "sloanje01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/sloanje01.html", content=f.read())
            with open(os.path.join(self.dir, "vanlino01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/v/vanlino01.html", content=f.read())
            with open(os.path.join(self.dir, "walkech01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/walkech01.html", content=f.read())
            with open(os.path.join(self.dir, "KCO_1975.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/KCO/1975.html", content=f.read())
            with open(os.path.join(self.dir, "walkeji01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/walkeji01.html", content=f.read())
            with open(os.path.join(self.dir, "architi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/architi01.html", content=f.read())
            with open(os.path.join(self.dir, "wedmasc01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/wedmasc01.html", content=f.read())
            with open(os.path.join(self.dir, "behagro01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/behagro01.html", content=f.read())
            with open(os.path.join(self.dir, "laceysa01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/laceysa01.html", content=f.read())
            with open(os.path.join(self.dir, "dantomi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/d/dantomi01.html", content=f.read())
            with open(os.path.join(self.dir, "kosmale01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/k/kosmale01.html", content=f.read())
            with open(os.path.join(self.dir, "johnsol01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/johnsol01.html", content=f.read())
            with open(os.path.join(self.dir, "mcneila01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mcneila01.html", content=f.read())
            with open(os.path.join(self.dir, "kojisdo01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/k/kojisdo01.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(1975, 4, 23, 0, 0))

    def test_dt_old_style_10(self):
        url = "http://www.basketball-reference.com/boxscores/197504060KCO.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "197504060KCO.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "CLE_1975.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/CLE/1975.html", content=f.read())
            with open(os.path.join(self.dir, "pattest01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/p/pattest01.html", content=f.read())
            with open(os.path.join(self.dir, "cleamji01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/cleamji01.html", content=f.read())
            with open(os.path.join(self.dir, "breweji01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/breweji01.html", content=f.read())
            with open(os.path.join(self.dir, "smithbi02.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/smithbi02.html", content=f.read())
            with open(os.path.join(self.dir, "snydedi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/s/snydedi01.html", content=f.read())
            with open(os.path.join(self.dir, "choneji01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/c/choneji01.html", content=f.read())
            with open(os.path.join(self.dir, "KCO_1975.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/KCO/1975.html", content=f.read())
            with open(os.path.join(self.dir, "architi01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/architi01.html", content=f.read())
            with open(os.path.join(self.dir, "wedmasc01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/wedmasc01.html", content=f.read())
            with open(os.path.join(self.dir, "behagro01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/b/behagro01.html", content=f.read())
            with open(os.path.join(self.dir, "mcneila01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/m/mcneila01.html", content=f.read())
            with open(os.path.join(self.dir, "walkeji01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/w/walkeji01.html", content=f.read())
            with open(os.path.join(self.dir, "laceysa01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/l/laceysa01.html", content=f.read())
            with open(os.path.join(self.dir, "adelmri01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/a/adelmri01.html", content=f.read())
            with open(os.path.join(self.dir, "johnsol01.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/players/j/johnsol01.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(1975, 4, 6, 0, 0))

    def test_dt_old_style_11(self):
        url = "http://www.basketball-reference.com/boxscores/196805040PTP.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "196805040PTP.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "NOB_1968.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/NOB/1968.html", content=f.read())
            with open(os.path.join(self.dir, "PTP_1968.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/PTP/1968.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(1968, 5, 4, 0, 0))

    def test_dt_old_style_12(self):
        url = "http://www.basketball-reference.com/boxscores/196803260NOB.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "196803260NOB.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "DNR_1968.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/DNR/1968.html", content=f.read())
            with open(os.path.join(self.dir, "NOB_1968.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/NOB/1968.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(1968, 3, 26, 0, 0))

    def test_dt_old_style_13(self):
        url = "http://www.basketball-reference.com/boxscores/196803180ANA.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "196803180ANA.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "PTP_1968.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/PTP/1968.html", content=f.read())
            with open(os.path.join(self.dir, "ANA_1968.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/ANA/1968.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(1968, 3, 18, 0, 0))

    def test_dt_old_style_14(self):
        url = "http://www.basketball-reference.com/boxscores/196710170DNR.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "196710170DNR.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "HSM_1968.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/HSM/1968.html", content=f.read())
            with open(os.path.join(self.dir, "DNR_1968.html"), "rb") as f:
                m.get("http://www.basketball-reference.com/teams/DNR/1968.html", content=f.read())

            game_model = create_sportsreference_game_model(
                self.session,
                url,
                League.NBA,
                datetime.datetime(2010, 10, 10, 10, 10, 0),
            )
            self.assertEqual(game_model.dt, datetime.datetime(1967, 10, 17, 0, 0))
