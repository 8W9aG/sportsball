"""EPL FootballData league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...footballdata.footballdata_league_model import FootballDataLeagueModel
from ...league import League


class EPLFootballDataLeagueModel(FootballDataLeagueModel):
    """EPL FootballData implementation of the league model."""

    def __init__(
        self,
        session: ScrapeSession,
        position: int | None = None,
    ) -> None:
        super().__init__(League.EPL, session, position=position)

    @classmethod
    def name(cls) -> str:
        """The name of the league model."""
        return "epl-footballdata-league-model"
