"""Sports reference player model."""

# pylint: disable=too-many-arguments,unused-argument,line-too-long
import datetime
import http
import logging
from urllib.parse import unquote

import pytest_is_running
import requests_cache
from bs4 import BeautifulSoup

from ...cache import MEMORY
from ...session import DEFAULT_TIMEOUT
from ..player_model import PlayerModel

_FIX_URLS = {
    "https://www.sports-reference.com/cbb/players/leyla-öztürk-1.html": "https://www.sports-reference.com/cbb/players/leyla-ozturk-1.html",
    "https://www.sports-reference.com/cbb/players/vianè-cumber-1.html": "https://www.sports-reference.com/cbb/players/viane-cumber-1.html",
    "https://www.sports-reference.com/cbb/players/cia-eklof-1.html": "https://www.sports-reference.com/cbb/players/cia-eklöf-1.html",
    "https://www.sports-reference.com/cbb/players/chae-harris-1.html": "https://www.sports-reference.com/cbb/players/cha%C3%A9-harris-1.html",
    "https://www.sports-reference.com/cbb/players/tilda-sjokvist-1.html": "https://www.sports-reference.com/cbb/players/tilda-sjökvist-1.html",
    "https://www.sports-reference.com/cbb/players/hana-muhl-1.html": "https://www.sports-reference.com/cbb/players/hana-mühl-1.html",
    "https://www.sports-reference.com/cbb/players/noa-comesaña-1.html": "https://www.sports-reference.com/cbb/players/noa-comesana-1.html",
    "https://www.sports-reference.com/cbb/players/nadège-jean-1.html": "https://www.sports-reference.com/cbb/players/nadege-jean-1.html",
}


def _fix_url(url: str) -> str:
    url = unquote(url)
    url = url.replace("é", "e")
    url = url.replace("ć", "c")
    url = url.replace("ã", "a")
    url = url.replace("á", "a")
    url = url.replace("á", "a")
    url = url.replace("ö", "o")
    url = url.replace("ü", "u")

    url = url.replace("Ã©", "é")
    url = url.replace("Ã¶", "ö")
    url = url.replace("Ã¼", "ü")

    return _FIX_URLS.get(url, url)


def _create_sportsreference_player_model(
    session: requests_cache.CachedSession,
    player_url: str,
    fg: dict[str, int],
    fga: dict[str, int],
    offensive_rebounds: dict[str, int],
    assists: dict[str, int],
    turnovers: dict[str, int],
) -> PlayerModel | None:
    """Create a player model from NCAAB sports reference."""
    player_url = _fix_url(player_url)
    response = session.get(player_url, timeout=DEFAULT_TIMEOUT)
    # Some players can't be accessed on sports reference
    if response.status_code == http.HTTPStatus.FORBIDDEN:
        logging.warning("Cannot access player at URL %s", player_url)
        return None
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    h1 = soup.find("h1")
    if h1 is None:
        logging.warning("h1 is null for %s", player_url)
        return None
    name = h1.get_text().strip()
    return PlayerModel(
        identifier=name,
        jersey=None,
        kicks=None,
        fumbles=None,
        fumbles_lost=None,
        field_goals=fg.get(name),
        field_goals_attempted=fga.get(name),
        offensive_rebounds=offensive_rebounds.get(name),
        assists=assists.get(name),
        turnovers=turnovers.get(name),
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_sportsreference_player_model(
    session: requests_cache.CachedSession,
    player_url: str,
    fg: dict[str, int],
    fga: dict[str, int],
    offensive_rebounds: dict[str, int],
    assists: dict[str, int],
    turnovers: dict[str, int],
) -> PlayerModel | None:
    return _create_sportsreference_player_model(
        session, player_url, fg, fga, offensive_rebounds, assists, turnovers
    )


def create_sportsreference_player_model(
    session: requests_cache.CachedSession,
    player_url: str,
    dt: datetime.datetime,
    fg: dict[str, int],
    fga: dict[str, int],
    offensive_rebounds: dict[str, int],
    assists: dict[str, int],
    turnovers: dict[str, int],
) -> PlayerModel | None:
    """Create a player model from sports reference."""
    if not pytest_is_running.is_running():
        return _cached_create_sportsreference_player_model(
            session, player_url, fg, fga, offensive_rebounds, assists, turnovers
        )
    with session.cache_disabled():
        return _create_sportsreference_player_model(
            session, player_url, fg, fga, offensive_rebounds, assists, turnovers
        )
