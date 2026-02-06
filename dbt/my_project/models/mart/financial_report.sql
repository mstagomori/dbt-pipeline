{{ config(
    materialized='table',
    unique_key='id'
) }}

select 
    date,
    open,
    close,
    high,
    low,
    volume
from {{ ref('stg_financial_data') }}