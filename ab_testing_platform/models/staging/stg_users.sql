select
    cast(user_id as bigint) as user_id,
    cast(signup_date as timestamp) as signup_date,
    upper(country) as country,
    variant,
    cast(converted as int) as converted
from {{ source('bronze', 'users') }}