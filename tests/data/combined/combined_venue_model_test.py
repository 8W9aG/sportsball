"""Tests for the combined venue model class."""
import os
import unittest

import requests_mock
import requests_cache
from sportsball.data.combined.combined_venue_model import create_combined_venue_model
from sportsball.data.venue_model import VenueModel, VERSION


class TestCombinedVenueModel(unittest.TestCase):

    def setUp(self):
        self._session = requests_cache.CachedSession(backend="memory")
        self.dir = os.path.dirname(__file__)

    def test_is_turf(self):
        is_turf = True
        with requests_mock.Mocker() as m:
            venue_model = VenueModel(
                identifier="a",
                name="The Venue",
                address=None,
                is_grass=None,
                is_indoor=None,
                is_turf=is_turf,
                is_dirt=None,
                version=VERSION,
            )
            venue_model_2 = VenueModel(
                identifier="b",
                name="The Venue",
                address=None,
                is_grass=None,
                is_indoor=None,
                is_turf=None,
                is_dirt=None,
                version=VERSION,
            )
            combined_venue_model = create_combined_venue_model(
                [venue_model, venue_model_2],
                "a",
                self._session,
            )
            self.assertTrue(combined_venue_model.is_turf)
