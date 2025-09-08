"""NHL combined league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.nhl_espn_league_model import NHLESPNLeagueModel
from ..oddsportal.nhl_oddsportal_league_model import NHLOddsPortalLeagueModel

NHL_TEAM_IDENTITY_MAP: dict[str, str] = {}
NHL_VENUE_IDENTITY_MAP: dict[str, str] = {}
NHL_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class NHLCombinedLeagueModel(CombinedLeagueModel):
    """NHL combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.NHL,
            [
                NHLESPNLeagueModel(session, position=0),
                NHLOddsPortalLeagueModel(session, position=1),
                # NHLSportsDBLeagueModel(session, position=2),
                # NHLSportsReferenceLeagueModel(session, position=3),
            ],
            league_filter,
        )

    @classmethod
    def name(cls) -> str:
        return "nhl-combined-league-model"

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return NHL_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return NHL_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return NHL_PLAYER_IDENTITY_MAP
