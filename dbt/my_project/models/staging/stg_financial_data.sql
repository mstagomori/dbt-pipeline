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
    date,
    open,
    close,
    high,
    low,
    volume
from source