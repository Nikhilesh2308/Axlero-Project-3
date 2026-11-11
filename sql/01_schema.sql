-- Raw layer: loaded exactly as received. Timestamps stay TEXT because the source
-- system mixes several date formats; they are parsed in Python (src/features.py).
DROP TABLE IF EXISTS shipments_raw CASCADE;
DROP TABLE IF EXISTS weather_daily CASCADE;
DROP TABLE IF EXISTS carriers CASCADE;

CREATE TABLE carriers (
    carrier_id    VARCHAR(10) PRIMARY KEY,
    carrier_name  VARCHAR(50)
);

CREATE TABLE shipments_raw (
    shipment_id     INTEGER,
    carrier_id      VARCHAR(10),
    vehicle_type    VARCHAR(30),
    origin_city     VARCHAR(40),
    origin_lat      NUMERIC(9, 5),
    origin_lon      NUMERIC(9, 5),
    dest_city       VARCHAR(40),
    dest_lat        NUMERIC(9, 5),
    dest_lon        NUMERIC(9, 5),
    package_weight_kg NUMERIC(10, 2),
    sla_hours       NUMERIC(6, 1),
    dispatch_time   TEXT,
    delivery_time   TEXT
);

CREATE TABLE weather_daily (
    weather_date  DATE,
    city          VARCHAR(40),
    precip_mm     NUMERIC(6, 1),
    temp_c        NUMERIC(4, 1)
);

CREATE INDEX idx_ship_carrier ON shipments_raw (carrier_id);
