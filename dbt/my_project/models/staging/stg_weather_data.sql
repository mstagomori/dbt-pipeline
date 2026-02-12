{{ config(
    materialized='table',
    unique_key='id'
)}}

with source as (
    select *
    from {{ source('dev', 'weather_data') }}
),

resolve_duplicates as (
    select
        *,
        row_number() over (partition by time order by inserted_at) as rn
    from source
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
from resolve_duplicates
where rn = 1