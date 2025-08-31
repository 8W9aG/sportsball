"""The prototype class for social."""

import datetime

from pydantic import BaseModel, ConfigDict, Field

from .field_type import TYPE_KEY, FieldType


class SocialModel(BaseModel):
    """The serialisable social class."""

    model_config = ConfigDict(
        validate_assignment=False,
        revalidate_instances="never",
        extra="ignore",
        from_attributes=False,
    )

    network: str = Field(..., json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL})
    post: str = Field(..., json_schema_extra={TYPE_KEY: FieldType.TEXT})
    comments: int
    reposts: int
    likes: int
    views: int | None
    published: datetime.datetime
