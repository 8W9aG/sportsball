"""Combined venue model."""

import requests

from ..venue_model import VenueModel
from ..wikipedia.wikipedia_venue_model import create_wikipedia_venue_model
from .combined_address_model import create_combined_address_model


def create_combined_venue_model(
    venue_models: list[VenueModel],
    identifier: str | None,
    session: requests.Session,
) -> VenueModel | None:
    """Create a venue model by combining many venue models."""
    if not venue_models or identifier is None:
        return None
    wikipedia_venue_model = create_wikipedia_venue_model(session, identifier)
    if wikipedia_venue_model is not None:
        venue_models.append(wikipedia_venue_model)

    address_models = []
    is_grass = None
    is_indoor = None
    for venue_model in venue_models:
        venue_model_address = venue_model.address
        if venue_model_address is not None:
            address_models.append(venue_model_address)
        venue_model_is_grass = venue_model.is_grass
        if venue_model_is_grass is not None:
            is_grass = venue_model_is_grass
        venue_model_is_indoor = venue_model.is_indoor
        if venue_model_is_indoor is not None:
            is_indoor = venue_model_is_indoor
    return VenueModel(
        identifier=identifier,
        name=venue_models[0].name,
        address=create_combined_address_model(address_models),  # pyright: ignore
        is_grass=is_grass,
        is_indoor=is_indoor,
    )
