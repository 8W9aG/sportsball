"""The prototype class for news."""

import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from .field_type import TYPE_KEY, FieldType

NEWS_SUMMARY_COLUMN: Literal["summary"] = "summary"
NEWS_TITLE_COLUMN: Literal["title"] = "title"
NEWS_PUBLISHED_COLUMN: Literal["published"] = "published"
NEWS_SOURCE_COLUMN: Literal["source"] = "source"


class NewsModel(BaseModel):
    """The serialisable news class."""

    model_config = ConfigDict(
        validate_assignment=False,
        revalidate_instances="never",
        extra="ignore",
        from_attributes=False,
    )

    title: str = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.TEXT}, alias=NEWS_TITLE_COLUMN
    )
    published: datetime.datetime = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.DATETIME},
        alias=NEWS_PUBLISHED_COLUMN,
    )
    summary: str = Field(
        ..., json_schema_extra={TYPE_KEY: FieldType.TEXT}, alias=NEWS_SUMMARY_COLUMN
    )
    source: str = Field(
        ...,
        json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL},
        alias=NEWS_SOURCE_COLUMN,
    )
