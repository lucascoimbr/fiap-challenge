create table chatbot.answers 
WITH (
format = 'PARQUET',
external_location='s3://fiapchallenge/chatbot_answers/')
as

with init_table as (
select
    id
    , "protocol"
    , "queryResult.allRequiredParamsPresent"
    , "queryResult.fulfillmentMessages"
    , "queryResult.fulfillmentText"
    , "queryResult.intent.displayName"
    , "queryResult.intent.name"
    , "queryResult.intentDetectionConfidence"
    , "queryResult.languageCode"
    , "queryResult.outputContexts"
    , "queryResult.parameters.location"
    , "queryResult.parameters.url"
    , "queryText"
    , "responseId"
    , "customer_id" 
    , "metadata.timestamp"
from
chatbot.answers
)
