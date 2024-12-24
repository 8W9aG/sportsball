"""Combined game model."""

# pylint: disable=too-many-locals
import datetime
import logging
from typing import Callable

import requests

from ..game_model import GameModel
from ..odds_model import OddsModel
from ..team_model import TeamModel
from ..venue_model import VenueModel
from .combined_team_model import create_combined_team_model
from .combined_venue_model import create_combined_venue_model


def _venue_models(
    game_models: list[GameModel], venue_identity_map: dict[str, str]
) -> tuple[list[VenueModel], str | None]:
    venue_models = []
    full_venue_identity = None
    for game_model in game_models:
        game_model_venue = game_model.venue
        if game_model_venue is not None:
            venue_identity = venue_identity_map.get(game_model_venue.identifier)
            if venue_identity is None:
                logging.warning("Failed to find %s venue identifier.", venue_identity)
            else:
                full_venue_identity = venue_identity
            venue_models.append(game_model_venue)
    return venue_models, full_venue_identity


def _team_models(
    game_models: list[GameModel],
    team_identity_map: dict[str, str],
    odds_factory: Callable[[requests.Session, datetime.datetime, str], OddsModel]
    | None,
    session: requests.Session,
) -> list[TeamModel]:
    team_models: dict[str, list[TeamModel]] = {}
    for game_model in game_models:
        game_model_teams = game_model.teams
        if game_model_teams:
            for team_model in game_model_teams:
                team_identity = team_identity_map.get(team_model.identifier)
                if team_identity is None:
                    logging.warning("Failed to find %s team identifier.", team_identity)
                    team_identity = team_model.identifier
                team_models[team_identity] = team_models.get(team_identity, []) + [
                    team_model
                ]
    return [
        create_combined_team_model(v, k, odds_factory, session, game_models[0].dt)
        for k, v in team_models.items()
    ]


def create_combined_game_model(
    game_models: list[GameModel],
    venue_identity_map: dict[str, str],
    team_identity_map: dict[str, str],
    odds_factory: Callable[[requests.Session, datetime.datetime, str], OddsModel]
    | None,
    session: requests.Session,
) -> GameModel:
    """Create a game model by combining many game models."""
    venue_models, full_venue_identity = _venue_models(game_models, venue_identity_map)
    full_team_models = _team_models(
        game_models, team_identity_map, odds_factory, session
    )
    attendance = None
    end_dt = None
    year = None
    season_type = None
    for game_model in game_models:
        game_model_attendance = game_model.attendance
        if game_model_attendance is not None:
            attendance = game_model_attendance
        game_model_end_dt = game_model.end_dt
        if game_model_end_dt is not None:
            end_dt = game_model_end_dt
        game_model_year = game_model.year
        if game_model_year is not None:
            year = game_model_year
        game_model_season_type = game_model.season_type
        if game_model_season_type is not None:
            season_type = game_model_season_type

    if full_venue_identity is None and venue_models:
        full_venue_identity = venue_models[0].identifier
    if full_venue_identity is None:
        raise ValueError("full_venue_identity is null.")

    return GameModel(
        dt=game_models[0].dt,
        week=game_models[0].week,
        game_number=game_models[0].game_number,
        venue=create_combined_venue_model(venue_models, full_venue_identity),
        teams=full_team_models,
        end_dt=end_dt,
        attendance=attendance,
        league=game_models[0].league,
        year=year,
        season_type=season_type,
    )
