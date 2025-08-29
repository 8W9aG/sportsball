"""Openmeteo weather model."""

# pylint: disable=too-many-statements,too-many-locals,line-too-long,duplicate-code,too-many-arguments,too-many-positional-arguments
import datetime
import struct

import openmeteo_requests  # type: ignore
import pandas as pd
import pytest_is_running
import pytz
import requests
import requests_cache
from openmeteo_requests.Client import OpenMeteoRequestsError  # type: ignore
from openmeteo_requests.Client import WeatherApiResponse

from ....cache import MEMORY
from ...weather_model import VERSION, WeatherModel


def _parse_openmeteo(
    responses: list[WeatherApiResponse], tz: str, dt: datetime.datetime, version: str
) -> WeatherModel | None:
    # pylint: disable=broad-exception-caught
    if not responses:
        return None
    response = responses[0]
    try:
        hourly = response.Hourly()
        daily = response.Daily()
    except Exception:
        return None
    if hourly is None:
        raise ValueError("hourly is null.")
    if daily is None:
        raise ValueError("daily is null")
    dt_index = pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s"),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left",
        tz=tz,
    )
    try:
        row_count = min(
            len(hourly.Variables(0).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(1).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(2).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(3).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(4).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(5).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(6).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(7).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(8).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(9).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(10).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(11).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(12).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(13).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(14).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(15).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(16).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(17).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(18).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(19).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(20).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(21).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(22).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(23).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(24).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(25).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(26).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(27).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(28).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(29).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(30).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(31).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(32).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(33).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(34).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(35).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(36).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(37).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(38).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(39).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(40).ValuesAsNumpy()),  # type: ignore
            len(hourly.Variables(41).ValuesAsNumpy()),  # type: ignore
            len(dt_index),
        )
        hourly_df = pd.DataFrame(
            index=dt_index[:row_count],  # type: ignore
            data={
                "temperature_2m": hourly.Variables(0).ValuesAsNumpy()[:row_count],  # type: ignore
                "relative_humidity_2m": hourly.Variables(1).ValuesAsNumpy()[:row_count],  # type: ignore
                "dew_point_2m": hourly.Variables(2).ValuesAsNumpy()[:row_count],  # type: ignore
                "apparent_temperature": hourly.Variables(3).ValuesAsNumpy()[:row_count],  # type: ignore
                "precipitation_probability": hourly.Variables(4).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "precipitation": hourly.Variables(5).ValuesAsNumpy()[:row_count],  # type: ignore
                "rain": hourly.Variables(6).ValuesAsNumpy()[:row_count],  # type: ignore
                "showers": hourly.Variables(7).ValuesAsNumpy()[:row_count],  # type: ignore
                "snowfall": hourly.Variables(8).ValuesAsNumpy()[:row_count],  # type: ignore
                "snow_depth": hourly.Variables(9).ValuesAsNumpy()[:row_count],  # type: ignore
                "weather_code": hourly.Variables(10).ValuesAsNumpy()[:row_count],  # type: ignore
                "pressure_msl": hourly.Variables(11).ValuesAsNumpy()[:row_count],  # type: ignore
                "surface_pressure": hourly.Variables(12).ValuesAsNumpy()[:row_count],  # type: ignore
                "cloud_cover": hourly.Variables(13).ValuesAsNumpy()[:row_count],  # type: ignore
                "cloud_cover_low": hourly.Variables(14).ValuesAsNumpy()[:row_count],  # type: ignore
                "cloud_cover_mid": hourly.Variables(15).ValuesAsNumpy()[:row_count],  # type: ignore
                "cloud_cover_high": hourly.Variables(16).ValuesAsNumpy()[:row_count],  # type: ignore
                "visibility": hourly.Variables(17).ValuesAsNumpy()[:row_count],  # type: ignore
                "evapotranspiration": hourly.Variables(18).ValuesAsNumpy()[:row_count],  # type: ignore
                "reference_evapotranspiration": hourly.Variables(19).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "vapour_pressure_deficit": hourly.Variables(20).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "wind_speed_10m": hourly.Variables(21).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_speed_80m": hourly.Variables(22).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_speed_120m": hourly.Variables(23).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_speed_180m": hourly.Variables(24).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_direction_10m": hourly.Variables(25).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_direction_80m": hourly.Variables(26).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_direction_120m": hourly.Variables(27).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_direction_180m": hourly.Variables(28).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_gusts": hourly.Variables(29).ValuesAsNumpy()[:row_count],  # type: ignore
                "temperature_80m": hourly.Variables(30).ValuesAsNumpy()[:row_count],  # type: ignore
                "temperature_120m": hourly.Variables(31).ValuesAsNumpy()[:row_count],  # type: ignore
                "temperature_180m": hourly.Variables(32).ValuesAsNumpy()[:row_count],  # type: ignore
                "soil_temperature": hourly.Variables(33).ValuesAsNumpy()[:row_count],  # type: ignore
                "soil_temperature_6cm": hourly.Variables(34).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "soil_temperature_18cm": hourly.Variables(35).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "soil_temperature_54cm": hourly.Variables(36).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "soil_moisture": hourly.Variables(37).ValuesAsNumpy()[:row_count],  # type: ignore
                "soil_moisture_1cm": hourly.Variables(38).ValuesAsNumpy()[:row_count],  # type: ignore
                "soil_moisture_3cm": hourly.Variables(39).ValuesAsNumpy()[:row_count],  # type: ignore
                "soil_moisture_9cm": hourly.Variables(40).ValuesAsNumpy()[:row_count],  # type: ignore
                "soil_moisture_27cm": hourly.Variables(41).ValuesAsNumpy()[:row_count],  # type: ignore
            },
        )

        dt_index = pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s"),
            end=pd.to_datetime(daily.TimeEnd(), unit="s"),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left",
            tz=tz,
        )
        row_count = min(
            len(daily.Variables(0).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(1).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(2).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(3).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(4).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(5).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(6).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(7).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(8).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(9).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(10).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(11).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(12).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(13).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(14).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(15).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(16).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(17).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(18).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(19).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(20).ValuesAsNumpy()),  # type: ignore
            len(daily.Variables(21).ValuesAsNumpy()),  # type: ignore
            len(dt_index),
        )
        daily_df = pd.DataFrame(
            index=dt_index[:row_count],  # type: ignore
            data={
                "weather_code": daily.Variables(0).ValuesAsNumpy()[:row_count],  # type: ignore
                "temperature_2m_max": daily.Variables(1).ValuesAsNumpy()[:row_count],  # type: ignore
                "temperature_2m_min": daily.Variables(2).ValuesAsNumpy()[:row_count],  # type: ignore
                "apparent_temperature_max": daily.Variables(3).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "apparent_temperature_min": daily.Variables(4).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "sunrise": daily.Variables(5).ValuesAsNumpy()[:row_count],  # type: ignore
                "sunset": daily.Variables(6).ValuesAsNumpy()[:row_count],  # type: ignore
                "daylight_duration": daily.Variables(7).ValuesAsNumpy()[:row_count],  # type: ignore
                "sunshine_duration": daily.Variables(8).ValuesAsNumpy()[:row_count],  # type: ignore
                "uv_index_max": daily.Variables(9).ValuesAsNumpy()[:row_count],  # type: ignore
                "uv_index_clear_sky_max": daily.Variables(10).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "rain_sum": daily.Variables(11).ValuesAsNumpy()[:row_count],  # type: ignore
                "showers_sum": daily.Variables(12).ValuesAsNumpy()[:row_count],  # type: ignore
                "snowfall_sum": daily.Variables(13).ValuesAsNumpy()[:row_count],  # type: ignore
                "precipitation_sum": daily.Variables(14).ValuesAsNumpy()[:row_count],  # type: ignore
                "precipitation_hours": daily.Variables(15).ValuesAsNumpy()[:row_count],  # type: ignore
                "precipitation_probability_max": daily.Variables(16).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "wind_speed_10m_max": daily.Variables(17).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_gusts_10m_max": daily.Variables(18).ValuesAsNumpy()[:row_count],  # type: ignore
                "wind_direction_10m_dominant": daily.Variables(19).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "shortwave_radiation_sum": daily.Variables(20).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
                "et0_fao_evapotranspiration": daily.Variables(21).ValuesAsNumpy()[  # type: ignore
                    :row_count
                ],  # type: ignore
            },
        )

        dt = dt.replace(tzinfo=None)
        timezone = pytz.timezone(tz)
        dt = timezone.localize(dt)

        hourly_idx = hourly_df.index.get_indexer([dt], method="nearest")[0]
        temperature = hourly_df.iloc[hourly_idx]["temperature_2m"]  # type: ignore
        relative_humidity = hourly_df.iloc[hourly_idx]["relative_humidity_2m"]  # type: ignore
        dew_point_2m = hourly_df.iloc[hourly_idx]["dew_point_2m"]  # type: ignore
        apparent_temperature = hourly_df.iloc[hourly_idx]["apparent_temperature"]  # type: ignore
        precipitation_probability = hourly_df.iloc[hourly_idx][
            "precipitation_probability"
        ]  # type: ignore
        precipitation = hourly_df.iloc[hourly_idx]["precipitation"]  # type: ignore
        rain = hourly_df.iloc[hourly_idx]["rain"]  # type: ignore
        showers = hourly_df.iloc[hourly_idx]["showers"]  # type: ignore
        snowfall = hourly_df.iloc[hourly_idx]["snowfall"]  # type: ignore
        snow_depth = hourly_df.iloc[hourly_idx]["snow_depth"]  # type: ignore
        weather_code = hourly_df.iloc[hourly_idx]["weather_code"]  # type: ignore
        pressure_msl = hourly_df.iloc[hourly_idx]["pressure_msl"]  # type: ignore
        surface_pressure = hourly_df.iloc[hourly_idx]["surface_pressure"]  # type: ignore
        cloud_cover = hourly_df.iloc[hourly_idx]["cloud_cover"]  # type: ignore
        cloud_cover_low = hourly_df.iloc[hourly_idx]["cloud_cover_low"]  # type: ignore
        cloud_cover_mid = hourly_df.iloc[hourly_idx]["cloud_cover_mid"]  # type: ignore
        cloud_cover_high = hourly_df.iloc[hourly_idx]["cloud_cover_high"]  # type: ignore
        visibility = hourly_df.iloc[hourly_idx]["visibility"]  # type: ignore
        evapotranspiration = hourly_df.iloc[hourly_idx]["evapotranspiration"]  # type: ignore
        reference_evapotranspiration = hourly_df.iloc[hourly_idx][
            "reference_evapotranspiration"
        ]  # type: ignore
        vapour_pressure_deficit = hourly_df.iloc[hourly_idx]["vapour_pressure_deficit"]  # type: ignore
        wind_speed_10m = hourly_df.iloc[hourly_idx]["wind_speed_10m"]  # type: ignore
        wind_speed_80m = hourly_df.iloc[hourly_idx]["wind_speed_80m"]  # type: ignore
        wind_speed_120m = hourly_df.iloc[hourly_idx]["wind_speed_120m"]  # type: ignore
        wind_speed_180m = hourly_df.iloc[hourly_idx]["wind_speed_180m"]  # type: ignore
        wind_direction_10m = hourly_df.iloc[hourly_idx]["wind_direction_10m"]  # type: ignore
        wind_direction_80m = hourly_df.iloc[hourly_idx]["wind_direction_80m"]  # type: ignore
        wind_direction_120m = hourly_df.iloc[hourly_idx]["wind_direction_120m"]  # type: ignore
        wind_direction_180m = hourly_df.iloc[hourly_idx]["wind_direction_180m"]  # type: ignore
        wind_gusts = hourly_df.iloc[hourly_idx]["wind_gusts"]  # type: ignore
        temperature_80m = hourly_df.iloc[hourly_idx]["temperature_80m"]  # type: ignore
        temperature_120m = hourly_df.iloc[hourly_idx]["temperature_120m"]  # type: ignore
        temperature_180m = hourly_df.iloc[hourly_idx]["temperature_180m"]  # type: ignore
        soil_temperature = hourly_df.iloc[hourly_idx]["soil_temperature"]  # type: ignore
        soil_temperature_6cm = hourly_df.iloc[hourly_idx]["soil_temperature_6cm"]  # type: ignore
        soil_temperature_18cm = hourly_df.iloc[hourly_idx]["soil_temperature_18cm"]  # type: ignore
        soil_temperature_54cm = hourly_df.iloc[hourly_idx]["soil_temperature_54cm"]  # type: ignore
        soil_moisture = hourly_df.iloc[hourly_idx]["soil_moisture"]  # type: ignore
        soil_moisture_1cm = hourly_df.iloc[hourly_idx]["soil_moisture_1cm"]  # type: ignore
        soil_moisture_3cm = hourly_df.iloc[hourly_idx]["soil_moisture_3cm"]  # type: ignore
        soil_moisture_9cm = hourly_df.iloc[hourly_idx]["soil_moisture_9cm"]  # type: ignore
        soil_moisture_27cm = hourly_df.iloc[hourly_idx]["soil_moisture_27cm"]  # type: ignore

        daily_idx = daily_df.index.get_indexer([dt], method="nearest")[0]
        daily_weather_code = daily_df.iloc[daily_idx]["weather_code"]  # type: ignore
        temperature_2m_max = daily_df.iloc[daily_idx]["temperature_2m_max"]  # type: ignore
        temperature_2m_min = daily_df.iloc[daily_idx]["temperature_2m_min"]  # type: ignore
        apparent_temperature_max = daily_df.iloc[daily_idx]["apparent_temperature_max"]  # type: ignore
        apparent_temperature_min = daily_df.iloc[daily_idx]["apparent_temperature_min"]  # type: ignore
        sunrise = daily_df.iloc[daily_idx]["sunrise"]  # type: ignore
        sunset = daily_df.iloc[daily_idx]["sunset"]  # type: ignore
        daylight_duration = daily_df.iloc[daily_idx]["daylight_duration"]  # type: ignore
        sunshine_duration = daily_df.iloc[daily_idx]["sunshine_duration"]  # type: ignore
        uv_index_max = daily_df.iloc[daily_idx]["uv_index_max"]  # type: ignore
        uv_index_clear_sky_max = daily_df.iloc[daily_idx]["uv_index_clear_sky_max"]  # type: ignore
        rain_sum = daily_df.iloc[daily_idx]["rain_sum"]  # type: ignore
        showers_sum = daily_df.iloc[daily_idx]["showers_sum"]  # type: ignore
        snowfall_sum = daily_df.iloc[daily_idx]["snowfall_sum"]  # type: ignore
        precipitation_sum = daily_df.iloc[daily_idx]["precipitation_sum"]  # type: ignore
        precipitation_hours = daily_df.iloc[daily_idx]["precipitation_hours"]  # type: ignore
        precipitation_probability_max = daily_df.iloc[daily_idx][
            "precipitation_probability_max"
        ]  # type: ignore
        wind_speed_10m_max = daily_df.iloc[daily_idx]["wind_speed_10m_max"]  # type: ignore
        wind_gusts_10m_max = daily_df.iloc[daily_idx]["wind_gusts_10m_max"]  # type: ignore
        wind_direction_10m_dominant = daily_df.iloc[daily_idx][
            "wind_direction_10m_dominant"
        ]  # type: ignore
        shortwave_radiation_sum = daily_df.iloc[daily_idx]["shortwave_radiation_sum"]  # type: ignore
        et0_fao_evapotranspiration = daily_df.iloc[daily_idx][
            "et0_fao_evapotranspiration"
        ]  # type: ignore

        return WeatherModel(
            temperature=temperature,
            relative_humidity=relative_humidity,
            dew_point=dew_point_2m,
            apparent_temperature=apparent_temperature,
            precipitation_probability=precipitation_probability,
            precipitation=precipitation,
            rain=rain,
            showers=showers,
            snowfall=snowfall,
            snow_depth=snow_depth,
            weather_code=weather_code,
            sealevel_pressure=pressure_msl,
            surface_pressure=surface_pressure,
            cloud_cover_total=cloud_cover,
            cloud_cover_low=cloud_cover_low,
            cloud_cover_mid=cloud_cover_mid,
            cloud_cover_high=cloud_cover_high,
            visibility=visibility,
            evapotranspiration=evapotranspiration,
            reference_evapotranspiration=reference_evapotranspiration,
            vapour_pressure_deficit=vapour_pressure_deficit,
            wind_speed_10m=wind_speed_10m,
            wind_speed_80m=wind_speed_80m,
            wind_speed_120m=wind_speed_120m,
            wind_speed_180m=wind_speed_180m,
            wind_direction_10m=wind_direction_10m,
            wind_direction_80m=wind_direction_80m,
            wind_direction_120m=wind_direction_120m,
            wind_direction_180m=wind_direction_180m,
            wind_gusts=wind_gusts,
            temperature_80m=temperature_80m,
            temperature_120m=temperature_120m,
            temperature_180m=temperature_180m,
            soil_temperature_0cm=soil_temperature,
            soil_temperature_6cm=soil_temperature_6cm,
            soil_temperature_18cm=soil_temperature_18cm,
            soil_temperature_54cm=soil_temperature_54cm,
            soil_moisture_0cm=soil_moisture,
            soil_moisture_1cm=soil_moisture_1cm,
            soil_moisture_3cm=soil_moisture_3cm,
            soil_moisture_9cm=soil_moisture_9cm,
            soil_moisture_27cm=soil_moisture_27cm,
            daily_weather_code=daily_weather_code,
            daily_maximum_temperature_2m=temperature_2m_max,
            daily_minimum_temperature_2m=temperature_2m_min,
            daily_maximum_apparent_temperature_2m=apparent_temperature_max,
            daily_minimum_apparent_temperature_2m=apparent_temperature_min,
            sunrise=sunrise,
            sunset=sunset,
            daylight_duration=daylight_duration,
            sunshine_duration=sunshine_duration,
            uv_index=uv_index_max,
            uv_index_clear_sky=uv_index_clear_sky_max,
            rain_sum=rain_sum,
            showers_sum=showers_sum,
            snowfall_sum=snowfall_sum,
            precipitation_sum=precipitation_sum,
            precipitation_hours=precipitation_hours,
            precipitation_probability_max=precipitation_probability_max,
            maximum_wind_speed_10m=wind_speed_10m_max,
            maximum_wind_gusts_10m=wind_gusts_10m_max,
            dominant_wind_direction=wind_direction_10m_dominant,
            shortwave_radiation_sum=shortwave_radiation_sum,
            daily_reference_evapotranspiration=et0_fao_evapotranspiration,
            version=version,
        )
    except (
        struct.error,
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
    ):
        return None


