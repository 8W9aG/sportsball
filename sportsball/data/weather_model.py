"""A class for holding weather information."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from .field_type import TYPE_KEY, FieldType

VERSION: Literal["0.0.1"] = "0.0.1"


class WeatherModel(BaseModel):
    """The serialisable class for representing weather."""

    model_config = ConfigDict(
        validate_assignment=False,
        revalidate_instances="never",
        extra="ignore",
        from_attributes=False,
    )

    temperature: float | None
    relative_humidity: float | None
    dew_point: float | None
    apparent_temperature: float | None
    precipitation_probability: float | None
    precipitation: float | None
    rain: float | None
    showers: float | None
    snowfall: float | None
    snow_depth: float | None
    weather_code: float | None
    sealevel_pressure: float | None
    surface_pressure: float | None
    cloud_cover_total: float | None
    cloud_cover_low: float | None
    cloud_cover_mid: float | None
    cloud_cover_high: float | None
    visibility: float | None
    evapotranspiration: float | None
    reference_evapotranspiration: float | None
    vapour_pressure_deficit: float | None
    wind_speed_10m: float | None
    wind_speed_80m: float | None
    wind_speed_120m: float | None
    wind_speed_180m: float | None
    wind_direction_10m: float | None
    wind_direction_80m: float | None
    wind_direction_120m: float | None
    wind_direction_180m: float | None
    wind_gusts: float | None
    temperature_80m: float | None
    temperature_120m: float | None
    temperature_180m: float | None
    soil_temperature_0cm: float | None
    soil_temperature_6cm: float | None
    soil_temperature_18cm: float | None
    soil_temperature_54cm: float | None
    soil_moisture_0cm: float | None
    soil_moisture_1cm: float | None
    soil_moisture_3cm: float | None
    soil_moisture_9cm: float | None
    soil_moisture_27cm: float | None
    daily_weather_code: float | None
    daily_maximum_temperature_2m: float | None
    daily_minimum_temperature_2m: float | None
    daily_maximum_apparent_temperature_2m: float | None
    daily_minimum_apparent_temperature_2m: float | None
    sunrise: float | None
    sunset: float | None
    daylight_duration: float | None
    sunshine_duration: float | None
    uv_index: float | None
    uv_index_clear_sky: float | None
    rain_sum: float | None
    showers_sum: float | None
    snowfall_sum: float | None
    precipitation_sum: float | None
    precipitation_hours: float | None
    precipitation_probability_max: float | None
    maximum_wind_speed_10m: float | None
    maximum_wind_gusts_10m: float | None
    dominant_wind_direction: float | None
    shortwave_radiation_sum: float | None
    daily_reference_evapotranspiration: float | None
    version: str = Field(..., json_schema_extra={TYPE_KEY: FieldType.CATEGORICAL})
