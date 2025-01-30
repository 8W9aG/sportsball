"""AFL AFLTables venue model."""

import datetime
import os
from urllib.parse import urlparse

import pytest_is_running
import requests_cache
from bs4 import BeautifulSoup

from ....cache import MEMORY
from ...google.google_address_model import create_google_address_model
from ...venue_model import VenueModel


def _create_afl_afltables_venue_model(
    url: str, session: requests_cache.CachedSession, dt: datetime.datetime
) -> VenueModel:
    o = urlparse(url)
    last_component = o.path.split("/")[-1]
    identifier, _ = os.path.splitext(last_component)
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    name = None
    for h1 in soup.find_all("h1"):
        name = h1.get_text()
    if name is None:
        raise ValueError("name is null.")
    address = create_google_address_model(f"{name} - Australia", session, dt)
    return VenueModel(
        identifier=identifier,
        name=name,
        address=address,  # pyright: ignore
        is_grass=None,
        is_indoor=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_afl_afltables_venue_model(
    url: str, session: requests_cache.CachedSession, dt: datetime.datetime
) -> VenueModel:
    return _create_afl_afltables_venue_model(url, session, dt)


def create_afl_afltables_venue_model(
    url: str, session: requests_cache.CachedSession, dt: datetime.datetime
) -> VenueModel:
    """Create a venue model from AFL tables."""
    if (
        not pytest_is_running.is_running()
        and dt < datetime.datetime.now() - datetime.timedelta(days=7)
    ):
        return _cached_create_afl_afltables_venue_model(url, session, dt)
    with session.cache_disabled():
        return _create_afl_afltables_venue_model(url, session, dt)
