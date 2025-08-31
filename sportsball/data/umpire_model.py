"""The prototype class for an umpire."""

# pylint: disable=duplicate-code
import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from .address_model import VERSION as ADDRESS_VERSION
from .address_model import AddressModel
from .delimiter import DELIMITER
from .field_type import FFILL_KEY, TYPE_KEY, FieldType
from .sex import (FEMALE_GENDERS, GENDER_DETECTOR, MALE_GENDERS,
                  UNCERTAIN_GENDERS, Sex)
from .venue_model import VERSION as VENUE_VERSION
from .venue_model import VenueModel

UMPIRE_IDENTIFIER_COLUMN: Literal["identifier"] = "identifier"
UMPIRE_NAME_COLUMN: Literal["name"] = "name"
UMPIRE_SEX_COLUMN: Literal["sex"] = "sex"
UMPIRE_BIRTH_DATE_COLUMN: Literal["birth_date"] = "birth_date"
UMPIRE_AGE_COLUMN: Literal["age"] = "age"
UMPIRE_BIRTH_ADDRESS_COLUMN: Literal["birth_address"] = "birth_address"
UMPIRE_HIGH_SCHOOL_COLUMN: Literal["high_school"] = "high_school"
VERSION = DELIMITER.join(["0.0.1", ADDRESS_VERSION, VENUE_VERSION])


def _guess_sex(data: dict[str, Any]) -> str | None:
    name = data[UMPIRE_NAME_COLUMN]
    gender_tag = GENDER_DETECTOR.get_gender(name)
    if gender_tag in MALE_GENDERS:
        return str(Sex.MALE)
    if gender_tag in FEMALE_GENDERS:
        return str(Sex.FEMALE)
    if gender_tag in UNCERTAIN_GENDERS:
        return None
    return None


class UmpireModel(BaseModel):
    """The serialisable umpire class."""

    model_config = ConfigDict(
        validate_assignment=False,
        revalidate_instances="never",
        extra="ignore",
        from_attributes=False,
    )

    identifier: str = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=UMPIRE_IDENTIFIER_COLUMN,
    )
    name: str = Field(..., alias=UMPIRE_NAME_COLUMN)
    sex: str | None = Field(
        default_factory=_guess_sex,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL, FFILL_KEY: True},
        alias=UMPIRE_SEX_COLUMN,
    )
    birth_date: datetime.date | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=UMPIRE_BIRTH_DATE_COLUMN
    )
    age: int | None = Field(..., alias=UMPIRE_AGE_COLUMN)
    birth_address: AddressModel | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=UMPIRE_BIRTH_ADDRESS_COLUMN
    )
    high_school: VenueModel | None = Field(
        ..., json_schema_extra={FFILL_KEY: True}, alias=UMPIRE_HIGH_SCHOOL_COLUMN
    )
    version: str = Field(..., json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL})
