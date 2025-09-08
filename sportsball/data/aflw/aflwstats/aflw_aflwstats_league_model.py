"""AFLW AFLWStats league model."""

import urllib.parse
from typing import Iterator

import tqdm
from bs4 import BeautifulSoup
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...game_model import GameModel
from ...league import League
from ...league_model import LeagueModel
from .aflw_aflwstats_game_model import create_aflw_aflwstats_game_model


class AFLWAFLWStatsLeagueModel(LeagueModel):
    """AFLW AFLWStats implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(League.AFLW, session, position=position)

    @classmethod
    def name(cls) -> str:
        return "aflw-aflwstats-league-model"

    def _produce_seasons_games(self, url: str, pbar: tqdm.tqdm) -> Iterator[GameModel]:
        with self.session.cache_disabled():
            with self.session.wayback_disabled():
                response = self.session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        for a in soup.find_all("a"):
            a_url = urllib.parse.urljoin(url, a.get("href"))
            if "/game/" not in a_url:
                continue
            game_model = create_aflw_aflwstats_game_model(
                url=a_url, session=self.session
            )
            pbar.update(1)
            pbar.set_description(f"AFLWStats {game_model.year} - {game_model.dt}")
            yield game_model

    @property
    def games(self) -> Iterator[GameModel]:
        with self.session.cache_disabled():
            with self.session.wayback_disabled():
                response = self.session.get("https://aflwstats.com/")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        with tqdm.tqdm(position=self.position) as pbar:
            for a in soup.find_all("a"):
                a_url = urllib.parse.urljoin(response.url, a.get("href"))
                if "/season/" not in a_url and "/season/7" not in a_url:
                    continue
                yield from self._produce_seasons_games(a_url, pbar)
