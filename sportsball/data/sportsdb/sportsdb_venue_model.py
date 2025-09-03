"""SportsDB venue model."""

# pylint: disable=duplicate-code
import datetime

import pytest_is_running
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..google.google_address_model import create_google_address_model
from ..venue_model import VERSION, VenueModel


def _create_sportsdb_venue_model(
    session: ScrapeSession,
    venue_id: str,
    dt: datetime.datetime,
    version: str,
) -> VenueModel | None:
    if venue_id == "19533":
        venue_id = "17146"
    if venue_id == "21813":
        venue_id = "23848"
    if venue_id == "21642":
        venue_id = "29570"
    if venue_id == "23652":
        venue_id = "29569"
    if venue_id == "23654":
        venue_id = "15874"
    if venue_id == "23655":
        venue_id = "30856"
    if venue_id == "23656":
        venue_id = "29575"
    if venue_id == "23657":
        venue_id = "23720"
    response = session.get(
        f"https://www.thesportsdb.com/api/v1/json/3/lookupvenue.php?id={venue_id}"
    )
    response.raise_for_status()
    venues = response.json()["venues"]
    if venues is None:
        return None
    venue = venues[0]
    name = venue["strVenue"]

    address = create_google_address_model(
        " - ".join(
            [
                x
                for x in [
                    name,
                    venue["strLocation"],
                    venue["strCountry"],
                ]
                if x is not None and x
            ]
        ),
        session,
        dt,
    )

    return VenueModel(
        identifier=venue_id,
        name=name,
        address=address,  # pyright: ignore
        is_grass=None,
        is_indoor=None,
        is_turf=None,
        is_dirt=None,
        version=version,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_sportsdb_venue_model(
    session: ScrapeSession,
    venue_id: str,
    dt: datetime.datetime,
    version: str,
) -> VenueModel | None:
    return _create_sportsdb_venue_model(
        session=session, venue_id=venue_id, dt=dt, version=version
    )


def create_sportsdb_venue_model(
    session: ScrapeSession, venue_id: str, dt: datetime.datetime
) -> VenueModel | None:
    """Create sports DB venue model."""
    if not pytest_is_running.is_running() and dt < datetime.datetime.now().replace(
        tzinfo=dt.tzinfo
    ) - datetime.timedelta(days=7):
        return _cached_create_sportsdb_venue_model(
            session=session, venue_id=venue_id, dt=dt, version=VERSION
        )
    with session.cache_disabled():
        return _create_sportsdb_venue_model(
            session=session, venue_id=venue_id, dt=dt, version=VERSION
        )
