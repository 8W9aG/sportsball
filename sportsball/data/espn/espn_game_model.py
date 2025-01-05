"""ESPN game model."""

# pylint: disable=too-many-arguments
import datetime
from typing import Any, Dict

import requests
from dateutil.parser import parse

from ...cache import MEMORY
from ..game_model import GameModel, localize
from ..league import League
from ..odds_model import OddsModel
from ..season_type import SeasonType
from ..team_model import TeamModel
from ..venue_model import VenueModel
from .espn_bookie_model import create_espn_bookie_model
from .espn_odds_model import MONEYLINE_KEY, create_espn_odds_model
from .espn_team_model import create_espn_team_model
from .espn_venue_model import create_espn_venue_model


def _create_espn_team(
    competitor: Dict[str, Any],
    odds_dict: Dict[str, Any],
    session: requests.Session,
) -> TeamModel:
    team_response = session.get(competitor["team"]["$ref"])
    team_response.raise_for_status()
    team_dict = team_response.json()

    odds_key = competitor["homeAway"] + "TeamOdds"
    odds: list[OddsModel] = []
    if odds_dict:
        odds = [  # pyright: ignore
            create_espn_odds_model(
                x[odds_key],
                create_espn_bookie_model(x["provider"]),
            )
            for x in odds_dict["items"]
            if odds_key in x and MONEYLINE_KEY in x[odds_key]
        ]

    roster_dict = {}
    if "roster" in competitor:
        roster_response = session.get(competitor["roster"]["$ref"])
        roster_response.raise_for_status()
        roster_dict = roster_response.json()

    score_response = session.get(competitor["score"]["$ref"])
    score_response.raise_for_status()
    score_dict = score_response.json()

    return create_espn_team_model(
        session,
        team_dict,
        roster_dict,
        odds,
        score_dict,
    )


def _create_venue(
    event: dict[str, Any], session: requests.Session, dt: datetime.datetime
) -> VenueModel | None:
    venue = None
    if "venue" in event:
        venue = create_espn_venue_model(event["venue"], session, dt)
    if venue is None and "venues" in event:
        venues = event["venues"]
        if venues:
            venue_url = event["venues"][0]["$ref"]
            venue_response = session.get(venue_url)
            venue_response.raise_for_status()
            venue = create_espn_venue_model(venue_response.json(), session, dt)
    return venue  # pyright: ignore


def _create_teams(
    event: dict[str, Any], session: requests.Session, venue: VenueModel | None
) -> tuple[list[TeamModel], int | None, datetime.datetime | None]:
    teams = []
    attendance = None
    end_dt = None
    for competition in event["competitions"]:
        odds_dict = {}
        if "odds" in competition:
            odds_response = session.get(competition["odds"]["$ref"])
            odds_response.raise_for_status()
            odds_dict = odds_response.json()

        for competitor in competition["competitors"]:
            teams.append(_create_espn_team(competitor, odds_dict, session))
        attendance = competition["attendance"]
        if "situation" in competition:
            situation_url = competition["situation"]["$ref"]
            situation_response = session.get(situation_url)
            situation_response.raise_for_status()
            situation = situation_response.json()
            if "lastPlay" in situation:
                last_play_response = session.get(situation["lastPlay"]["$ref"])
                last_play_response.raise_for_status()
                last_play = last_play_response.json()
                if "wallclock" in last_play:
                    end_dt = parse(last_play["wallclock"])
        if venue is not None and end_dt is not None:
            end_dt = localize(venue, end_dt)
    return teams, attendance, end_dt


@MEMORY.cache(ignore=["session"])
def create_espn_game_model(
    event: dict[str, Any],
    week: int,
    game_number: int,
    session: requests.Session,
    league: League,
    year: int | None,
    season_type: SeasonType | None,
) -> GameModel:
    """Creates an ESPN game model."""
    dt = parse(event["date"])
    venue = _create_venue(event, session, dt)
    if venue is not None:
        dt = localize(venue, dt)
    teams, attendance, end_dt = _create_teams(event, session, venue)
    return GameModel(
        dt=dt,
        week=week,
        game_number=game_number,
        venue=venue,
        teams=teams,
        end_dt=end_dt,
        attendance=attendance,
        league=league,
        year=year,
        season_type=season_type,
    )
