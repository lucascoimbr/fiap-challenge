create table customer.personal_info 
WITH (
format = 'PARQUET',
external_location='s3://fiapchallenge/customer_register/personal_info/')
as

with init_table as (
select
    id
    ,to_hex(md5(to_utf8(
        concat(
            cast(customer_id as varchar), 
            cast(cpf as varchar),
            cast(address_number as varchar)
            )))) id
    , name 
    , cpf
    ,to_hex(md5(to_utf8(
        concat(
            cast(id as varchar), 
            cast(cpf as varchar),
            cast(name as varchar)
            )))) id
    , cast(birthdate as timestamp)
    , "metadata.timestamp"
from
register.personal_info
)