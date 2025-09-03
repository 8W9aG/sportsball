"""Sports Reference venue model."""

# pylint: disable=duplicate-code
import datetime

import pytest_is_running
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..google.google_address_model import create_google_address_model
from ..venue_model import VERSION, VenueModel


def _create_sportsreference_venue_model(
    venue_name: str | None,
    session: ScrapeSession,
    dt: datetime.datetime | None,
    version: str,
) -> VenueModel | None:
    if not venue_name:
        return None
    address_model = create_google_address_model(venue_name, session, dt)
    return VenueModel(
        identifier=venue_name,
        name=venue_name,
        address=address_model,
        is_grass=None,
        is_indoor=None,
        is_turf=None,
        is_dirt=None,
        version=version,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_sportsreference_venue_model(
    venue_name: str | None,
    session: ScrapeSession,
    dt: datetime.datetime | None,
    version: str,
) -> VenueModel | None:
    return _create_sportsreference_venue_model(
        venue_name=venue_name, session=session, dt=dt, version=version
    )


def create_sportsreference_venue_model(
    venue_name: str | None,
    session: ScrapeSession,
    dt: datetime.datetime | None,
) -> VenueModel | None:
    """Create a sports reference venue model."""
    if not pytest_is_running.is_running():
        return _cached_create_sportsreference_venue_model(
            venue_name=venue_name, session=session, dt=dt, version=VERSION
        )
    with session.cache_disabled():
        return _create_sportsreference_venue_model(
            venue_name=venue_name, session=session, dt=dt, version=VERSION
        )
