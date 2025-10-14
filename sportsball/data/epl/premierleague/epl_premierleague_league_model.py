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

    _found_matches: set[str]

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(League.NFL, session, position=position)
        self._found_matches = set()

    @classmethod
    def name(cls) -> str:
        return "epl-premierleague-league-model"

    @property
    def games(self) -> Iterator[GameModel]:
        self._found_matches = set()
        with self.session.wayback_disabled():
            with tqdm.tqdm(position=self.position) as pbar:
                try:
                    pagination_token = None
                    current_date = None
                    while True:

                        def find_games() -> Iterator[GameModel]:
                            nonlocal current_date
                            nonlocal pagination_token
                            url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v2/matches?competition=8"
                            if pagination_token is not None:
                                url += "&_next=" + pagination_token
                            response = self.session.get(url)
                            response.raise_for_status()
                            data = response.json()
                            for game_data in data["data"]:
                                if needs_shutdown():
                                    return
                                if game_data["matchId"] in self._found_matches:
                                    continue
                                game_model = create_epl_premierleague_game_model(
                                    game=game_data,
                                    session=self.session,
                                    version=VERSION,
                                )
                                pbar.update(1)
                                pbar.set_description(f"PremierLeague - {game_model.dt}")
                                yield game_model
                                current_date = game_model.dt.date()
                                self._found_matches.add(game_data["matchId"])
                                if (
                                    game_model.dt.date()
                                    >= (
                                        datetime.datetime.now()
                                        + datetime.timedelta(days=7)
                                    ).date()
                                ):
                                    return
                            pagination_token = data["pagination"]["_next"]

                        if (
                            current_date is None
                            or current_date
                            < (
                                datetime.datetime.now() - datetime.timedelta(days=7)
                            ).date()
                        ):
                            yield from find_games()
                        else:
                            with self.session.cache_disabled():
                                yield from find_games()

                except Exception as exc:
                    SHUTDOWN_FLAG.set()
                    raise exc
