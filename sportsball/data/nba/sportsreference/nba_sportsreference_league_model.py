"""NBA sports reference league model."""

# pylint: disable=line-too-long

import requests_cache

from ...league import League
from ...sportsreference.sportsreference_league_model import \
    SportsReferenceLeagueModel


class NBASportsReferenceLeagueModel(SportsReferenceLeagueModel):
    """NBA Sports Reference implementation of the league model."""

    def __init__(self, session: requests_cache.CachedSession) -> None:
        super().__init__(
            session, League.NBA, "https://www.basketball-reference.com/boxscores/"
        )
