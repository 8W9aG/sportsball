"""Venue model from wikipedia information."""

# pylint: disable=duplicate-code
import logging

import requests
import wikipediaapi  # type: ignore

from ... import __VERSION__
from ...cache import MEMORY
from ..google.google_address_model import get_venue_db
from ..venue_model import VenueModel


@MEMORY.cache(ignore=["session"])
def create_wikipedia_venue_model(
    session: requests.Session, latitude: float, longitude: float, version: str
) -> VenueModel | None:
    """Create a venue model by looking up the venue on wikipedia."""
    wiki_wiki = wikipediaapi.Wikipedia(user_agent=f"sportsball ({__VERSION__})")
    wiki_wiki._session = session

    venue_db = get_venue_db()
    for venue in venue_db["venues"].values():
        if venue["lat"] == latitude and venue["lng"] == longitude:
            if "wiki" not in venue:
                logging.warning("wiki not found for %f, %f", latitude, longitude)
            else:
                wikipage = venue["wiki"]
                if wikipage is not None:
                    page_py = wiki_wiki.page(wikipage)
                    return VenueModel(
                        identifier=wikipage,
                        name=page_py.title,
                        address=None,
                        is_grass=None,
                        is_indoor=None,
                        is_turf=None,
                        is_dirt=None,
                        is_hard=None,
                        version=version,
                    )
            break
    return None
