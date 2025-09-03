"""Tests for the afltables game model class."""
import unittest
import os
import datetime

from scrapesession.scrapesession import ScrapeSession
import requests_mock
from sportsball.data.afl.afltables.afl_afltables_game_model import create_afl_afltables_game_model
from sportsball.data.league import League


class TestAFLTablesGameModel(unittest.TestCase):

    def setUp(self):
        self._session = ScrapeSession(backend="memory")
        self.dir = os.path.dirname(__file__)

    def test_player_identifier(self):
        url = "https://afltables.com/afl/stats/games/2025/081820250330.html"
        with requests_mock.Mocker() as m:
            with open(os.path.join(self.dir, "081820250330.html"), "rb") as f:
                m.get(url, content=f.read())
            with open(os.path.join(self.dir, "perth.html"), "rb") as f:
                m.get("https://afltables.com/afl/venues/perth.html", content=f.read())
            with open(os.path.join(self.dir, "westcoast_idx.html"), "rb") as f:
                m.get("https://afltables.com/afl/teams/westcoast_idx.html", content=f.read())
            with open(os.path.join(self.dir, "fremantle_idx.html"), "rb") as f:
                m.get("https://afltables.com/afl/teams/fremantle_idx.html", content=f.read())
            with open(os.path.join(self.dir, "Oscar_Allen.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/O/Oscar_Allen.html", content=f.read())
            with open(os.path.join(self.dir, "Liam_Baker.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/L/Liam_Baker.html", content=f.read())
            with open(os.path.join(self.dir, "Tyler_Brockman.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/T/Tyler_Brockman.html", content=f.read())
            with open(os.path.join(self.dir, "Tom_Cole.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/T/Tom_Cole.html", content=f.read())
            with open(os.path.join(self.dir, "Jamie_Cripps.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Jamie_Cripps.html", content=f.read())
            with open(os.path.join(self.dir, "Tyrell_Dewar.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/T/Tyrell_Dewar.html", content=f.read())
            with open(os.path.join(self.dir, "Liam_Duggan.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/L/Liam_Duggan.html", content=f.read())
            with open(os.path.join(self.dir, "Harry_Edwards.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/H/Harry_Edwards.html", content=f.read())
            with open(os.path.join(self.dir, "Reuben_Ginbey.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/R/Reuben_Ginbey.html", content=f.read())
            with open(os.path.join(self.dir, "Jack_Graham.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Jack_Graham.html", content=f.read())
            with open(os.path.join(self.dir, "Elijah_Hewett.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/E/Elijah_Hewett.html", content=f.read())
            with open(os.path.join(self.dir, "Brady_Hough.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/B/Brady_Hough.html", content=f.read())
            with open(os.path.join(self.dir, "Jayden_Hunt.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Jayden_Hunt.html", content=f.read())
            with open(os.path.join(self.dir, "Tim_Kelly.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/T/Tim_Kelly.html", content=f.read())
            with open(os.path.join(self.dir, "Noah_Long.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/N/Noah_Long.html", content=f.read())
            with open(os.path.join(self.dir, "Ryan_Maric.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/R/Ryan_Maric.html", content=f.read())
            with open(os.path.join(self.dir, "Jeremy_McGovern.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Jeremy_McGovern.html", content=f.read())
            with open(os.path.join(self.dir, "Matthew_Owies.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/M/Matthew_Owies.html", content=f.read())
            with open(os.path.join(self.dir, "Archer_Reid.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/A/Archer_Reid.html", content=f.read())
            with open(os.path.join(self.dir, "Harley_Reid.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/H/Harley_Reid.html", content=f.read())
            with open(os.path.join(self.dir, "Liam_Ryan.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/L/Liam_Ryan.html", content=f.read())
            with open(os.path.join(self.dir, "Bailey_Williams1.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/B/Bailey_Williams1.html", content=f.read())
            with open(os.path.join(self.dir, "Jack_Williams.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Jack_Williams.html", content=f.read())
            with open(os.path.join(self.dir, "James_Aish.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/James_Aish.html", content=f.read())
            with open(os.path.join(self.dir, "Jye_Amiss.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Jye_Amiss.html", content=f.read())
            with open(os.path.join(self.dir, "Bailey_Banfield.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/B/Bailey_Banfield.html", content=f.read())
            with open(os.path.join(self.dir, "Shai_Bolton.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/S/Shai_Bolton.html", content=f.read())
            with open(os.path.join(self.dir, "Andrew_Brayshaw.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/A/Andrew_Brayshaw.html", content=f.read())
            with open(os.path.join(self.dir, "Heath_Chapman.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/H/Heath_Chapman.html", content=f.read())
            with open(os.path.join(self.dir, "Jordan_Clark.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Jordan_Clark.html", content=f.read())
            with open(os.path.join(self.dir, "Brennan_Cox.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/B/Brennan_Cox.html", content=f.read())
            with open(os.path.join(self.dir, "Josh_Draper.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Josh_Draper.html", content=f.read())
            with open(os.path.join(self.dir, "Isaiah_Dudley.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/I/Isaiah_Dudley.html", content=f.read())
            with open(os.path.join(self.dir, "Neil_Erasmus.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/N/Neil_Erasmus.html", content=f.read())
            with open(os.path.join(self.dir, "Michael_Frederick.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/M/Michael_Frederick.html", content=f.read())
            with open(os.path.join(self.dir, "Luke_Jackson.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/L/Luke_Jackson.html", content=f.read())
            with open(os.path.join(self.dir, "Matthew_Johnson.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/M/Matthew_Johnson.html", content=f.read())
            with open(os.path.join(self.dir, "Nathan_ODriscoll.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/N/Nathan_ODriscoll.html", content=f.read())
            with open(os.path.join(self.dir, "Alex_Pearce.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/A/Alex_Pearce.html", content=f.read())
            with open(os.path.join(self.dir, "Murphy_Reid.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/M/Murphy_Reid.html", content=f.read())
            with open(os.path.join(self.dir, "Luke_Ryan.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/L/Luke_Ryan.html", content=f.read())
            with open(os.path.join(self.dir, "Caleb_Serong.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/C/Caleb_Serong.html", content=f.read())
            with open(os.path.join(self.dir, "Jeremy_Sharp.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Jeremy_Sharp.html", content=f.read())
            with open(os.path.join(self.dir, "Josh_Treacy.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/J/Josh_Treacy.html", content=f.read())
            with open(os.path.join(self.dir, "Patrick_Voss.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/P/Patrick_Voss.html", content=f.read())
            with open(os.path.join(self.dir, "Karl_Worner.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/players/K/Karl_Worner.html", content=f.read())
            with open(os.path.join(self.dir, "coaches_westcoast.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/coaches/westcoast.html", content=f.read())
            with open(os.path.join(self.dir, "coaches_fremantle.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/coaches/fremantle.html", content=f.read())
            with open(os.path.join(self.dir, "John_Worsfold.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/coaches/John_Worsfold.html", content=f.read())
            with open(os.path.join(self.dir, "Ross_Lyon.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/coaches/Ross_Lyon.html", content=f.read())
            with open(os.path.join(self.dir, "Andrew_McQualter.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/coaches/Andrew_McQualter.html", content=f.read())
            with open(os.path.join(self.dir, "Justin_Longmuir.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/coaches/Justin_Longmuir.html", content=f.read())
            with open(os.path.join(self.dir, "Daniel_Johanson.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/umpires/Daniel_Johanson.html", content=f.read())
            with open(os.path.join(self.dir, "Jeff_Dalgleish.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/umpires/Jeff_Dalgleish.html", content=f.read())
            with open(os.path.join(self.dir, "Simon_Meredith.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/umpires/Simon_Meredith.html", content=f.read())
            with open(os.path.join(self.dir, "Nathan_Toner.html"), "rb") as f:
                m.get("https://afltables.com/afl/stats/umpires/Nathan_Toner.html", content=f.read())
            m.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-31.9511597&longitude=115.884175&start_date=2025-03-29&end_date=2025-03-30&hourly=temperature_2m&hourly=relative_humidity_2m&hourly=dew_point_2m&hourly=apparent_temperature&hourly=precipitation&hourly=rain&hourly=snowfall&hourly=snow_depth&hourly=weather_code&hourly=pressure_msl&hourly=surface_pressure&hourly=cloud_cover&hourly=cloud_cover_low&hourly=cloud_cover_mid&hourly=cloud_cover_high&hourly=et0_fao_evapotranspiration&hourly=vapour_pressure_deficit&hourly=wind_speed_10m&hourly=wind_speed_100m&hourly=wind_direction_10m&hourly=wind_direction_100m&hourly=wind_gusts_10m&hourly=soil_temperature_0_to_7cm&hourly=soil_temperature_7_to_28cm&hourly=soil_temperature_28_to_100cm&hourly=soil_temperature_100_to_255cm&hourly=soil_moisture_0_to_7cm&hourly=soil_moisture_7_to_28cm&hourly=soil_moisture_28_to_100cm&hourly=soil_moisture_100_to_255cm&daily=weather_code&daily=temperature_2m_max&daily=temperature_2m_min&daily=temperature_2m_mean&daily=apparent_temperature_max&daily=apparent_temperature_min&daily=apparent_temperature_mean&daily=sunrise&daily=sunset&daily=daylight_duration&daily=sunshine_duration&daily=precipitation_sum&daily=rain_sum&daily=snowfall_sum&daily=precipitation_hours&daily=wind_speed_10m_max&daily=wind_gusts_10m_max&daily=wind_direction_10m_dominant&daily=shortwave_radiation_sum&daily=et0_fao_evapotranspiration&timezone=Australia%2FPerth&format=flatbuffers")

            game_model = create_afl_afltables_game_model(
                0,
                self._session,
                url,
                2,
                {},
                League.AFL,
                season_year=2025,
                season_type=None,
            )
            self.assertIsNotNone(game_model.teams[0].players[0].identifier)
            self.assertEqual(game_model.dt, datetime.datetime(2025, 3, 30, 15, 10))
