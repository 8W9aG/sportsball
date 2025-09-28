"""NFL NFL.com game model."""

import datetime
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from playwright.sync_api import Playwright
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....playwright import ensure_install
from ...game_model import GameModel
from ...league import League
from ...team_model import VERSION
from ...venue_model import VERSION as VENUE_VERSION
from .nfl_nflcom_team_model import create_nfl_nflcom_team_model
from .nfl_nflcom_venue_model import create_nfl_nflcom_venue_model


def create_nfl_nflcom_game_model(
    url: str,
    session: ScrapeSession,
    playwright: Playwright,
    version: str,
) -> GameModel:
    """Create a game model from NFL.com."""
    o = urlparse(url)
    end_path_split = o.path.split("/")[-1].split("-")
    week = int(end_path_split[-1])

    ensure_install()
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto(url, wait_until="load")
    soup = BeautifulSoup(page.content(), "lxml")

    dt = None
    for time in soup.find_all("time"):
        dt = datetime.datetime.fromisoformat(time.get("datetime"))
        break
    if dt is None:
        raise ValueError("dt is null")

    venue_model = None
    for dd in soup.find_all("dd", {"aria-labelledby": "info-card-term-STADIUM"}):
        venue_model = create_nfl_nflcom_venue_model(
            venue_name=dd.get_text().strip(),
            session=session,
            dt=dt,
            version=VENUE_VERSION,
        )
        break

    home_team_name = end_path_split[2]
    away_team_name = end_path_split[0]
    teams = [
        create_nfl_nflcom_team_model(
            team_name=x, dt=dt, session=session, version=VERSION
        )
        for x in [home_team_name, away_team_name]
    ]

    return GameModel(
        dt=dt,
        week=week,
        game_number=None,
        venue=venue_model,
        teams=teams,
        end_dt=None,
        attendance=None,
        league=League.NFL,
        year=dt.year,
        season_type=None,
        postponed=None,
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        version=version,
        umpires=[],
        best_of=None,
    )
