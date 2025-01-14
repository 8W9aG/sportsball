"""AFL AFLTables team model."""

import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from ....cache import MEMORY
from ...team_model import TeamModel
from .afl_afltables_player_model import create_afl_afltables_player_model

_TEAM_NAME_MAP = {
    "Melbourne": ["ME"],
    "Geelong": ["GE"],
    "Fitzroy": ["FI"],
    "Collingwood": ["CW"],
    "Essendon": ["ES"],
    "South Melbourne": ["SM"],
    "St Kilda": ["SK"],
    "Carlton": ["CA"],
    "Sydney": ["SM", "SY"],
    "University": ["UN"],
    "Richmond": ["RI"],
    "North Melbourne": ["NM"],
    "Western Bulldogs": ["WB", "FO"],
    "Hawthorn": ["HW"],
    "Brisbane Bears": ["BB"],
    "West Coast": ["WC"],
    "Adelaide": ["AD"],
    "Fremantle": ["FR"],
    "Brisbane Lions": ["BL"],
    "Port Adelaide": ["PA"],
    "Gold Coast": ["GC"],
    "Greater Western Sydney": ["GW"],
}


@MEMORY.cache(ignore=["session"])
def create_afl_afltables_team_model(
    team_url: str,
    players: list[tuple[str, str, int | None]],
    points: float,
    session: requests.Session,
    last_ladder_ranks: dict[str, int] | None,
) -> TeamModel:
    """Create a team model from AFL Tables."""
    response = session.get(team_url)
    soup = BeautifulSoup(response.text, "html.parser")
    o = urlparse(team_url)
    last_component = o.path.split("/")[-1]
    identifier, _ = os.path.splitext(last_component)
    h1 = soup.find("h1")
    if h1 is None:
        raise ValueError("h1 is null.")
    name = h1.get_text()
    last_ladder_rank = None
    if last_ladder_ranks is not None and last_ladder_ranks:
        short_names = _TEAM_NAME_MAP[name]
        for short_name in short_names:
            if short_name in last_ladder_ranks:
                last_ladder_rank = last_ladder_ranks[short_name]
                break
    return TeamModel(
        identifier=identifier,
        name=name,
        players=[  # pyright: ignore
            create_afl_afltables_player_model(player_url, jersey, kicks)
            for player_url, jersey, kicks in players
        ],
        odds=[],
        points=points,
        ladder_rank=last_ladder_rank,
        location=None,
    )
