"""SportsDB game model."""

# pylint: disable=too-many-arguments,duplicate-code
import datetime
from typing import Any

import pytest_is_running
from dateutil import parser
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..game_model import VERSION, GameModel
from ..league import League
from ..season_type import SeasonType
from .sportsdb_team_model import create_sportsdb_team_model
from .sportsdb_venue_model import create_sportsdb_venue_model


def _create_sportsdb_game_model(
    session: ScrapeSession,
    game: dict[str, Any],
    week_number: int,
    game_number: int,
    league: League,
    year: int | None,
    season_type: SeasonType | None,
    dt: datetime.datetime,
    version: str,
) -> GameModel:
    venue = create_sportsdb_venue_model(session, game["idVenue"], dt)
    home_score = float(game["intHomeScore"] if game["intHomeScore"] is not None else 0)
    away_score = float(game["intAwayScore"] if game["intAwayScore"] is not None else 0)
    teams = [
        create_sportsdb_team_model(
            game["idHomeTeam"],
            game["strHomeTeam"],
            home_score,
            session,
            dt,
            league,
        ),
        create_sportsdb_team_model(
            game["idAwayTeam"],
            game["strAwayTeam"],
            away_score,
            session,
            dt,
            league,
        ),
    ]
    postponed = None
    if game.get("strPostponed") == "no":
        postponed = False
    elif game.get("strPostponed") == "yes":
        postponed = True

    return GameModel(
        dt=dt,
        week=week_number,
        game_number=game_number,
        venue=venue,  # pyright: ignore
        teams=teams,  # pyright: ignore
        league=str(league),
        year=year,
        season_type=season_type,
        end_dt=None,
        attendance=None,
        postponed=postponed,
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        version=version,
        umpires=[],
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_sportsdb_game_model(
    session: ScrapeSession,
    game: dict[str, Any],
    week_number: int,
    game_number: int,
    league: League,
    year: int | None,
    season_type: SeasonType | None,
    dt: datetime.datetime,
    version: str,
) -> GameModel:
    return _create_sportsdb_game_model(
        session=session,
        game=game,
        week_number=week_number,
        game_number=game_number,
        league=league,
        year=year,
        season_type=season_type,
        dt=dt,
        version=version,
    )


def create_sportsdb_game_model(
    session: ScrapeSession,
    game: dict[str, Any],
    week_number: int,
    game_number: int,
    league: League,
    year: int | None,
    season_type: SeasonType | None,
) -> GameModel | None:
    """Create a SportsDB game model."""
    if isinstance(game, str):
        return None

    try:
        ts = game["strTimestamp"]
        if ts is None:
            return None
        if ts.endswith("T"):
            ts += "00:00:00"
        dt = datetime.datetime.fromisoformat(ts)
    except TypeError:
        dt = parser.parse(game["dateEvent"])
    if dt > datetime.datetime.now().replace(tzinfo=dt.tzinfo):
        return None

    if not pytest_is_running.is_running() and dt < datetime.datetime.now().replace(
        tzinfo=dt.tzinfo
    ) - datetime.timedelta(days=7):
        return _cached_create_sportsdb_game_model(
            session=session,
            game=game,
            week_number=week_number,
            game_number=game_number,
            league=league,
            year=year,
            season_type=season_type,
            dt=dt,
            version=VERSION,
        )
    with session.cache_disabled():
        return _create_sportsdb_game_model(
            session=session,
            game=game,
            week_number=week_number,
            game_number=game_number,
            league=league,
            year=year,
            season_type=season_type,
            dt=dt,
            version=VERSION,
        )
