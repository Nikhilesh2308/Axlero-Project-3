# Supervisor Requirements Compliance

Project: Axlero Data Analytics Internship — Project 3
Title: Logistics & Supply Chain — Delivery Route Delay Forecasting

This package is organized around the supervisor's Cookiecutter Data Science requirement and the
four-week Project 3 lifecycle.

## Included in this package

- `data/raw/`: original shipment, carrier, and weather input CSVs.
- `data/interim/`: cleaned shipment data and cleaning audit.
- `data/processed/`: enriched modeling data, model comparison, route-risk summaries,
  carrier performance, and dashboard-ready data.
- `notebooks/`: numbered notebooks for spatio-temporal wrangling, time-series EDA,
  regression modeling, and operations-dashboard preparation.
- `src/`: reusable dataset, feature-engineering, pipeline, dashboard, training, and prediction code.
- `sql/`: PostgreSQL schema and extraction SQL.
- `models/`: trained model artifact and model metrics.
- `reports/`: final analytical report and figures, including residual/model diagnostics.
- `dashboard/`: interactive HTML dashboard, Tableau build guide, and dashboard backgrounds.
- `tests/`: feature/pipeline tests.
- `requirements.txt`: pinned Python dependencies.
- `docs/`: commit plan and technical defense notes.

## Supervisor criteria addressed

| Requirement | Package evidence |
|---|---|
| Cookiecutter Data Science structure | `data/raw`, `data/interim`, `data/processed`, `notebooks`, `src`, `reports` |
| Time-series handling | Numbered EDA notebook and engineered temporal features |
| Haversine geospatial distance | `src/features.py` and wrangling notebook |
| Weather and carrier enrichment | Dataset pipeline and processed datasets |
| Ridge and Random Forest regression | `src/modeling/train.py` and model comparison outputs |
| RMSE, MAE, R-squared | `models/delay_model_metrics.json` and final report |
| Residual analysis | `reports/figures/` and final report |
| Operations dashboard | `dashboard/ops_dashboard.html` and `dashboard/TABLEAU_BUILD_GUIDE.md` |
| Reproducibility | `requirements.txt`, source pipeline, SQL, tests, README |

## Items that must still be completed outside this ZIP

1. **Packaged BI workbook:** The source archive does not contain a Tableau `.twbx` or Power BI
   `.pbix` export. The HTML dashboard and Tableau build guide are included, but they are not a
   substitute for the supervisor's required `.twbx`/`.pbix`. Build the workbook in Tableau or
   Power BI, then add the exported file under `dashboard/`.
2. **Four-week Git history:** Git history is not included in a ZIP archive. The supervisor requires
   genuine, incremental commits over all four weeks (20 working days). Follow `docs/COMMIT_PLAN.md`.
   Do not fabricate or backdate commits. A bulk upload at the end does not satisfy this criterion.
3. **Review the synthetic-data limitation:** The dataset is synthetic because client data was not
   supplied. Disclose this clearly in the report and during the technical presentation.

## Before submission

- Create and verify the `.twbx` or `.pbix` export.
- Run the setup and pipeline commands in `README.md`.
- Run `pytest -q` and resolve any failures.
- Check that the report's metric values match the generated metrics JSON.
- Commit the work incrementally and push to the intended GitHub repository.
