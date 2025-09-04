"""EPL combined league model."""

# pylint: disable=line-too-long
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.epl_espn_league_model import EPLESPNLeagueModel
from ..oddsportal.epl_oddsportal_league_model import EPLOddsPortalLeagueModel

EPL_TEAM_IDENTITY_MAP: dict[str, str] = {}
EPL_VENUE_IDENTITY_MAP: dict[str, str] = {}
EPL_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class EPLCombinedLeagueModel(CombinedLeagueModel):
    """NBA combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.EPL,
            [
                EPLESPNLeagueModel(session, position=0),
                EPLOddsPortalLeagueModel(session, position=1),
                # EPLSportsDBLeagueModel(session, position=2),
                # EPLSportsReferenceLeagueModel(session, position=3),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return EPL_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return EPL_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return EPL_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "epl-combined-league-model"
