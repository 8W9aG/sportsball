"""Footballdata umpire model."""

# pylint: disable=too-many-arguments
from ...cache import MEMORY
from ..umpire_model import UmpireModel


@MEMORY.cache
def create_footballdata_umpire_model(
    name: str,
    version: str,
) -> UmpireModel:
    """Create a umpire model based off footballdata."""
    return UmpireModel(
        identifier=name,
        name=name,
        birth_date=None,
        age=None,
        birth_address=None,
        high_school=None,
        version=version,
    )
