"""NBA sports reference league model."""

# pylint: disable=line-too-long

from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...league import League
from ...sportsreference.sportsreference_league_model import \
    SportsReferenceLeagueModel
from ..position import Position


class EPLSportsReferenceLeagueModel(SportsReferenceLeagueModel):
    """EPL Sports Reference implementation of the league model."""

    def __init__(self, session: ScrapeSession, position: int | None = None) -> None:
        super().__init__(
            session,
            League.EPL,
            "https://fbref.com/en/matches/",
            position=position,
        )

    @classmethod
    def name(cls) -> str:
        return "epl-sportsreference-league-model"

    @classmethod
    def position_validator(cls) -> dict[str, str]:
        return {str(x): str(x) for x in Position}
