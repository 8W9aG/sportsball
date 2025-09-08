"""AFLW combined league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..aflwstats.aflw_aflwstats_league_model import AFLWAFLWStatsLeagueModel
from ..oddsportal.aflw_oddsportal_league_model import AFLWOddsPortalLeagueModel

AFLW_TEAM_IDENTITY_MAP: dict[str, str] = {}
AFLW_VENUE_IDENTITY_MAP: dict[str, str] = {}


class AFLWCombinedLeagueModel(CombinedLeagueModel):
    """AFLW combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.AFLW,
            [
                AFLWAFLWStatsLeagueModel(session, position=0),
                AFLWOddsPortalLeagueModel(session, position=1),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return AFLW_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return AFLW_VENUE_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "aflw-combined-league-model"