def _create_openmeteo_weather_model(
    session: requests_cache.CachedSession,
    latitude: float,
    longitude: float,
    dt: datetime.datetime,
    tz: str,
    version: str,
) -> WeatherModel | None:
    # pylint: disable=broad-exception-caught
    client = openmeteo_requests.Client(session=session)
    try:
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": [
                "temperature_2m",
                "relative_humidity_2m",
                "dew_point_2m",
                "apparent_temperature",
                "precipitation",
                "rain",
                "snowfall",
                "snow_depth",
                "weather_code",
                "pressure_msl",
                "surface_pressure",
                "cloud_cover",
                "cloud_cover_low",
                "cloud_cover_mid",
                "cloud_cover_high",
                "et0_fao_evapotranspiration",
                "vapour_pressure_deficit",
                "wind_speed_10m",
                "wind_speed_100m",
                "wind_direction_10m",
                "wind_direction_100m",
                "wind_gusts_10m",
                "soil_temperature_0_to_7cm",
                "soil_temperature_7_to_28cm",
                "soil_temperature_28_to_100cm",
                "soil_temperature_100_to_255cm",
                "soil_moisture_0_to_7cm",
                "soil_moisture_7_to_28cm",
                "soil_moisture_28_to_100cm",
                "soil_moisture_100_to_255cm",
            ],
            "daily": [
                "weather_code",
                "temperature_2m_max",
                "temperature_2m_min",
                "temperature_2m_mean",
                "apparent_temperature_max",
                "apparent_temperature_min",
                "apparent_temperature_mean",
                "sunrise",
                "sunset",
                "daylight_duration",
                "sunshine_duration",
                "precipitation_sum",
                "rain_sum",
                "snowfall_sum",
                "precipitation_hours",
                "wind_speed_10m_max",
                "wind_gusts_10m_max",
                "wind_direction_10m_dominant",
                "shortwave_radiation_sum",
                "et0_fao_evapotranspiration",
            ],
            "timezone": tz,
        }
        url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
        if dt.date() > datetime.datetime.today().date():
            url = "https://api.open-meteo.com/v1/forecast"
            params["forecast_days"] = (
                datetime.datetime.today().date() - dt.date()
            ).days
        else:
            params["start_date"] = str((dt - datetime.timedelta(days=1.0)).date())
            params["end_date"] = str(dt.date())
        responses = client.weather_api(
            url,
            params=params,
        )
        return _parse_openmeteo(responses, tz, dt, version)
    except (
        requests.exceptions.RetryError,
        OpenMeteoRequestsError,
        requests.exceptions.ReadTimeout,
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
    ):
        return None
    except Exception as e:
        e_text = str(e)
        if "Parameter 'start_date' is out of allowed range from" in e_text:
            return None
        raise e


@MEMORY.cache(ignore=["session"])
def _cached_create_openmeteo_weather_model(
    session: requests_cache.CachedSession,
    latitude: float,
    longitude: float,
    dt: datetime.datetime,
    tz: str,
    version: str,
) -> WeatherModel | None:
    return _create_openmeteo_weather_model(
        session, latitude, longitude, dt, tz, version
    )


def create_openmeteo_weather_model(
    session: requests_cache.CachedSession,
    latitude: float,
    longitude: float,
    dt: datetime.datetime,
    tz: str,
) -> WeatherModel | None:
    """Create a weather model from openmeteo."""
    if not pytest_is_running.is_running() and dt < datetime.datetime.now().replace(
        tzinfo=dt.tzinfo
    ) - datetime.timedelta(days=3):
        return _cached_create_openmeteo_weather_model(
            session, latitude, longitude, dt, tz, VERSION
        )
    with session.cache_disabled():
        return _create_openmeteo_weather_model(
            session, latitude, longitude, dt, tz, VERSION
        )
