"""MLB combined league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.mlb_espn_league_model import MLBESPNLeagueModel
from ..oddsportal.mlb_oddsportal_league_model import MLBOddsPortalLeagueModel

MLB_TEAM_IDENTITY_MAP: dict[str, str] = {}
MLB_VENUE_IDENTITY_MAP: dict[str, str] = {}
MLB_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class MLBCombinedLeagueModel(CombinedLeagueModel):
    """MLB combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.MLB,
            [
                MLBESPNLeagueModel(session, position=0),
                MLBOddsPortalLeagueModel(session, position=1),
                # MLBSportsDBLeagueModel(session, position=2),
                # MLBSportsReferenceLeagueModel(session, position=3),
            ],
            league_filter,
        )

    @classmethod
    def name(cls) -> str:
        return "mlb-combined-league-model"

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return MLB_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return MLB_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return MLB_PLAYER_IDENTITY_MAP
