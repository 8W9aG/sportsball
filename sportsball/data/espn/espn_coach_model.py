"""ESPN coach model."""

import datetime
from typing import Any

import pytest_is_running
import requests_cache

from ...cache import MEMORY
from ..coach_model import VERSION, CoachModel


def _create_espn_coach_model(
    session: requests_cache.CachedSession,
    url: str,
    version: str,
) -> dict[str, Any]:
    response = session.get(url)
    response.raise_for_status()
    data = response.json()
    return CoachModel(
        identifier=data["id"],
        name=" ".join([data["firstName"], data["lastName"]]),
        birth_date=None,
        age=None,
        version=version,
    ).model_dump()


@MEMORY.cache(ignore=["session"])
def _cached_create_espn_coach_model(
    session: requests_cache.CachedSession,
    url: str,
    version: str,
) -> dict[str, Any]:
    return _create_espn_coach_model(session=session, url=url, version=version)


def create_espn_coach_model(
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    url: str,
) -> CoachModel:
    """Create coach model from ESPN."""
    if (
        not pytest_is_running.is_running()
        and dt.date() < datetime.datetime.today().date() - datetime.timedelta(days=7)
    ):
        return CoachModel.model_construct(
            **_cached_create_espn_coach_model(session=session, url=url, version=VERSION)
        )
    with session.cache_disabled():
        return CoachModel.model_construct(
            **_create_espn_coach_model(session=session, url=url, version=VERSION)
        )
