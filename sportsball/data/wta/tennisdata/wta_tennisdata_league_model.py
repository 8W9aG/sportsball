"""WTA TennisData league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...league import League
from ...tennisdata.tennisdata_league_model import TennisDataLeagueModel


class WTATennisDataLeagueModel(TennisDataLeagueModel):
    """WTA TennisData implementation of the league model."""

    def __init__(
        self,
        session: ScrapeSession,
        position: int | None = None,
    ) -> None:
        super().__init__(League.WTA, session, position=position)

    @classmethod
    def name(cls) -> str:
        """The name of the league model."""
        return "wta-tennisdata-league-model"
