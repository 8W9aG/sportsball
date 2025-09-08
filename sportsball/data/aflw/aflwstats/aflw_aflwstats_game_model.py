"""AFLW AFLWStats game model."""

import io
import logging
import urllib.parse
from urllib.parse import urlparse

import pandas as pd
import pytest_is_running
from bs4 import BeautifulSoup
from dateutil.parser import parse
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....cache import MEMORY
from ...game_model import VERSION, GameModel
from ...league import League
from .aflw_aflwstats_team_model import create_aflw_aflwstats_team_model
from .aflw_aflwstats_venue_model import create_aflw_aflwstats_venue_model


def _create_aflw_aflwstats_game_model(
    session: ScrapeSession,
    url: str,
    version: str,
) -> GameModel:
    o = urlparse(url)
    season_year = o.path.split("/")[-1]

    response = session.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    h4 = soup.find("h4")
    if h4 is None:
        raise ValueError("h4 is null")
    h4_text = h4.get_text()
    dt = None
    week = None
    venue_name = None
    for line in h4_text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if "/" in line and ":" in line:
            dt = parse(line)
        elif "Round" in line:
            week = int(line.replace("Round", "").strip())
        else:
            venue_name = line

    team_urls = []
    player_urls = {}
    for a in soup.find_all("a"):
        a_url = urllib.parse.urljoin(url, a.get("href"))
        if "/team/" in a_url:
            team_urls.append(a_url)
        elif "/player/" in a_url:
            player_urls[a.get_text().strip()] = a_url

    points = []
    for h2 in soup.find_all("h2"):
        for line in h2.get_text().split("\n"):
            line = line.strip()
            if not line:
                continue
            if "." not in line:
                continue
            points.append(float(line.split()[-1]))

    handle = io.StringIO()
    handle.write(response.text)
    handle.seek(0)
    dfs = pd.read_html(handle)
    players = []
    for df in dfs:
        if "Player" not in df.columns.values.tolist():
            continue
        players.append(df.to_dict())

    if dt is None:
        raise ValueError("dt is null")
    if venue_name is None:
        raise ValueError("venue_name is null")

    try:
        return GameModel(
            dt=dt,
            week=week,
            game_number=None,
            venue=create_aflw_aflwstats_venue_model(
                name=venue_name, session=session, dt=dt
            ),
            teams=[
                create_aflw_aflwstats_team_model(
                    team_url=team_url,
                    players=players[count],  # type: ignore
                    points=float(points[count]),
                    session=session,
                    player_urls=player_urls,
                    dt=dt,
                )
                for count, team_url in enumerate(team_urls)
            ],
            end_dt=None,
            attendance=None,
            league=str(League.AFLW),
            year=int(season_year),
            season_type=None,
            postponed=None,
            play_off=None,
            distance=None,
            dividends=[],
            pot=None,
            version=version,
            umpires=[],
        )
    except ValueError as exc:
        logging.error(str(exc))
        logging.error(url)
        raise exc


@MEMORY.cache(ignore=["session"])
def _cached_create_aflw_aflwstats_game_model(
    session: ScrapeSession,
    url: str,
    version: str,
) -> GameModel:
    return _create_aflw_aflwstats_game_model(
        session=session,
        url=url,
        version=version,
    )


def create_aflw_aflwstats_game_model(
    session: ScrapeSession,
    url: str,
) -> GameModel:
    """Create a game model from AFLWStats."""
    if not pytest_is_running.is_running():
        return _cached_create_aflw_aflwstats_game_model(
            session=session,
            url=url,
            version=VERSION,
        )
    with session.cache_disabled():
        return _create_aflw_aflwstats_game_model(
            session=session,
            url=url,
            version=VERSION,
        )
