"""NCAAF combined league model."""

import requests_cache

from ...combined.combined_league_model import CombinedLeagueModel
from ...league import League
from ..espn.ncaaf_espn_league_model import NCAAFESPNLeagueModel
from ..oddsportal.ncaaf_oddsportal_league_model import \
    NCAAFOddsPortalLeagueModel

NCAAF_TEAM_IDENTITY_MAP: dict[str, str] = {}
NCAAF_VENUE_IDENTITY_MAP: dict[str, str] = {}


class NCAAFCombinedLeagueModel(CombinedLeagueModel):
    """NCAAF combined implementation of the league model."""

    def __init__(self, session: requests_cache.CachedSession) -> None:
        super().__init__(
            session,
            League.NCAAF,
            [
                NCAAFESPNLeagueModel(session, position=0),
                NCAAFOddsPortalLeagueModel(session, position=1),
            ],
        )

    @classmethod
    def team_identity_map(cls) -> dict[str, str]:
        return NCAAF_TEAM_IDENTITY_MAP

    @classmethod
    def venue_identity_map(cls) -> dict[str, str]:
        return NCAAF_VENUE_IDENTITY_MAP
