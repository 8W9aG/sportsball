"""Tennisdata venue model."""

# pylint: disable=duplicate-code
import datetime

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..google.google_address_model import create_google_address_model
from ..venue_model import VenueModel


@MEMORY.cache(ignore=["session"])
def create_tennisdata_venue_model(
    venue: str,
    session: ScrapeSession,
    dt: datetime.datetime,
    court: str,
    surface: str,
    version: str,
) -> VenueModel:
    """Create a venue model based off tennisdata."""
    address_model = create_google_address_model(venue, session, dt)
    return VenueModel(
        identifier=venue,
        name=venue,
        address=address_model,
        is_grass=None,
        is_indoor=court == "Outdoor",
        is_turf=surface == "Grass",
        is_dirt=surface == "Clay",
        is_hard=surface == "Hard",
        version=version,
    )
