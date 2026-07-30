CREATE PUBLICATION cdc_pub FOR TABLE customers, orders;

SELECT pg_create_logical_replication_slot('cdc_slot', 'test_decoding');
