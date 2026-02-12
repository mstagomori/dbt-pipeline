{{ config(
    materialized='table'
) }}

-- Calculate the daily average closing price from weather data
select
    date_trunc('day', weather_time_local)::date as day,
    avg(temperature) as average_temperature
from {{ ref('stg_weather_data') }}
group by day
order by day