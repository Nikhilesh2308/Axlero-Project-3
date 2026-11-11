# Hiring-Manager Defence Notes (answer these in your own words)

**Business context (30 s):** Late deliveries cost SLA penalties. If we can predict before dispatch how late a shipment will
be, operations can intervene. The model predicts hours delayed vs SLA; a risk tier and route ranking make it actionable.

**How is Haversine computed, and why not Euclidean?** Coordinates are on a sphere, so straight-line degree differences are
wrong (a degree of longitude shrinks toward the poles). Haversine gives great-circle distance:
`a = sin^2(dphi/2) + cos(phi1)cos(phi2)sin^2(dlambda/2)`, `d = 2R*asin(sqrt(a))`, R = 6371 km. It is a lower bound on road
distance, which is why road distance is modelled via speed/vehicle effects. Sanity check: Mumbai-Delhi is ~1,150 km.

**Why parse four formats separately?** `05/03/2024` is ambiguous (5 March vs 3 May). Trying each *explicit* format in turn,
instead of letting pandas guess, avoids silently swapping day and month.

**How did you prevent data leakage?**
1. Only dispatch-time features; the delivery time is used only to build the target.
2. Vendor performance via `merge_asof(allow_exact_matches=False)` on shipments **already delivered** before dispatch.
   A naive "carrier mean delay over all data" would leak future outcomes. There is a unit test for this.
3. Chronological train/test split and `TimeSeriesSplit` for tuning. A random split would let the model learn from the
   future (and from near-identical shipments on the same day).
4. Scaler/imputer/encoder live inside the Pipeline so they are fitted on training folds only.

**Why is R2 on total delivery hours not enough?** Even "trust the SLA" scores 0.990 because total time is dominated by
distance. The informative metric is R2 / RMSE on **hours delayed**: RF 0.672 / 1.52 h vs baselines -0.21 / 2.93 h.
Say this before they ask - it shows you understand your own metric.

**Why Random Forest over Ridge?** Delay depends on interactions (rain x distance, carrier x season). Ridge is linear in
the encoded features (R2 0.30); RF captures interactions (R2 0.67). Ridge is more interpretable but misses the structure.

**Residuals - is the model biased?** Mostly no, but be honest: C04 is under-predicted by ~0.78 h because its performance keeps
drifting worse beyond what training showed; Saturday +0.56 h. Remedy: monthly retraining and residual monitoring by carrier.

**Why do the risk tiers matter?** On the test period High-tier shipments were late 92 % of the time, Medium 46 %, Low 7.5 %,
so the tiers are calibrated enough to prioritise interventions.

**What are the limits?** Synthetic data; origin-only weather; unpredictable breakdowns set a floor on error; route rankings
rest on 20-30 shipments per route.

**Separation of concerns:** `sql/` extraction, `src/dataset.py` data + weather merge, `src/features.py` transformations,
`src/modeling/` train/score, notebooks orchestrate and visualise, `src/run_pipeline.py` reproduces everything.

**Be able to explain every file you commit.** Run each notebook and change something (the vendor window, the split date,
the risk thresholds) to see the effect before the presentation.
