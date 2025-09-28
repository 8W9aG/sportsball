"""Bundesliga FootballData league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...footballdata.footballdata_league_model import FootballDataLeagueModel
from ...league import League


class BundesligaFootballDataLeagueModel(FootballDataLeagueModel):
    """Bundesliga FootballData implementation of the league model."""

    def __init__(
        self,
        session: ScrapeSession,
        position: int | None = None,
    ) -> None:
        super().__init__(League.BUNDESLIGA, session, position=position)

    @classmethod
    def name(cls) -> str:
        """The name of the league model."""
        return "bundesliga-footballdata-league-model"
