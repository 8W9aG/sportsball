"""WNBA WNBA.com venue model."""

import datetime

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...google.google_address_model import create_google_address_model
from ...venue_model import VenueModel


def create_wnba_wnbacom_venue_model(
    venue_name: str,
    session: ScrapeSession,
    dt: datetime.datetime,
    version: str,
) -> VenueModel:
    """Create a venue model from WNBA.com."""
    address_model = create_google_address_model(venue_name, session, dt)
    return VenueModel(
        identifier=venue_name,
        name=venue_name,
        address=address_model,
        is_grass=None,
        is_indoor=None,
        is_turf=None,
        is_dirt=None,
        is_hard=None,
        version=version,
    )
