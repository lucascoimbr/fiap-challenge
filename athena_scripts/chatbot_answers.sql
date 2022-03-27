create table chatbot.answers 
WITH (
format = 'PARQUET',
external_location='s3://fiapchallenge/chatbot_answers/')
as

with init_table as (
select
    id
    , customer_id 
    , field
    , value
    , "metadata.timestamp"
from
chatbot.answers
)