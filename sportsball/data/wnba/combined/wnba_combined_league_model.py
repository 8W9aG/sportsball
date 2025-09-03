"""WNBA combined league model."""

# pylint: disable=line-too-long
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.wnba_espn_league_model import WNBAESPNLeagueModel
from ..oddsportal.wnba_oddsportal_league_model import WNBAOddsPortalLeagueModel

WNBA_TEAM_IDENTITY_MAP: dict[str, str] = {}
WNBA_VENUE_IDENTITY_MAP: dict[str, str] = {}
WNBA_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class WNBACombinedLeagueModel(CombinedLeagueModel):
    """WNBA combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.WNBA,
            [
                WNBAESPNLeagueModel(session, position=0),
                WNBAOddsPortalLeagueModel(session, position=1),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return WNBA_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return WNBA_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return WNBA_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "wnba-combined-league-model"
