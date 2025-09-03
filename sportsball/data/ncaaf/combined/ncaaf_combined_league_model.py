"""NCAAF combined league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.ncaaf_espn_league_model import NCAAFESPNLeagueModel
from ..oddsportal.ncaaf_oddsportal_league_model import \
    NCAAFOddsPortalLeagueModel

# from ..sportsreference.ncaaf_sportsreference_league_model import \
#    NCAAFSportsReferenceLeagueModel

NCAAF_TEAM_IDENTITY_MAP: dict[str, str] = {}
NCAAF_VENUE_IDENTITY_MAP: dict[str, str] = {}
NCAAF_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class NCAAFCombinedLeagueModel(CombinedLeagueModel):
    """NCAAF combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.NCAAF,
            [
                NCAAFESPNLeagueModel(session, position=0),
                NCAAFOddsPortalLeagueModel(session, position=1),
                # NCAAFSportsDBLeagueModel(session, position=2),
                # NCAAFSportsReferenceLeagueModel(session, position=3),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return NCAAF_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return NCAAF_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return NCAAF_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "ncaaf-combined-league-model"
