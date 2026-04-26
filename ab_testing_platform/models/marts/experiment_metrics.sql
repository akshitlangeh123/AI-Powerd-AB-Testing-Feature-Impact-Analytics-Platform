select
    variant,
    count(*) as users,
    sum(converted) as conversions,
    sum(converted) * 1.0 / count(*) as conversion_rate
from {{ ref('stg_users') }}
group by variant