"""OddsPortal game model."""

# pylint: disable=too-many-locals,too-many-statements,line-too-long,broad-exception-caught,duplicate-code
import datetime
import json
import logging
import urllib.parse

import pytest_is_running
from bs4 import BeautifulSoup, Tag
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..game_model import VERSION, GameModel
from ..league import League
from .decrypt import fetch_data
from .oddsportal_team_model import create_oddsportal_team_model
from .oddsportal_venue_model import create_oddsportal_venue_model


def _create_oddsportal_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    version: str,
) -> GameModel | None:
    with session.wayback_disabled():
        response = session.get(
            url,
        )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    event_tag = soup.find("div", id="react-event-header")
    if not isinstance(event_tag, Tag):
        soup_x = BeautifulSoup(response.text, "xml")
        event_tag = soup_x.find("Event")
        if not isinstance(event_tag, Tag):
            logging.error("event_tag is not a tag for URL: %s.", url)
            return None
        event = json.loads(str(event_tag[":data"]))
    else:
        event = json.loads(str(event_tag["data"]))

    event_body = event["eventBody"]
    event_data = event["eventData"]
    dt = datetime.datetime.fromtimestamp(event_body["startDate"])
    end_dt = None
    if event_body.get("endDate", False) is not False:
        end_dt = datetime.datetime.fromtimestamp(event_body["endDate"])
    version_id = str(event_data["versionId"])
    sport_id = str(event_data["sportId"])
    unique_id = event_data["id"]
    default_bet_id = str(event_data["defaultBetId"])
    default_scope_id = str(event_data["defaultScopeId"])
    xhash = urllib.parse.unquote(event_data["xhash"])

    bookie_names = event_body["providersNames"]
    home_points = None
    if event_body["homeResult"] != "":
        home_points = float(event_body["homeResult"])
    away_points = None
    if event_body["awayResult"] != "":
        away_points = float(event_body["awayResult"])

    venue = None
    if (
        event_body.get("venue", "")
        and event_body.get("venueTown", "")
        and event_body.get("venueCountry", "")
    ):
        venue = create_oddsportal_venue_model(
            session,
            dt,
            event_body["venue"],
            event_body["venueTown"],
            event_body["venueCountry"],
        )

    dat_url = f"https://www.oddsportal.com/match-event/{version_id}-{sport_id}-{unique_id}-{default_bet_id}-{default_scope_id}-{xhash}.dat"
    try:
        parsed_data = fetch_data(dat_url, session, url, soup)
    except Exception:
        return None

    return GameModel(
        dt=dt,
        week=None,
        game_number=None,
        venue=venue,
        teams=[
            create_oddsportal_team_model(
                session,
                dt,
                event_data["home"],
                league,
                home_points,
                default_bet_id,
                default_scope_id,
                bookie_names,
                0,
                parsed_data,
            ),
            create_oddsportal_team_model(
                session,
                dt,
                event_data["away"],
                league,
                away_points,
                default_bet_id,
                default_scope_id,
                bookie_names,
                1,
                parsed_data,
            ),
        ],
        end_dt=end_dt,
        attendance=None,
        league=str(league),
        year=dt.year,
        season_type=None,
        postponed=event_data["isPostponed"],
        play_off=None,
        distance=None,
        dividends=[],
        pot=None,
        version=version,
        umpires=[],
        best_of=None,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_oddsportal_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    version: str,
) -> GameModel | None:
    return _create_oddsportal_game_model(
        session=session, url=url, league=league, version=version
    )


def create_oddsportal_game_model(
    session: ScrapeSession,
    url: str,
    league: League,
    is_next: bool,
) -> GameModel | None:
    """Create a OddsPortal game model."""
    if not pytest_is_running.is_running() and not is_next:
        return _cached_create_oddsportal_game_model(
            session=session, url=url, league=league, version=VERSION
        )
    with session.cache_disabled():
        return _create_oddsportal_game_model(
            session=session, url=url, league=league, version=VERSION
        )
