"""The prototype class for a venue."""

from typing import Literal

from pydantic import BaseModel, Field

from .address_model import AddressModel
from .field_type import TYPE_KEY, FieldType

VENUE_IDENTIFIER_COLUMN: Literal["identifier"] = "identifier"


class VenueModel(BaseModel):
    """The serialisable venue class."""

    identifier: str = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=VENUE_IDENTIFIER_COLUMN,
    )
    name: str = Field(..., json_schema_extra={TYPE_KEY: FieldType.TEXT})
    address: AddressModel | None
    is_grass: bool | None
    is_indoor: bool | None
