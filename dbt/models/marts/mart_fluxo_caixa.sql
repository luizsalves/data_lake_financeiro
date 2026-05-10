select
    loaded_at
from {{ ref('stg_recebimentos') }}
