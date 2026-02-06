{{ config(
    materialized='table'
) }}

-- Calculate the monthly average closing price from financial data
select
    date_trunc('month', date)::date as month,
    avg(close) as average_close_price
from {{ ref('stg_financial_data') }}
group by month
order by month