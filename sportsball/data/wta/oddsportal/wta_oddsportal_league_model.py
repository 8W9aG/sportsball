"""WTA OddsPortal league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...league import League
from ...oddsportal.oddsportal_league_model import OddsPortalLeagueModel


class WTAOddsPortalLeagueModel(OddsPortalLeagueModel):
    """WTA OddsPortal implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(League.WTA, session, position=position)
