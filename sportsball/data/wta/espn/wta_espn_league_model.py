"""WTA ESPN league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...espn.espn_league_model import ESPNLeagueModel
from ...league import League

_SEASON_URL = (
    "http://sports.core.api.espn.com/v2/sports/tennis/leagues/wta/seasons?limit=100"
)


class WTAESPNLeagueModel(ESPNLeagueModel):
    """WTA ESPN implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(_SEASON_URL, League.WTA, session, position=position)

    @classmethod
    def name(cls) -> str:
        return "wta-espn-league-model"

    @classmethod
    def position_validator(cls) -> dict[str, str]:
        return {}
