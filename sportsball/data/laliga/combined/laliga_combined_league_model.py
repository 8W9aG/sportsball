"""EPL combined league model."""

# pylint: disable=line-too-long
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.laliga_espn_league_model import LaLigaESPNLeagueModel
from ..footballdata.laliga_footballdata_league_model import \
    LaLigaFootballDataLeagueModel
from ..oddsportal.laliga_oddsportal_league_model import \
    LaLigaOddsPortalLeagueModel

LALIGA_TEAM_IDENTITY_MAP: dict[str, str] = {}
LALIGA_VENUE_IDENTITY_MAP: dict[str, str] = {}
LALIGA_PLAYER_IDENTITY_MAP: dict[str, str] = {}


class LaLigaCombinedLeagueModel(CombinedLeagueModel):
    """LaLiga combined implementation of the league model."""

    def __init__(self, session: ScrapeSession, league_filter: str | None) -> None:
        super().__init__(
            session,
            League.LALIGA,
            [
                LaLigaESPNLeagueModel(session, position=0),
                LaLigaOddsPortalLeagueModel(session, position=1),
                LaLigaFootballDataLeagueModel(session, position=2),
            ],
            league_filter,
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return LALIGA_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return LALIGA_VENUE_IDENTITY_MAP

    @classmethod
    def player_identity_map(cls) -> dict[str, str]:
        return LALIGA_PLAYER_IDENTITY_MAP

    @classmethod
    def name(cls) -> str:
        return "laliga-combined-league-model"
