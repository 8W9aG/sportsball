"""Odds Portal venue model."""

# pylint: disable=duplicate-code,too-many-arguments
import datetime

import pytest_is_running
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..google.google_address_model import create_google_address_model
from ..venue_model import VERSION, VenueModel


def _create_oddsportal_venue_model(
    session: ScrapeSession,
    dt: datetime.datetime,
    venue: str,
    venue_town: str,
    venue_country: str,
    version: str,
) -> VenueModel | None:
    return VenueModel(
        identifier=venue,
        name=venue,
        address=create_google_address_model(
            query=", ".join([venue, venue_town, venue_country]), session=session, dt=dt
        ),
        is_grass=None,
        is_indoor=None,
        is_turf=None,
        is_dirt=None,
        version=version,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_oddsportal_venue_model(
    session: ScrapeSession,
    dt: datetime.datetime,
    venue: str,
    venue_town: str,
    venue_country: str,
    version: str,
) -> VenueModel | None:
    return _create_oddsportal_venue_model(
        session=session,
        dt=dt,
        venue=venue,
        venue_town=venue_town,
        venue_country=venue_country,
        version=version,
    )


def create_oddsportal_venue_model(
    session: ScrapeSession,
    dt: datetime.datetime,
    venue: str,
    venue_town: str,
    venue_country: str,
) -> VenueModel | None:
    """Create odds portal venue model."""
    if not pytest_is_running.is_running() and dt < datetime.datetime.now().replace(
        tzinfo=dt.tzinfo
    ) - datetime.timedelta(days=7):
        return _cached_create_oddsportal_venue_model(
            session=session,
            dt=dt,
            venue=venue,
            venue_town=venue_town,
            venue_country=venue_country,
            version=VERSION,
        )
    with session.cache_disabled():
        return _create_oddsportal_venue_model(
            session=session,
            dt=dt,
            venue=venue,
            venue_town=venue_town,
            venue_country=venue_country,
            version=VERSION,
        )
