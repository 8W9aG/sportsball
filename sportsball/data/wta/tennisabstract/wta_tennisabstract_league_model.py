"""WTA TennisAbstract league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...league import League
from ...tennisabstract.tennisabstract_league_model import \
    TennisAbstractLeagueModel


class WTATennisAbstractLeagueModel(TennisAbstractLeagueModel):
    """WTA TennisAbstract implementation of the league model."""

    def __init__(
        self,
        session: ScrapeSession,
        position: int | None = None,
    ) -> None:
        super().__init__(League.WTA, session, position=position)

    @classmethod
    def name(cls) -> str:
        """The name of the league model."""
        return "wta-tennisabstract-league-model"
