"""LaLiga ESPN league model."""

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...epl.position import Position
from ...espn.espn_league_model import ESPNLeagueModel
from ...league import League

_SEASON_URL = (
    "http://sports.core.api.espn.com/v2/sports/soccer/leagues/esp.1/seasons?limit=100"
)


class LaLigaESPNLeagueModel(ESPNLeagueModel):
    """LaLiga ESPN implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(_SEASON_URL, League.LALIGA, session, position=position)

    @classmethod
    def name(cls) -> str:
        return "laliga-espn-league-model"

    @classmethod
    def position_validator(cls) -> dict[str, str]:
        positions = {str(x): str(x) for x in Position}
        positions["RCF"] = str(Position.CENTRE_FORWARD_RIGHT)
        return positions
