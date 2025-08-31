"""The prototype class for a coach."""

import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from .field_type import FFILL_KEY, TYPE_KEY, FieldType
from .sex import (FEMALE_GENDERS, GENDER_DETECTOR, MALE_GENDERS,
                  UNCERTAIN_GENDERS, Sex)

COACH_IDENTIFIER_COLUMN: Literal["identifier"] = "identifier"
COACH_NAME_COLUMN: Literal["name"] = "name"
COACH_BIRTH_DATE_COLUMN: Literal["birth_date"] = "birth_date"
COACH_AGE_COLUMN: Literal["age"] = "age"
COACH_SEX_COLUMN: Literal["sex"] = "sex"
VERSION = "0.0.1"


def _guess_sex(data: dict[str, Any]) -> str | None:
    name = data[COACH_NAME_COLUMN]
    gender_tag = GENDER_DETECTOR.get_gender(name)
    if gender_tag in MALE_GENDERS:
        return str(Sex.MALE)
    if gender_tag in FEMALE_GENDERS:
        return str(Sex.FEMALE)
    if gender_tag in UNCERTAIN_GENDERS:
        return None
    return None


class CoachModel(BaseModel):
    """The serialisable coach class."""

    model_config = ConfigDict(
        validate_assignment=False,
        revalidate_instances="never",
        extra="ignore",
        from_attributes=False,
    )

    identifier: str = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=COACH_IDENTIFIER_COLUMN,
    )
    name: str = Field(..., alias=COACH_NAME_COLUMN)
    birth_date: datetime.date | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=COACH_BIRTH_DATE_COLUMN
    )
    age: int | None = Field(..., alias=COACH_AGE_COLUMN)
    version: str = Field(..., json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL})
    sex: str | None = Field(
        default_factory=_guess_sex,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL, FFILL_KEY: True},
        alias=COACH_SEX_COLUMN,
    )
