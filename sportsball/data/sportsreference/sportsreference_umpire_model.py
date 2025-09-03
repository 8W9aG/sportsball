"""Sports Reference umpire model."""

# pylint: disable=too-many-locals,too-many-branches
import datetime
import logging
import os
from urllib.parse import urlparse

import pytest_is_running
from bs4 import BeautifulSoup
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from scrapesession.scrapesession import ScrapeSession  # type: ignore

from ...cache import MEMORY
from ..google.address_exception import AddressException
from ..google.google_address_model import create_google_address_model
from ..umpire_model import VERSION, UmpireModel
from .sportsreference_venue_model import create_sportsreference_venue_model


def _create_sportsreference_umpire_model(
    url: str,
    session: ScrapeSession,
    dt: datetime.datetime,
    version: str,
) -> UmpireModel:
    response = session.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    name = None
    for h1 in soup.find_all("h1"):
        for span in h1.find_all("span"):
            name = span.get_text().strip()
            break
        if name is not None:
            break

    if name is None:
        for h1 in soup.find_all("h1"):
            name = h1.get_text().strip()

    if name is None:
        logging.error(response.text)
        logging.error("error url = %s", url)
        raise ValueError("name is null")

    o = urlparse(url)
    last_component = o.path.split("/")[-1]
    identifier, _ = os.path.splitext(last_component)

    birth_date = None
    for span in soup.find_all("span", {"id": "necro-birth"}):
        birth_date = parse(span.get("data-birth"))

    birth_address = None
    for p in soup.find_all("p"):
        p_text = p.get_text().strip()
        if "Born:" not in p_text:
            continue
        address_text = p_text.split("in ")[-1].strip().split("College:")[0].strip()
        try:
            birth_address = create_google_address_model(
                query=address_text, session=session, dt=None
            )
        except AddressException as exc:
            logging.warning("Failed to find birth address: %s", str(exc))
        break

    high_school = None
    for p in soup.find_all("p"):
        p_text = p.get_text().strip()
        if "High School:" not in p_text:
            continue
        address_text = p_text.split("in ")[-1].strip().split("College:")[0].strip()
        try:
            high_school = create_sportsreference_venue_model(
                venue_name=address_text, session=session, dt=None
            )
        except AddressException as exc:
            logging.warning("Failed to find high school: %s", str(exc))
        break

    return UmpireModel(
        identifier=identifier,
        name=name,
        birth_date=birth_date,
        age=None if birth_date is None else relativedelta(birth_date, dt).years,
        birth_address=birth_address,
        high_school=high_school,
        version=version,
    )


@MEMORY.cache(ignore=["session"])
def _cached_create_sportsreference_umpire_model(
    url: str,
    session: ScrapeSession,
    dt: datetime.datetime,
    version: str,
) -> UmpireModel:
    return _create_sportsreference_umpire_model(
        url=url, session=session, dt=dt, version=version
    )


def create_sportsreference_umpire_model(
    url: str,
    session: ScrapeSession,
    dt: datetime.datetime,
) -> UmpireModel:
    """Create a sports reference umpire model."""
    if not pytest_is_running.is_running():
        return _cached_create_sportsreference_umpire_model(
            url=url, session=session, dt=dt, version=VERSION
        )
    with session.cache_disabled():
        return _create_sportsreference_umpire_model(
            url=url, session=session, dt=dt, version=VERSION
        )
