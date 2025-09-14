"""NCAABW combined league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.ncaabw_espn_league_model import NCAABWESPNLeagueModel
from ..oddsportal.ncaabw_oddsportal_league_model import \
    NCAABWOddsPortalLeagueModel

NCAABW_TEAM_IDENTITY_MAP: dict[str, str] = {}
NCAABW_VENUE_IDENTITY_MAP: dict[str, str] = {}
NCAABW_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class NCAABWCombinedLeagueModel(CombinedLeagueModel):
    """NCAABW combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.NCAABW,
            [
                NCAABWESPNLeagueModel(session, position=0),
                NCAABWOddsPortalLeagueModel(session, position=1),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return NCAABW_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return NCAABW_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return NCAABW_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "ncaabw-combined-league-model"
