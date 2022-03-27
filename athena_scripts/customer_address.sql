create table customer.address 
WITH (
format = 'PARQUET',
external_location='s3://fiapchallenge/customer_register/address/')
as

with init_table as (
select
    id
    ,to_hex(md5(to_utf8(
        concat(
            cast(customer_id as varchar), 
            cast(address_street as varchar),
            cast(address_number as varchar),
            )))) id
    ,customer_id
    , country_id 
    , address_street
    , address_number
    , address_complement
    , "metadata.timestamp"
from
register.address
)