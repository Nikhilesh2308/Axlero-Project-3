# Logistics & Supply Chain – Delivery Route Delay Forecasting

## Axlero Data Analytics Internship | Project 3

A machine learning project focused on forecasting shipment delivery delays and helping logistics teams identify high-risk routes, carriers, and operating conditions.

## Project Overview

This project develops a data pipeline and regression workflow to estimate shipment delay duration in hours. It combines shipment timestamps, route coordinates, weather information, and carrier-related attributes to support operational planning and proactive intervention.

The current project package uses a **synthetic shipment dataset** (30,000 records; generated with seed 42, covering 2024–2025). Results should therefore be interpreted as a demonstration of the methodology on synthetic data, not as validated performance on live logistics operations.

## Objectives

- Prepare and validate shipment and logistics data.
- Extract temporal features from shipment timestamps, including day, week, month, and time-of-day.
- Calculate route distance from origin and destination coordinates using the Haversine formula.
- Incorporate weather and carrier-performance information where available in the prepared dataset.
- Train regression models to estimate continuous shipment delay duration.
- Evaluate model performance and inspect prediction residuals.
- Present operational insights through a dashboard highlighting high-risk routes and enabling region/carrier filtering.

## Methodology

1. **Data preparation:** Load raw shipment data, validate fields, parse timestamps, and prepare interim and processed datasets.
2. **Feature engineering:** Create calendar/time features and calculate geographic route distance from raw coordinates.
3. **Exploratory analysis:** Examine delay patterns across routes, time periods, regions, and carriers.
4. **Model development:** Train and compare Random Forest Regressor and Ridge Regression models.
5. **Evaluation:** Assess predictions using MAE, RMSE, and R², followed by residual analysis.
6. **Dashboard preparation:** Surface delay patterns and high-risk route information for operational review.

## Current Reported Results

The project README and generated metrics report the following model performance:

| Metric | Reported value |
|---|---:|
| R² | 0.672 |
| RMSE | 1.52 hours |
| MAE | 1.02 hours |

The package also reports a 48% lower RMSE than a zero-delay baseline. These are results from the included synthetic dataset and project experiment; they are not a guarantee of performance on real shipment data.

## Repository Structure

```
.
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── notebooks/
│   ├── 1.0-spatiotemporal-wrangling.ipynb
│   ├── 2.0-time-series-eda.ipynb
│   ├── 3.0-regression-modeling.ipynb
│   └── 4.0-operations-dashboard-prep.ipynb
├── src/
│   ├── dataset.py
│   ├── config.py
│   ├── features.py
│   ├── run_pipeline.py
│   └── modeling/
├── models/
├── reports/
│   └── figures/
├── dashboard/
├── sql/
├── tests/
├── docs/
├── requirements.txt
└── README.md
```

The exact contents may evolve as the project is updated. Refer to the repository tree for the current files.

## Setup

Python 3.10 or a compatible version is recommended.

```bash
git clone https://github.com/Nikhilesh2308/Axlero-Project-3.git
cd Axlero-Project-3

python -m venv .venv
```

Activate the virtual environment:

**Windows**
```bash
.venv\\Scripts\\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline using the entry point included in the repository:

```bash
python src/run_pipeline.py
```

Review the numbered notebooks for the step-by-step analysis and modeling workflow. Check each script's arguments and configuration before running optional stages.

## Dashboard

The project package includes an HTML operations dashboard and supporting dashboard assets/build instructions. A Tableau packaged workbook (`.twbx`) or Power BI file (`.pbix`) should only be listed here once the corresponding export has actually been added to the repository.

## Reproducibility and Version Control

The repository is organized to separate raw, interim, and processed data; exploratory notebooks; reusable source code; trained model artifacts; reports; and dashboard resources. Commit meaningful project changes as they are completed, with commit messages that describe the actual work. Do not fabricate or backdate development history.

## Limitations

- The included dataset is synthetic; real-world validation is required before operational use.
- Model metrics depend on the generated data, feature set, and evaluation split.
- Weather/carrier enrichment and dashboard functionality should be checked against the included source files and data before deployment.
- The reported regression metrics do not establish causal relationships between features and delays.

## Internship Project

**Program:** Axlero Data Analytics Internship  
**Project:** Project 3 – Logistics & Supply Chain: Delivery Route Delay Forecasting

---
