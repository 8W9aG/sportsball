"""A class for holding address information."""

import datetime
from typing import Any, Dict, Optional, Pattern, Union

import pandas as pd
import requests_cache

from .columns import (CATEGORICAL_COLUMNS_ATTR, COLUMN_SEPARATOR,
                      update_columns_list)
from .model import Model

ADDRESS_COLUMN_SUFFIX = "address"
CITY_COLUMN = "city"
STATE_COLUMN = "state"
ZIPCODE_COLUMN = "zipcode"


class AddressModel(Model):
    """The class for representing an address."""

    def __init__(
        self, session: requests_cache.CachedSession, city: str, state: str, zipcode: str
    ) -> None:
        super().__init__(session)
        self._city = city
        self._state = state
        self._zipcode = zipcode

    @property
    def city(self) -> str:
        """Return the city."""
        return self._city

    @property
    def state(self) -> str:
        """Return the state."""
        return self._state

    @property
    def zipcode(self) -> str:
        """Return the zipcode."""
        return self._zipcode

    def to_frame(self) -> pd.DataFrame:
        """Render the address as a dataframe."""
        data = {
            CITY_COLUMN: [self.city],
            STATE_COLUMN: [self.state],
            ZIPCODE_COLUMN: [self.zipcode],
        }
        df = pd.DataFrame(
            data={
                ADDRESS_COLUMN_SUFFIX + COLUMN_SEPARATOR + k: v for k, v in data.items()
            }
        )
        df.attrs[CATEGORICAL_COLUMNS_ATTR] = list(
            set(
                update_columns_list(
                    [CITY_COLUMN, STATE_COLUMN, ZIPCODE_COLUMN], ADDRESS_COLUMN_SUFFIX
                )
            )
        )
        return df

    @staticmethod
    def urls_expire_after() -> (
        Dict[
            Union[str, Pattern[Any]],
            Optional[Union[int, float, str, datetime.datetime, datetime.timedelta]],
        ]
    ):
        """Report any cache rules."""
        return {}
