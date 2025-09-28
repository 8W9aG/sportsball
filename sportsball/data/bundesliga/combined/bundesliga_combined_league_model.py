"""Bundesliga combined league model."""

# pylint: disable=line-too-long
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.bundesliga_espn_league_model import BundesligaESPNLeagueModel
from ..footballdata.bundesliga_footballdata_league_model import \
    BundesligaFootballDataLeagueModel
from ..oddsportal.bundesliga_oddsportal_league_model import \
    BundesligaOddsPortalLeagueModel

BUNDESLIGA_TEAM_IDENTITY_MAP: dict[str, str] = {}
BUNDESLIGA_VENUE_IDENTITY_MAP: dict[str, str] = {}
BUNDESLIGA_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class BundesligaCombinedLeagueModel(CombinedLeagueModel):
    """Bundesliga combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.BUNDESLIGA,
            [
                BundesligaESPNLeagueModel(session, position=0),
                BundesligaOddsPortalLeagueModel(session, position=1),
                BundesligaFootballDataLeagueModel(session, position=2),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return BUNDESLIGA_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return BUNDESLIGA_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return BUNDESLIGA_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "bundesliga-combined-league-model"
