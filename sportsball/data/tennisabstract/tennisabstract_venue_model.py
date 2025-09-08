"""TennisAbstract venue model."""

import datetime

import pytest_is_running
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..google.google_address_model import create_google_address_model
from ..venue_model import VERSION, VenueModel


def _create_tennisabstract_venue_model(
    grounds: str,
    session: ScrapeSession,
    dt: datetime.datetime,
    version: str,
) -> VenueModel:
    address_model = create_google_address_model(grounds, session, dt)
    return VenueModel(
        identifier=grounds,
        name=grounds,
        address=address_model,
        is_grass=None,
        is_indoor=None,
        is_turf=None,
        is_dirt=None,
        version=version,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_tennisabstract_venue_model(
    grounds: str,
    session: ScrapeSession,
    dt: datetime.datetime,
    version: str,
) -> VenueModel:
    return _create_tennisabstract_venue_model(
        grounds=grounds, session=session, dt=dt, version=version
    )


def create_tennisabstract_venue_model(
    grounds: str,
    session: ScrapeSession,
    dt: datetime.datetime,
) -> VenueModel:
    """Create a TennisAbstract venue model."""
    if not pytest_is_running.is_running():
        return _cached_create_tennisabstract_venue_model(
            grounds=grounds, session=session, dt=dt, version=VERSION
        )
    with session.cache_disabled():
        return _create_tennisabstract_venue_model(
            grounds=grounds, session=session, dt=dt, version=VERSION
        )
