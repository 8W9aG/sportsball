"""EPL premierleague.com league model."""

import datetime
from typing import Iterator

import tqdm
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...game_model import VERSION, GameModel
from ...league import League
from ...league_model import SHUTDOWN_FLAG, LeagueModel, needs_shutdown
from .epl_premierleague_game_model import create_epl_premierleague_game_model


class EPLPremierLeagueLeagueModel(LeagueModel):
    """EPL PremierLeague implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(League.NFL, session, position=position)

    @classmethod
    def name(cls) -> str:
        return "epl-premierleague-league-model"

    @property
    def games(self) -> Iterator[GameModel]:
        with tqdm.tqdm(position=self.position) as pbar:
            try:
                with self.session.cache_disabled():
                    pagination_token = None
                    while True:
                        url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v2/matches?competition=8"
                        if pagination_token is not None:
                            url += "&_next=" + pagination_token
                        response = self.session.get(url)
                        response.raise_for_status()
                        data = response.json()
                        for games_data in data["data"]:
                            if needs_shutdown():
                                return
                            for game_data in games_data:
                                game_model = create_epl_premierleague_game_model(
                                    game=game_data,
                                    session=self.session,
                                    version=VERSION,
                                )
                                pbar.update(1)
                                pbar.set_description(f"PremierLeague - {game_model.dt}")
                                yield game_model
                                if (
                                    game_model.dt
                                    >= datetime.datetime.now()
                                    + datetime.timedelta(days=7)
                                ):
                                    return
                        pagination_token = data["pagination"]["_next"]
            except Exception as exc:
                SHUTDOWN_FLAG.set()
                raise exc
