"""The prototype class for a game."""

import datetime
from typing import Literal

import pytz
from pydantic import BaseModel, ConfigDict, Field

from .delimiter import DELIMITER
from .dividend_model import DividendModel
from .field_type import TYPE_KEY, FieldType
from .season_type import SeasonType
from .team_model import VERSION as TEAM_VERSION
from .team_model import TeamModel
from .umpire_model import VERSION as UMPIRE_VERSION
from .umpire_model import UmpireModel
from .venue_model import VERSION as VENUE_VERSION
from .venue_model import VenueModel

GAME_DT_COLUMN = "dt"
SEASON_TYPE_COLUMN = "season_type"
SEASON_YEAR_COLUMN = "year"
VENUE_COLUMN_PREFIX: Literal["venue"] = "venue"
TEAM_COLUMN_PREFIX: Literal["teams"] = "teams"
GAME_ATTENDANCE_COLUMN: Literal["attendance"] = "attendance"
GAME_WEEK_COLUMN: Literal["week"] = "week"
LEAGUE_COLUMN: Literal["league"] = "league"
END_DT_COLUMN: Literal["end_dt"] = "end_dt"
POSTPONED_COLUMN: Literal["postponed"] = "postponed"
PLAY_OFF_COLUMN: Literal["play_off"] = "play_off"
GAME_DISTANCE_COLUMN: Literal["distance"] = "distance"
GAME_DIVIDENDS_COLUMN: Literal["dividends"] = "dividends"
GAME_POT_COLUMN: Literal["pot"] = "pot"
GAME_UMPIRES_COLUMN: Literal["umpires"] = "umpires"
VERSION = DELIMITER.join(["0.0.1", VENUE_VERSION, TEAM_VERSION, UMPIRE_VERSION])


def localize(venue: VenueModel | None, dt: datetime.datetime) -> datetime.datetime:
    """Localize the datetime against the timezone of the venue."""
    if dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None:
        return dt
    tz = None
    venue_model = venue
    if venue_model is not None:
        address = venue_model.address
        if address is not None:
            timezone = address.timezone
            if timezone is not None:
                tz = pytz.timezone(timezone)
    if tz is None:
        tz = pytz.utc
    return tz.localize(dt)


class GameModel(BaseModel):
    """The serialisable representation of a game."""

    model_config = ConfigDict(
        validate_assignment=False,
        revalidate_instances="never",
        extra="ignore",
        from_attributes=False,
    )

    dt: datetime.datetime
    week: int | None = Field(..., alias=GAME_WEEK_COLUMN)
    game_number: int | None
    venue: VenueModel | None = Field(..., alias=VENUE_COLUMN_PREFIX)
    teams: list[TeamModel] = Field(..., alias=TEAM_COLUMN_PREFIX)
    end_dt: datetime.datetime | None = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD}, alias=END_DT_COLUMN
    )
    attendance: int | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=GAME_ATTENDANCE_COLUMN,
    )
    league: str = Field(..., alias=LEAGUE_COLUMN)
    year: int | None
    season_type: SeasonType | None
    postponed: bool | None = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD}, alias=POSTPONED_COLUMN
    )
    play_off: bool | None = Field(..., alias=PLAY_OFF_COLUMN)
    distance: float | None = Field(..., alias=GAME_DISTANCE_COLUMN)
    dividends: list[DividendModel] = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD},
        alias=GAME_DIVIDENDS_COLUMN,
    )
    pot: float | None = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.LOOKAHEAD}, alias=GAME_POT_COLUMN
    )
    version: str = Field(..., json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL})
    umpires: list[UmpireModel] = Field(
        ...,
        alias=GAME_UMPIRES_COLUMN,
    )
