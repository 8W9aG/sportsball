"""WTA combined league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.wta_espn_league_model import WTAESPNLeagueModel
from ..oddsportal.wta_oddsportal_league_model import WTAOddsPortalLeagueModel
from ..tennisabstract.wta_tennisabstract_league_model import \
    WTATennisAbstractLeagueModel

WTA_TEAM_IDENTITY_MAP: dict[str, str] = {}
WTA_VENUE_IDENTITY_MAP: dict[str, str] = {}
WTA_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class WTACombinedLeagueModel(CombinedLeagueModel):
    """WTA combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.WTA,
            [
                WTAOddsPortalLeagueModel(session, position=0),
                WTATennisAbstractLeagueModel(session, position=1),
                WTAESPNLeagueModel(session, position=2),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return WTA_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return WTA_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return WTA_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "wta-combined-league-model"
