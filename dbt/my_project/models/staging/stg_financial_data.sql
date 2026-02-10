{{ config(
    materialized='table',
    unique_key='id'
)}}

with source as (
    select *
    from {{ source('dev', 'financial_data') }}
)

select
    id,
    TO_CHAR(TO_TIMESTAMP(timestamp),'DD-MM-YYYY') AS date,
    ask,
    bid,
    mid,
    symbol
from source