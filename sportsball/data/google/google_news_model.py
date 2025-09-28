"""Google news model."""

# pylint: disable=broad-exception-caught
import datetime

import pytest_is_running
import requests_cache
from bs4 import BeautifulSoup
from dateutil import parser

from ...cache import MEMORY
from ...vendor.pygooglenews import GoogleNews  # type: ignore
from ..league import League, long_name
from ..news_model import NewsModel


def _create_google_news_models(
    query: str,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
) -> list[NewsModel]:
    gn = GoogleNews(session=session)
    to_dt = dt - datetime.timedelta(days=1)
    from_dt = to_dt - datetime.timedelta(days=1)
    if from_dt.date() >= datetime.datetime.now().date():
        from_dt = datetime.datetime.now() - datetime.timedelta(days=1)
    search_query = f'"{query}" + (sport OR {league} OR "{long_name(league)}")'
    try:
        s = gn.search(query=search_query, from_=str(from_dt), to_=str(to_dt))
        return sorted(
            [
                NewsModel(
                    title=x["title"],
                    published=parser.parse(x["published"]),
                    summary=BeautifulSoup(x["summary"], features="lxml").get_text(),
                    source=x["source"]["title"],
                )
                for x in s["entries"]
            ],
            key=lambda x: x.published,
        )
    except Exception:
        return []


@MEMORY.cache(ignore=["session"])
def _cached_create_google_news_models(
    query: str,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
) -> list[NewsModel]:
    return _create_google_news_models(query, session, dt, league)


def create_google_news_models(
    query: str,
    session: requests_cache.CachedSession,
    dt: datetime.datetime,
    league: League,
) -> list[NewsModel]:
    """Create news models from google."""
    if dt > datetime.datetime.now().replace(tzinfo=dt.tzinfo) + datetime.timedelta(
        days=1
    ):
        return []
    if not pytest_is_running.is_running() and dt < datetime.datetime.now().replace(
        tzinfo=dt.tzinfo
    ) - datetime.timedelta(days=3):
        return _cached_create_google_news_models(query, session, dt, league)
    with session.cache_disabled():
        return _create_google_news_models(query, session, dt, league)
