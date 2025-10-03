"""WNBA WNBA.com league model."""

import datetime
from typing import Iterator

from scrapesession.scrapesession import ScrapeSession  # type: ignore

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
        return "wnba-wnbacom-league-model"

    @property
    def games(self) -> Iterator[GameModel]:
        try:
            with self.session.cache_disabled():
                with self.session.wayback_disabled():
                    response = self.session.get(
                        "https://content-api-prod.nba.com/public/1/leagues/wnba/schedule"
                    )
                    response.raise_for_status()
                    data = response.json()
                    now_utc = datetime.datetime.now(datetime.timezone.utc)
                    for game_dict in data["results"]["schedule"]:
                        dt = datetime.datetime.fromisoformat(game_dict["utcTime"])
                        if dt <= now_utc:
                            continue
                        home_dict = game_dict["home"]
                        away_dict = game_dict["home"]
                        home_id = home_dict["tid"]
                        away_id = away_dict["tid"]
                        if home_id is None or away_id is None:
                            continue
                        yield create_wnba_wnbacom_game_model(
                            game_dict=game_dict,
                            session=self.session,
                            version=VERSION,
                        )
        except Exception as exc:
            SHUTDOWN_FLAG.set()
            raise exc
