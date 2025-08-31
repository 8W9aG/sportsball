"""The prototype class for odds."""

import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from .bookie_model import BookieModel
from .field_type import TYPE_KEY, FieldType

DT_COLUMN: Literal["dt"] = "dt"
ODDS_ODDS_COLUMN: Literal["odds"] = "odds"
ODDS_BOOKIE_COLUMN: Literal["bookie"] = "bookie"
ODDS_CANONICAL_COLUMN: Literal["canonical"] = "canonical"
ODDS_BET_COLUMN: Literal["bet"] = "bet"


class OddsModel(BaseModel):
    """The serialisable odds class."""

    model_config = ConfigDict(
        validate_assignment=False,
        revalidate_instances="never",
        extra="ignore",
        from_attributes=False,
    )

    odds: float = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.ODDS}, alias=ODDS_ODDS_COLUMN
    )
    bookie: BookieModel = Field(..., alias=ODDS_BOOKIE_COLUMN)
    dt: datetime.datetime | None = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.DATETIME},
        alias=DT_COLUMN,
    )
    canonical: bool = Field(..., alias=ODDS_CANONICAL_COLUMN)
    bet: str = Field(..., alias=ODDS_BET_COLUMN)
