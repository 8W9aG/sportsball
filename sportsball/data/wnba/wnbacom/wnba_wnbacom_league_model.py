"""WNBA WNBA.com league model."""

import urllib.parse
from typing import Iterator

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ....playwright import ensure_install
from ...game_model import VERSION, GameModel
from ...league import League
from ...league_model import SHUTDOWN_FLAG, LeagueModel
from .wnba_wnbacom_game_model import create_wnba_wnbacom_game_model


class WNBAWNBAComLeagueModel(LeagueModel):
    """WNBA WNBA.com implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(League.WNBA, session, position=position)

    @classmethod
    def name(cls) -> str:
        return "wnba-nflcom-league-model"

    @property
    def games(self) -> Iterator[GameModel]:
        try:
            ensure_install()
            with sync_playwright() as p:
                browser = p.chromium.launch()
                context = browser.new_context()
                page = context.new_page()
                url = "https://www.wnba.com/schedule?season=2025&month=all"
                page.goto(url, wait_until="load")
                soup = BeautifulSoup(page.content(), "lxml")
                game_urls = []
                for a in soup.find_all(
                    "a",
                ):
                    game_url = urllib.parse.urljoin(url, a.get("href"))
                    if not game_url.startswith("https://www.wnba.com/game/"):
                        continue
                    game_urls.append(game_url)
                for game_url in game_urls:
                    yield create_wnba_wnbacom_game_model(
                        url=game_url,
                        session=self.session,
                        playwright=p,
                        version=VERSION,
                    )
        except Exception as exc:
            SHUTDOWN_FLAG.set()
            raise exc
