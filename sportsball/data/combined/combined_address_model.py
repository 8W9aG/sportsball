"""Combined address model."""

from ..address_model import VERSION, AddressModel
from .combined_weather_model import create_combined_weather_model
from .most_interesting import more_interesting
from .null_check import is_null


def create_combined_address_model(
    address_models: list[AddressModel],
) -> AddressModel | None:
    """Create a address model by combining many address models."""
    if not address_models:
        return None
    latitude = None
    longitude = None
    housenumber = None
    weather_models = []
    altitude = None
    for address_model in address_models:
        latitude = more_interesting(latitude, address_model.latitude)
        longitude = more_interesting(longitude, address_model.longitude)
        housenumber = more_interesting(housenumber, address_model.housenumber)
        address_model_weather = address_model.weather
        if not is_null(address_model_weather):
            weather_models.append(address_model_weather)
        altitude = more_interesting(altitude, address_model.altitude)
    return AddressModel.model_construct(
        city=address_models[0].city,
        state=address_models[0].state,
        zipcode=address_models[0].zipcode,
        latitude=latitude,
        longitude=longitude,
        housenumber=housenumber,
        weather=create_combined_weather_model(weather_models),  # type: ignore
        timezone=address_models[0].timezone,
        country=address_models[0].country,
        altitude=altitude,
        version=VERSION,
    )
