"""The main sportsball class for accessing data."""

from typing import Dict
from warnings import simplefilter

import pandas as pd
from dotenv import load_dotenv
from scrapesession.scrapesession import ScrapeSession  # type: ignore
from scrapesession.scrapesession import create_scrape_session

from .data.afl import AFLLeagueModel
from .data.epl import EPLLeagueModel
from .data.hkjc import HKJCLeagueModel
from .data.league import League
from .data.league_model import LeagueModel
from .data.mlb import MLBLeagueModel
from .data.nba import NBALeagueModel
from .data.ncaab import NCAABLeagueModel
from .data.ncaaf import NCAAFLeagueModel
from .data.nfl import NFLLeagueModel
from .data.nhl import NHLLeagueModel


class SportsBall:
    """The main sportsball class."""

    # pylint: disable=too-few-public-methods

    _leagues: Dict[str, LeagueModel]
    _session: ScrapeSession

    def __init__(self) -> None:
        self._session = create_scrape_session(
            "sportsball",
            {
                "https://news.google.com/",
                "https://historical-forecast-api.open-meteo.com/",
                "https://api.open-meteo.com/",
            },
        )
        self._leagues = {}
        simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
        load_dotenv()

    def league(self, league: League, league_filter: str | None) -> LeagueModel:
        """Provide a league model for the given league."""
        if league not in self._leagues:
            if league == League.NFL:
                self._leagues[league] = NFLLeagueModel(self._session, league_filter)
            elif league == League.AFL:
                self._leagues[league] = AFLLeagueModel(self._session, league_filter)
            elif league == League.NBA:
                self._leagues[league] = NBALeagueModel(self._session, league_filter)
            elif league == League.NCAAF:
                self._leagues[league] = NCAAFLeagueModel(self._session, league_filter)
            elif league == League.NCAAB:
                self._leagues[league] = NCAABLeagueModel(self._session, league_filter)
            elif league == League.HKJC:
                self._leagues[league] = HKJCLeagueModel(self._session)
            elif league == League.NHL:
                self._leagues[league] = NHLLeagueModel(self._session, league_filter)
            elif league == League.MLB:
                self._leagues[league] = MLBLeagueModel(self._session, league_filter)
            elif league == League.EPL:
                self._leagues[league] = EPLLeagueModel(self._session, league_filter)
            else:
                raise ValueError(f"Unrecognised league: {league}")
        return self._leagues[league]
