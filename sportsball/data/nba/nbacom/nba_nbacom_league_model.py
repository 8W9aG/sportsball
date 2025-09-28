"""NBA NBA.com league model."""

# pylint: disable=too-many-statements,protected-access,too-many-locals,bare-except,too-many-branches,duplicate-code
import datetime
import logging
from typing import Iterator

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...game_model import VERSION, GameModel
from ...league import League
from ...league_model import SHUTDOWN_FLAG, LeagueModel, needs_shutdown
from .nba_nbacom_game_model import create_nba_nbacom_game_model


class NBANBAComLeagueModel(LeagueModel):
    """NBA NBA.com implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(League.NFL, session, position=position)

    @classmethod
    def name(cls) -> str:
        return "nba-nbacom-league-model"

    @property
    def games(self) -> Iterator[GameModel]:
        try:
            with self.session.cache_disabled():
                date_slug = datetime.datetime.today().date().strftime("%Y%m%d")
                response = self.session.get(
                    f"https://stats.nba.com/js/data/leaders/00_daily_lineups_{date_slug}.json"
                )
                if response.ok:
                    lineup = response.json()
                    for game in lineup["games"]:
                        if needs_shutdown():
                            return
                        yield create_nba_nbacom_game_model(
                            game=game, session=self.session, version=VERSION
                        )
                else:
                    logging.warning("Failed to fetch NBA daily lineups.")
        except Exception as exc:
            SHUTDOWN_FLAG.set()
            raise exc
