"""The prototype class for an owner."""

# pylint: disable=duplicate-code
from typing import Any, Literal

from pydantic import BaseModel, Field

from .field_type import FFILL_KEY, TYPE_KEY, FieldType
from .sex import (FEMALE_GENDERS, GENDER_DETECTOR, MALE_GENDERS,
                  UNCERTAIN_GENDERS, Sex)

OWNER_IDENTIFIER_COLUMN: Literal["identifier"] = "identifier"
OWNER_NAME_COLUMN: Literal["name"] = "name"
OWNER_SEX_COLUMN: Literal["sex"] = "sex"
VERSION = "0.0.1"


def _guess_sex(data: dict[str, Any]) -> str | None:
    name = data[OWNER_NAME_COLUMN]
    gender_tag = GENDER_DETECTOR.get_gender(name)
    if gender_tag in MALE_GENDERS:
        return str(Sex.MALE)
    if gender_tag in FEMALE_GENDERS:
        return str(Sex.FEMALE)
    if gender_tag in UNCERTAIN_GENDERS:
        return None
    return None


class OwnerModel(BaseModel):
    """The serialisable owner class."""

    identifier: str = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=OWNER_IDENTIFIER_COLUMN,
    )
    name: str = Field(..., alias=OWNER_NAME_COLUMN)
    sex: str | None = Field(
        default_factory=_guess_sex,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL, FFILL_KEY: True},
        alias=OWNER_SEX_COLUMN,
    )
    version: str
