"""Combined weather model."""

# pylint: disable=too-many-locals,too-many-statements,too-many-branches
from ..weather_model import VERSION, WeatherModel
from .most_interesting import more_interesting


def create_combined_weather_model(
    weather_models: list[WeatherModel],
) -> WeatherModel | None:
    """Create a weather model by combining many weather models."""
    if not weather_models:
        return None
    temperature = None
    relative_humidity = None
    dew_point = None
    apparent_temperature = None
    precipitation_probability = None
    precipitation = None
    rain = None
    showers = None
    snowfall = None
    snow_depth = None
    weather_code = None
    sealevel_pressure = None
    surface_pressure = None
    cloud_cover_total = None
    cloud_cover_low = None
    cloud_cover_mid = None
    cloud_cover_high = None
    visibility = None
    evapotranspiration = None
    reference_evapotranspiration = None
    vapour_pressure_deficit = None
    wind_speed_10m = None
    wind_speed_80m = None
    wind_speed_120m = None
    wind_speed_180m = None
    wind_direction_10m = None
    wind_direction_80m = None
    wind_direction_120m = None
    wind_direction_180m = None
    wind_gusts = None
    temperature_80m = None
    temperature_120m = None
    temperature_180m = None
    soil_temperature_0cm = None
    soil_temperature_6cm = None
    soil_temperature_18cm = None
    soil_temperature_54cm = None
    soil_moisture_0cm = None
    soil_moisture_1cm = None
    soil_moisture_3cm = None
    soil_moisture_9cm = None
    soil_moisture_27cm = None
    daily_weather_code = None
    daily_maximum_temperature_2m = None
    daily_minimum_temperature_2m = None
    daily_maximum_apparent_temperature_2m = None
    daily_minimum_apparent_temperature_2m = None
    sunrise = None
    sunset = None
    daylight_duration = None
    sunshine_duration = None
    uv_index = None
    uv_index_clear_sky = None
    rain_sum = None
    showers_sum = None
    snowfall_sum = None
    precipitation_sum = None
    precipitation_hours = None
    precipitation_probability_max = None
    maximum_wind_speed_10m = None
    maximum_wind_gusts_10m = None
    dominant_wind_direction = None
    shortwave_radiation_sum = None
    daily_reference_evapotranspiration = None
    for weather_model in weather_models:
        temperature = more_interesting(temperature, weather_model.temperature)
        relative_humidity = more_interesting(
            relative_humidity, weather_model.relative_humidity
        )
        dew_point = more_interesting(dew_point, weather_model.dew_point)
        apparent_temperature = more_interesting(
            apparent_temperature, weather_model.apparent_temperature
        )
        precipitation_probability = more_interesting(
            precipitation_probability, weather_model.precipitation_probability
        )
        precipitation = more_interesting(precipitation, weather_model.precipitation)
        rain = more_interesting(rain, weather_model.rain)
        showers = more_interesting(showers, weather_model.showers)
        snowfall = more_interesting(snowfall, weather_model.snowfall)
        snow_depth = more_interesting(snow_depth, weather_model.snow_depth)
        weather_code = more_interesting(weather_code, weather_model.weather_code)
        sealevel_pressure = more_interesting(
            sealevel_pressure, weather_model.sealevel_pressure
        )
        surface_pressure = more_interesting(
            surface_pressure, weather_model.surface_pressure
        )
        cloud_cover_total = more_interesting(
            cloud_cover_total, weather_model.cloud_cover_total
        )
        cloud_cover_low = more_interesting(
            cloud_cover_low, weather_model.cloud_cover_low
        )
        cloud_cover_mid = more_interesting(
            cloud_cover_mid, weather_model.cloud_cover_mid
        )
        cloud_cover_high = more_interesting(
            cloud_cover_high, weather_model.cloud_cover_high
        )
        visibility = more_interesting(visibility, weather_model.visibility)
        evapotranspiration = more_interesting(
            evapotranspiration, weather_model.evapotranspiration
        )
        reference_evapotranspiration = more_interesting(
            reference_evapotranspiration, weather_model.reference_evapotranspiration
        )
        vapour_pressure_deficit = more_interesting(
            vapour_pressure_deficit, weather_model.vapour_pressure_deficit
        )
        wind_speed_10m = more_interesting(wind_speed_10m, weather_model.wind_speed_10m)
        wind_speed_80m = more_interesting(wind_speed_80m, weather_model.wind_speed_80m)
        wind_speed_120m = more_interesting(
            wind_speed_120m, weather_model.wind_speed_120m
        )
        wind_speed_180m = more_interesting(
            wind_speed_180m, weather_model.wind_speed_180m
        )
        wind_direction_10m = more_interesting(
            wind_direction_10m, weather_model.wind_direction_10m
        )
        wind_direction_80m = more_interesting(
            wind_direction_80m, weather_model.wind_direction_80m
        )
        wind_direction_120m = more_interesting(
            wind_direction_120m, weather_model.wind_direction_120m
        )
        wind_direction_180m = more_interesting(
            wind_direction_180m, weather_model.wind_direction_180m
        )
        wind_gusts = more_interesting(wind_gusts, weather_model.wind_gusts)
        temperature_80m = more_interesting(
            temperature_80m, weather_model.temperature_80m
        )
        temperature_120m = more_interesting(
            temperature_120m, weather_model.temperature_120m
        )
        temperature_180m = more_interesting(
            temperature_180m, weather_model.temperature_180m
        )
        soil_temperature_0cm = more_interesting(
            soil_temperature_0cm, weather_model.soil_temperature_0cm
        )
        soil_temperature_6cm = more_interesting(
            soil_temperature_6cm, weather_model.soil_temperature_6cm
        )
        soil_temperature_18cm = more_interesting(
            soil_temperature_18cm, weather_model.soil_temperature_18cm
        )
        soil_temperature_54cm = more_interesting(
            soil_temperature_54cm, weather_model.soil_temperature_54cm
        )
        soil_moisture_0cm = more_interesting(
            soil_moisture_0cm, weather_model.soil_moisture_0cm
        )
        soil_moisture_1cm = more_interesting(
            soil_moisture_1cm, weather_model.soil_moisture_1cm
        )
        soil_moisture_3cm = more_interesting(
            soil_moisture_3cm, weather_model.soil_moisture_3cm
        )
        soil_moisture_9cm = more_interesting(
            soil_moisture_9cm, weather_model.soil_moisture_9cm
        )
        soil_moisture_27cm = more_interesting(
            soil_moisture_27cm, weather_model.soil_moisture_27cm
        )
        daily_weather_code = more_interesting(
            daily_weather_code, weather_model.daily_weather_code
        )
        daily_maximum_temperature_2m = more_interesting(
            daily_maximum_temperature_2m, weather_model.daily_maximum_temperature_2m
        )
        daily_minimum_temperature_2m = more_interesting(
            daily_minimum_temperature_2m, weather_model.daily_minimum_temperature_2m
        )
        daily_maximum_apparent_temperature_2m = more_interesting(
            daily_maximum_apparent_temperature_2m,
            weather_model.daily_maximum_apparent_temperature_2m,
        )
        daily_minimum_apparent_temperature_2m = more_interesting(
            daily_minimum_apparent_temperature_2m,
            weather_model.daily_minimum_apparent_temperature_2m,
        )
        sunrise = more_interesting(sunrise, weather_model.sunrise)
        sunset = more_interesting(sunset, weather_model.sunset)
        daylight_duration = more_interesting(
            daylight_duration, weather_model.daylight_duration
        )
        sunshine_duration = more_interesting(
            sunshine_duration, weather_model.sunshine_duration
        )
        uv_index = more_interesting(uv_index, weather_model.uv_index)
        uv_index_clear_sky = more_interesting(
            uv_index_clear_sky, weather_model.uv_index_clear_sky
        )
        rain_sum = more_interesting(rain_sum, weather_model.rain_sum)
        showers_sum = more_interesting(showers_sum, weather_model.showers_sum)
        snowfall_sum = more_interesting(snowfall_sum, weather_model.snowfall_sum)
        precipitation_sum = more_interesting(
            precipitation_sum, weather_model.precipitation_sum
        )
        precipitation_hours = more_interesting(
            precipitation_hours, weather_model.precipitation_hours
        )
        precipitation_probability_max = more_interesting(
            precipitation_probability_max, weather_model.precipitation_probability_max
        )
        maximum_wind_speed_10m = more_interesting(
            maximum_wind_speed_10m, weather_model.maximum_wind_speed_10m
        )
        maximum_wind_gusts_10m = more_interesting(
            maximum_wind_gusts_10m, weather_model.maximum_wind_gusts_10m
        )
        dominant_wind_direction = more_interesting(
            dominant_wind_direction, weather_model.dominant_wind_direction
        )
        shortwave_radiation_sum = more_interesting(
            shortwave_radiation_sum, weather_model.shortwave_radiation_sum
        )
        daily_reference_evapotranspiration = more_interesting(
            daily_reference_evapotranspiration,
            weather_model.daily_reference_evapotranspiration,
        )

    return WeatherModel.model_construct(
        temperature=temperature,
        relative_humidity=relative_humidity,
        dew_point=dew_point,
        apparent_temperature=apparent_temperature,
        precipitation_probability=precipitation_probability,
        precipitation=precipitation,
        rain=rain,
        showers=showers,
        snowfall=snowfall,
        snow_depth=snow_depth,
        weather_code=weather_code,
        sealevel_pressure=sealevel_pressure,
        surface_pressure=surface_pressure,
        cloud_cover_total=cloud_cover_total,
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
        soil_temperature_0cm=soil_temperature_0cm,
        soil_temperature_6cm=soil_temperature_6cm,
        soil_temperature_18cm=soil_temperature_18cm,
        soil_temperature_54cm=soil_temperature_54cm,
        soil_moisture_0cm=soil_moisture_0cm,
        soil_moisture_1cm=soil_moisture_1cm,
        soil_moisture_3cm=soil_moisture_3cm,
        soil_moisture_9cm=soil_moisture_9cm,
        soil_moisture_27cm=soil_moisture_27cm,
        daily_weather_code=daily_weather_code,
        daily_maximum_temperature_2m=daily_maximum_temperature_2m,
        daily_minimum_temperature_2m=daily_minimum_temperature_2m,
        daily_maximum_apparent_temperature_2m=daily_maximum_apparent_temperature_2m,
        daily_minimum_apparent_temperature_2m=daily_minimum_apparent_temperature_2m,
        sunrise=sunrise,
        sunset=sunset,
        daylight_duration=daylight_duration,
        sunshine_duration=sunshine_duration,
        uv_index=uv_index,
        uv_index_clear_sky=uv_index_clear_sky,
        rain_sum=rain_sum,
        showers_sum=showers_sum,
        snowfall_sum=snowfall_sum,
        precipitation_sum=precipitation_sum,
        precipitation_hours=precipitation_hours,
        precipitation_probability_max=precipitation_probability_max,
        maximum_wind_speed_10m=maximum_wind_speed_10m,
        maximum_wind_gusts_10m=maximum_wind_gusts_10m,
        dominant_wind_direction=dominant_wind_direction,
        shortwave_radiation_sum=shortwave_radiation_sum,
        daily_reference_evapotranspiration=daily_reference_evapotranspiration,
        version=VERSION,
    )
