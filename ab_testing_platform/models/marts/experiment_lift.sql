with base as (
    select
        variant,
        sum(converted) * 1.0 / count(*) as conversion_rate
    from {{ ref('stg_users') }}
    group by variant
),

pivoted as (
    select
        max(case when variant = 'A' then conversion_rate end) as A_rate,
        max(case when variant = 'B' then conversion_rate end) as B_rate
    from base
)

select
    A_rate,
    B_rate,
    (B_rate - A_rate) as absolute_lift,
    (B_rate - A_rate) / A_rate as relative_lift
from pivoted