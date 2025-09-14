"""NCAABW OddsPortal league model."""

# pylint: disable=line-too-long

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...league import League
from ...oddsportal.oddsportal_league_model import OddsPortalLeagueModel


class NCAABWOddsPortalLeagueModel(OddsPortalLeagueModel):
    """NCAABW OddsPortal implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(League.NCAABW, session, position=position)

    @classmethod
    def name(cls) -> str:
        return "ncaabw-oddsportal-league-model"
