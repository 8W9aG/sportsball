"""Tests for the google address model class."""
import datetime
import unittest

from scrapesession.scrapesession import ScrapeSession
from sportsball.data.google.google_address_model import create_google_address_model


class TestGoogleAddressModel(unittest.TestCase):

    def setUp(self):
        self.session = ScrapeSession(backend="memory")

    def test_city(self):
        dt = datetime.datetime(2010, 10, 10, 10, 10, 00)
        address_model = create_google_address_model("Imperial Arena at Atlantis Resort, Nassau", self.session, dt)
        self.assertEqual(address_model.city, "Nassau")
