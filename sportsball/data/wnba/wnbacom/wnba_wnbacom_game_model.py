"""WNBA WNBA.com game model."""

import re
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from dateutil.parser import parse
from playwright.sync_api import Playwright
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....playwright import ensure_install
from ...game_model import GameModel
from ...league import League
from ...team_model import VERSION
from ...venue_model import VERSION as VENUE_VERSION
from .wnba_wnbacom_team_model import create_wnba_wnbacom_team_model
from .wnba_wnbacom_venue_model import create_wnba_wnbacom_venue_model


def create_wnba_wnbacom_game_model(
    url: str,
    session: ScrapeSession,
    playwright: Playwright,
    version: str,
) -> GameModel:
    """Create a game model from WNBA.com."""
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
    for div_date in soup.find_all(
        "div", {"class": re.compile("_GameStatusExpanded__date.*")}
    ):
        date_txt = div_date.get_text().strip()
        for div_time in soup.find_all(
            "div", {"class": re.compile("_GameStatusExpanded__date.*")}
        ):
            time_txt = div_time.get_text().strip()
            dt = parse(" ".join([date_txt, time_txt]))
            break
        break
    if dt is None:
        raise ValueError("dt is null")

    venue_model = None
    for div_location in soup.find_all(
        "div", {"class": re.compile("_GameDetailsHeader--location.*")}
    ):
        venue_model = create_wnba_wnbacom_venue_model(
            venue_name=div_location.get_text().strip(),
            session=session,
            dt=dt,
            version=VENUE_VERSION,
        )
        break

    teams = []
    for div_team in soup.find_all(
        "div", {"class": re.compile("_GameDetailsHeader--team.*")}
    ):
        team_name = div_team.get_text().strip().replace("\n", "").strip()
        teams.append(
            create_wnba_wnbacom_team_model(
                team_name=team_name, dt=dt, session=session, version=VERSION
            )
        )

    return GameModel(
        dt=dt,
        week=week,
        game_number=None,
        venue=venue_model,
        teams=list(reversed(teams)),
        end_dt=None,
        attendance=None,
        league=League.WNBA,
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
