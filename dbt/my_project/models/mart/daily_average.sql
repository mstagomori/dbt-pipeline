{{ config(
    materialized='table'
) }}

-- Calculate the daily average closing price from financial data
select
    date_trunc('day', date)::date as day,
    avg(mid) as average_mid_price
from {{ ref('stg_financial_data') }}
group by day
order by day