"""HKJC HKJC venue model."""

# pylint: disable=too-many-arguments
import datetime

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....cache import MEMORY
from ...google.google_address_model import create_google_address_model
from ...venue_model import VenueModel

SHA_TIN_VENUE_CODE = "ST"
HAPPY_VALLEY_VENUE_CODE = "HV"

ADDRESSES = {
    SHA_TIN_VENUE_CODE: "Sha Tin, China",
    HAPPY_VALLEY_VENUE_CODE: "Hally Valley, China",
}


@MEMORY.cache(ignore=["session"])
def create_hkjc_hkjc_venue_model(
    session: ScrapeSession,
    dt: datetime.datetime,
    venue_code: str,
    race_track: str,
    version: str,
) -> VenueModel:
    """Create a venue model from an HKJC result."""
    address = create_google_address_model(
        ADDRESSES[venue_code],
        session,
        dt,
    )
    name = ", ".join([race_track, venue_code])
    return VenueModel(
        identifier=name,
        name=name,
        address=address,  # pyright: ignore
        is_grass=None,
        is_indoor=None,
        is_turf=race_track.lower() == "turf",
        is_dirt=race_track.lower() == "dirt",
        version=version,
    )
