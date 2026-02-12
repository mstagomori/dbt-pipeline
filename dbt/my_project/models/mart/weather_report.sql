{{ config(
    materialized='table',
    unique_key='id'
) }}

select 
    weather_time_local,
    temperature,
    weather_descriptions,
    wind_speed,
    utc_offset
from {{ ref('stg_weather_data') }}