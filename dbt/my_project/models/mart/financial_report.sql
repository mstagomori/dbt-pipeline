{{ config(
    materialized='table',
    unique_key='id'
) }}

select 
    timestamp,
    ask,
    bid,
    mid,
    symbol
from {{ ref('stg_financial_data') }}