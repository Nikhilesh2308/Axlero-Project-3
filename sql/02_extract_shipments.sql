-- Extract used by src/features.py. De-duplicates exact repeats on the SQL side;
-- everything statistical (imputation, outlier rules) stays in Python.
SELECT DISTINCT
    shipment_id, carrier_id, vehicle_type,
    origin_city, origin_lat, origin_lon,
    dest_city, dest_lat, dest_lon,
    package_weight_kg, sla_hours, dispatch_time, delivery_time
FROM shipments_raw
ORDER BY shipment_id;
