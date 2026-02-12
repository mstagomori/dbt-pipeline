{{ config(
    materialized='table',
    unique_key='id'
)}}

with source as (
    select *
    from {{ source('dev', 'weather_data') }}
)

select
    id,
    city,
    temperature,
    weather_descriptions,
    wind_speed,
    inserted_at,
    time as weather_time_local,
    utc_offset
from source