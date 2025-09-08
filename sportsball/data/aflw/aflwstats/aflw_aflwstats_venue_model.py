"""AFLW AFLWStats venue model."""

# pylint: disable=duplicate-code
import datetime

import pytest_is_running
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....cache import MEMORY
from ...google.google_address_model import create_google_address_model
from ...venue_model import VERSION, VenueModel


def _create_aflw_aflwstats_venue_model(
    name: str,
    session: ScrapeSession,
    dt: datetime.datetime,
    version: str,
) -> VenueModel:
    return VenueModel(
        identifier=name,
        name=name,
        address=create_google_address_model(name, session, dt),
        is_grass=None,
        is_indoor=None,
        is_turf=None,
        is_dirt=None,
        version=version,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_aflw_aflwstats_venue_model(
    name: str, session: ScrapeSession, dt: datetime.datetime, version: str
) -> VenueModel:
    return _create_aflw_aflwstats_venue_model(
        name=name, session=session, dt=dt, version=version
    )


def create_aflw_aflwstats_venue_model(
    name: str, session: ScrapeSession, dt: datetime.datetime
) -> VenueModel:
    """Create a venue model from AFLW AFLWStats."""
    if not pytest_is_running.is_running():
        return _cached_create_aflw_aflwstats_venue_model(
            name=name, session=session, dt=dt, version=VERSION
        )
    with session.cache_disabled():
        return _create_aflw_aflwstats_venue_model(
            name=name, session=session, dt=dt, version=VERSION
        )
