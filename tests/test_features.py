"""Unit tests for parsing, geospatial math, cleaning and leakage safety (pytest -q)."""

import pandas as pd

from src import dataset, features as F
from src.modeling import train as T


def test_mixed_datetime_formats_all_parse():
    s = pd.Series(
        ["2024-03-05 14:30:00", "05/03/2024 14:30", "2024-03-05T14:30:00Z", "05 Mar 2024 02:30 PM"]
    )
    out = F.parse_mixed_datetimes(s)
    assert out.notna().all() and (out == pd.Timestamp("2024-03-05 14:30")).all()


def test_haversine_mumbai_delhi_about_1150km():
    d = F.haversine_km(19.0760, 72.8777, 28.7041, 77.1025)
    assert 1100 < d < 1200 and F.haversine_km(10, 10, 10, 10) == 0


def _raw():
    return pd.DataFrame(
        {
            "shipment_id": [1, 2],
            "carrier_id": ["C01", None],
            "vehicle_type": [" VAN", "van"],
            "origin_city": ["Mumbai"] * 2,
            "origin_lat": [19.07, 19.07],
            "origin_lon": [72.87, 72.87],
            "dest_city": ["Pune"] * 2,
            "dest_lat": [73.85, 18.52],
            "dest_lon": [18.52, 73.85],  # 1st swapped
            "package_weight_kg": [10.0, None],
            "sla_hours": [8.0, 8.0],
            "dispatch_time": ["2024-01-01 10:00:00", "2024-01-02 12:00:00"],
            "delivery_time": [
                "2024-01-01 08:00:00",
                "2024-01-02 17:00:00",
            ],  # 1st delivered "before" dispatch
        }
    )


def test_cleaning_repairs_instead_of_dropping():
    clean, audit = F.clean_shipments(_raw())
    assert len(clean) == 2 and audit["pct_rows_dropped"] < 5
    assert clean["vehicle_type"].eq("van").all() and (clean["carrier_id"] == "UNKNOWN").sum() == 1
    assert clean["dest_lat"].between(*F.INDIA_LAT).all()
    assert (clean["delivery_hours"] > 0).all()


def test_vendor_rolling_never_sees_undelivered_shipments():
    t0 = pd.Timestamp("2024-01-01")
    df = pd.DataFrame(
        {
            "carrier_id": ["A", "A", "A"],
            "dispatch_time": [t0, t0 + pd.Timedelta(hours=5), t0 + pd.Timedelta(hours=20)],
            "delivery_time": [
                t0 + pd.Timedelta(hours=10),
                t0 + pd.Timedelta(hours=30),
                t0 + pd.Timedelta(hours=40),
            ],
            "hours_delayed": [5.0, 1.0, 2.0],
            "is_late": [1, 1, 1],
        }
    )
    out = F.add_vendor_rolling(df, window=1).sort_values("dispatch_time")
    assert pd.isna(out["vendor_roll_delay"].iloc[0])  # nothing delivered yet
    assert pd.isna(out["vendor_roll_delay"].iloc[1])  # shipment 1 not yet delivered at hour 5
    assert out["vendor_roll_delay"].iloc[2] == 5.0  # only shipment 1 was delivered by hour 20


def test_chronological_split_has_no_overlap_in_time():
    t = pd.DataFrame({"dispatch_time": pd.date_range("2024-01-01", periods=100, freq="D")})
    train, test, cut = T.chronological_split(t)
    assert train["dispatch_time"].max() < test["dispatch_time"].min()


def test_weather_merge_keeps_every_shipment():
    ship = pd.DataFrame(
        {
            "dispatch_time": pd.to_datetime(["2024-07-01 09:00", "2024-07-02 10:00"]),
            "origin_city": ["Mumbai", "Mumbai"],
        }
    )
    w = pd.DataFrame(
        {
            "weather_date": pd.to_datetime(["2024-07-01"]),
            "city": ["Mumbai"],
            "precip_mm": [30.0],
            "temp_c": [27.0],
        }
    )
    out = dataset.merge_weather(ship, w)
    assert len(out) == 2 and out["precip_flag"].tolist() == [1, 0]
