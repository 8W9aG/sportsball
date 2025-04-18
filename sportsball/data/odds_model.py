"""The prototype class for odds."""

import datetime
from typing import Literal

from pydantic import BaseModel, Field

from .bookie_model import BookieModel
from .field_type import TYPE_KEY, FieldType

DT_COLUMN: Literal["dt"] = "dt"
ODDS_ODDS_COLUMN: Literal["odds"] = "odds"
ODDS_BOOKIE_COLUMN: Literal["bookie"] = "bookie"


class OddsModel(BaseModel):
    """The serialisable odds class."""

    odds: float = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.ODDS}, alias=ODDS_ODDS_COLUMN
    )
    bookie: BookieModel = Field(..., alias=ODDS_BOOKIE_COLUMN)
    dt: datetime.datetime | None = Field(
        ...,
        alias=DT_COLUMN,
    )
