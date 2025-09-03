"""ESPNCricInfo venue model."""

# pylint: disable=duplicate-code
import datetime
from typing import Any

import pytest_is_running
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....cache import MEMORY
from ...google.google_address_model import create_google_address_model
from ...venue_model import VERSION, VenueModel


def _create_espncricinfo_venue_model(
    grounds: dict[str, Any],
    session: ScrapeSession,
    dt: datetime.datetime,
    version: str,
) -> VenueModel:
    venue_name = grounds["name"]
    address_model = create_google_address_model(venue_name, session, dt)
    return VenueModel(
        identifier=str(grounds["id"]),
        name=venue_name,
        address=address_model,
        is_grass=None,
        is_indoor=None,
        is_turf=None,
        is_dirt=None,
        version=version,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_espncricinfo_venue_model(
    grounds: dict[str, Any],
    session: ScrapeSession,
    dt: datetime.datetime,
    version: str,
) -> VenueModel:
    return _create_espncricinfo_venue_model(
        grounds=grounds, session=session, dt=dt, version=version
    )


def create_espncricinfo_venue_model(
    grounds: dict[str, Any],
    session: ScrapeSession,
    dt: datetime.datetime,
) -> VenueModel:
    """Create a sports reference venue model."""
    if not pytest_is_running.is_running():
        return _cached_create_espncricinfo_venue_model(
            grounds=grounds, session=session, dt=dt, version=VERSION
        )
    with session.cache_disabled():
        return _create_espncricinfo_venue_model(
            grounds=grounds, session=session, dt=dt, version=VERSION
        )
