"""LaLiga FootballData league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...footballdata.footballdata_league_model import FootballDataLeagueModel
from ...league import League


class LaLigaFootballDataLeagueModel(FootballDataLeagueModel):
    """LaLiga FootballData implementation of the league model."""

    def __init__(
        self,
        session: ScrapeSession,
        position: int | None = None,
    ) -> None:
        super().__init__(League.LALIGA, session, position=position)

    @classmethod
    def name(cls) -> str:
        """The name of the league model."""
        return "laliga-footballdata-league-model"
