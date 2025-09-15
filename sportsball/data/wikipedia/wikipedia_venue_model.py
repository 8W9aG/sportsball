"""Venue model from wikipedia information."""

# pylint: disable=duplicate-code
import logging

import requests
import wikipediaapi  # type: ignore

from ... import __VERSION__
from ...cache import MEMORY
from ..venue_model import VenueModel

THE_GABBA = "The_Gabba"
SYDNEY_CRICKET_GROUND = "Sydney_Cricket_Ground"
STADIUM_AUSTRALIA = "Stadium_Australia"
YORK_PARK = "York_Park"
TRAEGER_PARK = "Traeger_Park"

WIKIPEDIA_VENUE_ID_MAP: dict[str, str | None] = {
    # AFLTables
    "brunswick_st": "Brunswick_Street_Oval",
    "victoria_park": "Victoria_Park,_Melbourne",
    "corio_oval": "Corio_Oval",
    "east_melbourne": "East_Melbourne_Cricket_Ground",
    "junction_oval": "Junction_Oval",
    "mcg": "Melbourne_Cricket_Ground",
    "princes_park": "Princes_Park_(stadium)",
    "scg": SYDNEY_CRICKET_GROUND,
    "punt_rd": "Punt_Road_Oval",
    "windy_hill": "Windy_Hill,_Essendon",
    "glenferrie_oval": "Glenferrie_Oval",
    "arden_st": "Arden_Street_Oval",
    "western_oval": "Whitten_Oval",
    "olympic_park": "Olympic_Park_Oval",
    "kardinia_park": "Kardinia_Park_(stadium)",
    "yarraville_oval": "Yarraville_Oval",
    "toorak_park": "Toorak_Park",
    "euroa": "",
    "north_hobart": "North_Hobart_Oval",
    "yallourn": "Yallourn_Football_Club",
    "albury": "Albury_Sports_Ground",
    "brisbane_exhibition": "Brisbane_Showgrounds",
    "moorabbin_oval": "Moorabbin_Oval",
    "coburg_oval": "Coburg_City_Oval",
    "waverley_park": "Waverley_Park",
    "gabba": THE_GABBA,
    "subiaco": "Subiaco_Oval",
    "carrara": "Carrara_Stadium",
    "waca": "WACA_Ground",
    "football_park": "Football_Park",
    "bruce_stadium": "Canberra_Stadium",
    "manuka_oval": "Manuka_Oval",
    "docklands": "Docklands_Stadium",
    "york_park": YORK_PARK,
    "stadium_australia": STADIUM_AUSTRALIA,
    "marrara_oval": "Marrara_Oval",
    "cazalys_stadium": "Cazalys_Stadium",
    "adelaide_oval": "Adelaide_Oval",
    "bellerive_oval": "Bellerive_Oval",
    "blacktown": "Blacktown_International_Sportspark",
    "wrs": "",
    "traeger": TRAEGER_PARK,
    "jiangwan": "Jiangwan_Stadium",
    "eureka": "Eureka_Stadium",
    "perth": "Perth_Stadium",
    "riverway": "Riverway_Stadium",
    "norwood": "Norwood_Oval",
    "summit": "Summit_Sport_and_Recreation_Park",
    "lake_oval": "Lakeside_Stadium",
    # OddsPortal
    "The Gabba": THE_GABBA,
    "Sydney Cricket Ground": SYDNEY_CRICKET_GROUND,
    "Engie Stadium": "Sydney_Showground_Stadium",
    "University of Tasmania Stadium": YORK_PARK,
    "Thunderdome Stadium": "Thunderdome_Stadium",
    "TIO Traeger Park": TRAEGER_PARK,
    "Ondrej Nepela Arena": "Tipos_aréna",
    "Angel Stadium of Anaheim": "Angel_Stadium",
    "Spotland Stadium": "Spotland_Stadium",
    "Giants Stadium": "Giants_Stadium",
    "Accor Arena": "Accor_Arena",
    "Barossa Park": "Lyndoch_Recreation_Park",
    # SportsReference
    "UW–Milwaukee Panther Arena, Milwaukee, Wisconsin": "UW–Milwaukee_Panther_Arena",
    # AFL.com
    "Hands Oval, Bunbury": "Hands_Oval",
    # ESPN
    "4461": "Princess_Auto_Stadium",
    "3610": "Aloha_Stadium",
    "4013": "Camping_World_Stadium",
    "3766": "Independence_Stadium_(Shreveport)",
}


@MEMORY.cache(ignore=["session"])
def create_wikipedia_venue_model(
    session: requests.Session, identifier: str, version: str
) -> VenueModel | None:
    """Create a venue model by looking up the venue on wikipedia."""
    # pylint: disable=protected-access

    wikipage = WIKIPEDIA_VENUE_ID_MAP.get(identifier)
    if wikipage is None:
        logging.warning(
            "Failed to map wikipedia venue for venue identifier: %s", identifier
        )
        return None

    wiki_wiki = wikipediaapi.Wikipedia(user_agent=f"sportsball ({__VERSION__})")
    wiki_wiki._session = session
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
