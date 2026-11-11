# 20-Day Commit Plan (4 weeks x 5 working days)

The programme evaluates **genuine daily, atomic commits across all 4 weeks**; a single bulk push or back-dated
history is disqualifying and would not survive the commit-graph review. This repo was delivered as finished code, so
**commit it gradually**: on each day run, read and understand that piece, then commit it with a message in your
own words. Use one commit per logical change (2-4 a day is fine).

Conventions: `type: what changed`, e.g. `feat: parse mixed datetime formats`, `fix:`, `docs:`, `test:`, `refactor:`.

| Day | Do & understand | Files to commit | Example message |
|---|---|---|---|
| **W1-D1** | Repo, folder structure, config | `.gitignore`, `requirements.txt`, `.gitkeep`s, `src/config.py` | `chore: initialise cookiecutter data science structure` |
| W1-D2 | Synthetic shipment generator | `src/dataset.py` (generate_*) | `feat: simulate shipments, carriers and weather` |
| W1-D3 | PostgreSQL schema + load | `sql/01_schema.sql`, `load_raw_to_postgres` | `feat: load raw shipments into PostgreSQL` |
| W1-D4 | Datetime parsing | `sql/02_*.sql`, `parse_mixed_datetimes` | `feat: parse four mixed timestamp formats` |
| W1-D5 | Haversine + cleaning + notebook 1.0 | `haversine_km`, `clean_shipments`, `notebooks/1.0-*`, `data/interim/*` | `feat: haversine distance and data cleaning` |
| **W2-D1** | Time features | `add_time_features` | `feat: add day/hour/month and seasonality features` |
| W2-D2 | Weather merge | `merge_weather` in `dataset.py` | `feat: merge origin-city weather with pandas merge` |
| W2-D3 | Route features | `add_route_features` | `feat: add route, region and size features` |
| W2-D4 | Vendor rolling performance (leakage-safe) | `add_vendor_rolling`, `carrier_daily_performance` | `feat: leakage-safe rolling vendor performance` |
| W2-D5 | Time-series EDA notebook | `notebooks/2.0-*`, figures 03-07, `data/processed/shipments_enriched.csv` | `docs: time-series EDA notebook` |
| **W3-D1** | Chronological split + preprocessor | `chronological_split`, `make_preprocessor` | `feat: time-based split and one-hot pipeline` |
| W3-D2 | Baselines + Ridge | `baselines`, ridge search | `feat: baselines and ridge regression` |
| W3-D3 | Random Forest + TimeSeriesSplit tuning | `candidate_searches` | `feat: tuned random forest with TimeSeriesSplit` |
| W3-D4 | Residual analysis + importance | `notebooks/3.0-*`, figures 08-11 | `docs: residual and feature-importance analysis` |
| W3-D5 | Save model + tests | `models/*`, `tests/test_features.py` | `test: leakage, parsing and split tests` |
| **W4-D1** | Scoring + risk tiers | `src/modeling/predict.py` | `feat: score shipments and assign risk tiers` |
| W4-D2 | BI tables + pipeline runner | `src/run_pipeline.py`, notebook 4.0 | `feat: export dashboard-ready tables` |
| W4-D3 | Tableau / Power BI dashboard | `dashboard/*.twbx` (you build it) | `feat: add operations dashboard` |
| W4-D4 | Report + README | `reports/final_report.md`, `README.md` | `docs: final report and README` |
| W4-D5 | Lint, final checks, tag | `setup.cfg`, formatting | `chore: flake8/black clean-up; tag v1.0` |

Daily: `git add <files> && git commit -m "..." && git push`. If a day has less work, commit smaller pieces (a docstring, a
figure, a test) rather than skipping - but only commit work you actually did that day.
