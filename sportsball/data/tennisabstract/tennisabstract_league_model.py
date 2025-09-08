"""TennisAbstract league model."""

import os
import urllib.parse
from typing import Iterator

import tqdm
from bs4 import BeautifulSoup
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ..game_model import GameModel
from ..league import League
from ..league_model import SHUTDOWN_FLAG, LeagueModel, needs_shutdown
from .tennisabstract_game_model import create_tennisabstract_game_model


class TennisAbstractLeagueModel(LeagueModel):
    """TennisAbstract implementation of the league model."""

    def __init__(
        self,
        league: League,
        session: ScrapeSession,
        position: int | None = None,
    ) -> None:
        super().__init__(league, session, position=position)

    @classmethod
    def name(cls) -> str:
        """The name of the league model."""
        return "tennisabstract-league-model"

    @classmethod
    def position_validator(cls) -> dict[str, str]:
        """Tennis position validators."""
        return {}

    @property
    def games(self) -> Iterator[GameModel]:
        """Find all the games."""
        try:
            with tqdm.tqdm(position=self.position) as pbar:
                url = "https://www.tennisabstract.com/charting/"
                response = None
                with self.session.wayback_disabled():
                    with self.session.cache_disabled():
                        self.session.cache.delete(urls=[url])
                        response = self.session.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "lxml")
                for a in soup.find_all("a", href=True):
                    if needs_shutdown():
                        return
                    match_name = a.get_text().strip()
                    if self.league == League.ATP:
                        if not match_name.endswith("(ATP)"):
                            continue
                    elif self.league == League.WTA:
                        if not match_name.endswith("(WTA)"):
                            continue
                    match_url = urllib.parse.urljoin(url, a.get("href"))
                    filename = os.path.basename(match_url)
                    datestr = filename.split("-")[0]
                    if len(datestr) == 8 and datestr.isnumeric():
                        pbar.update(1)
                        game_model = create_tennisabstract_game_model(
                            self.session,
                            match_url,
                            self.league,
                        )
                        if game_model is None:
                            continue
                        pbar.set_description(f"TennisAbstract {game_model.dt}")
                        yield game_model
        except Exception as exc:
            SHUTDOWN_FLAG.set()
            raise exc
