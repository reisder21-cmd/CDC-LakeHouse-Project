-- 1. drop the slot (guarded — the function errors if it doesn't exist)
SELECT pg_drop_replication_slot('cdc_slot')
WHERE EXISTS (SELECT 1 FROM pg_replication_slots WHERE slot_name = 'cdc_slot');

-- 2. drop the publication
DROP PUBLICATION IF EXISTS cdc_pub;

-- 3. drop tables, child before parent
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;