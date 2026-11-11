"""Central configuration for the delivery-delay forecasting project."""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_INTERIM = PROJECT_ROOT / "data" / "interim"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
SQL_DIR = PROJECT_ROOT / "sql"

RANDOM_STATE = 42

# Synthetic data window
START_DATE = "2024-01-01"
END_DATE = "2025-12-31"
N_SHIPMENTS = 30000

# Chronological split: first 80 % of dispatch time = train, last 20 % = test
TEST_FRACTION = 0.20

# Vendor-performance rolling window (number of previously DELIVERED shipments)
VENDOR_WINDOW = 50

# Risk tiers on predicted delay vs SLA (hours): Low < -0.5 <= Medium < 1.0 <= High
RISK_MEDIUM_HOURS = -0.5
RISK_HIGH_HOURS = 1.0

# Database connection (override with DATABASE_URL env var)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://nikki:nikki@localhost:5432/logistics_delay",
)
