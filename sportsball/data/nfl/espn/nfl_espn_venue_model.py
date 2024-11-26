"""NFL venue model."""

import datetime
from typing import Any, Dict, Optional, Pattern, Union

import requests_cache

from ...address_model import AddressModel
from ...venue_model import VenueModel


class NFLESPNVenueModel(VenueModel):
    """NFL implementation of the venue model."""

    def __init__(
        self, session: requests_cache.CachedSession, venue: Dict[str, Any]
    ) -> None:
        super().__init__(session)
        self._identifier = venue["id"]
        self._name = venue["fullName"]
        venue_address = venue["address"]
        city = venue_address["city"]
        state = venue_address["state"]
        zipcode = venue_address["zipCode"]
        self._address = AddressModel(session, city, state, zipcode)

    @property
    def identifier(self) -> str:
        """Return the venue ID."""
        return self._identifier

    @property
    def name(self) -> str:
        """Return the venue name."""
        return self._name

    @property
    def address(self) -> AddressModel | None:
        """Return the venue address."""
        return self._address

    @staticmethod
    def urls_expire_after() -> (
        Dict[
            Union[str, Pattern[Any]],
            Optional[Union[int, float, str, datetime.datetime, datetime.timedelta]],
        ]
    ):
        """Return the URL cache rules."""
        return AddressModel.urls_expire_after()
