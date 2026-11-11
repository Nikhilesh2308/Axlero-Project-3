# Tableau build guide - Operations Dashboard

**Design rule:** use ONE table (`data/processed/ops_dashboard_data.csv`) and **no relationships**. Every chart below can be
built from it, which avoids the "same field name in two tables" problem (e.g. two different `revenue` columns) that causes wrong numbers.

## 1. Connect and set types
1. Connect -> Text file -> `ops_dashboard_data.csv`.
2. Data Source tab: set `shipment_id` to **String**; `dispatch_date`, `month_start` to **Date**; `dispatch_time` to **Date & Time**.

## 2. Calculated fields
```
High Risk Shipments    COUNTD(IF [risk_tier] = "High" THEN [shipment_id] END)
Actual Late Rate       AVG([actual_late])
Predicted Late Rate    AVG([predicted_late])
RMSE (h)               SQRT(AVG([residual_h] * [residual_h]))
```

## 3. Sheets
| Sheet | Build |
|---|---|
| **KPI Shipments** | Text: `COUNTD(shipment_id)` |
| **KPI Late Rate** | Text: Actual Late Rate (format Percentage, 1 decimal) |
| **KPI High Risk** | Text: High Risk Shipments |
| **KPI RMSE** | Text: RMSE (h) (2 decimals) |
| **Top risk routes** | Rows: `route`. Columns: Predicted Late Rate. Color: `origin_region`. Filters: *Top 12 by Predicted Late Rate* (right-click route -> Filter -> Top) **and** `COUNTD(shipment_id)` >= 20 (add the measure to Filters, choose At least 20). Sort descending |
| **Risk mix by carrier** | Columns: `carrier_name`. Rows: `COUNTD(shipment_id)`. Color: `risk_tier` (Low green #59a14f, Medium yellow #edc948, High red #e15759). Mark: Bar |
| **Late rate trend** | Columns: `month_start` (continuous Month). Rows: Measure Values filtered to Actual Late Rate and Predicted Late Rate (drag both onto Measure Values; Color = Measure Names). Mark: Line with circles |
| **Actual vs predicted** | Analysis -> untick *Aggregate Measures*. Columns: `hours_delayed`. Rows: `predicted_delay_h`. Color: `risk_tier`. Add a reference line y = x if you like |
| **High-risk worklist** | Rows: `shipment_id`, `dispatch_time`, `carrier_name`, `route`, `distance_km`, `sla_hours`, `predicted_delay_h`. Filter `risk_tier` = High. Sort by `predicted_delay_h` descending |

## 4. Assemble (1400 x 800)
1. New Dashboard -> Size: **Fixed size 1400 x 800**.
2. Drag an **Image** object -> choose `dashboard/backgrounds/dashboard_bg_with_cards_1400x800.png` -> **Floating**, X 0, Y 0, W 1400, H 800 -> send to the bottom of the Item hierarchy.
3. Make every sheet **Floating** and enter the positions (Layout tab):

| Item | X | Y | W | H |
|---|---|---|---|---|
| KPI Shipments | 14 | 89 | 280 | 97 |
| KPI Late Rate | 312 | 89 | 280 | 97 |
| KPI High Risk | 609 | 89 | 280 | 97 |
| KPI RMSE | 907 | 89 | 280 | 97 |
| Top risk routes | 14 | 206 | 280 | 300 |
| Risk mix by carrier | 312 | 206 | 280 | 300 |
| Late rate trend | 609 | 206 | 280 | 300 |
| Actual vs predicted | 907 | 206 | 280 | 300 |
| High-risk worklist | 14 | 526 | 1172 | 260 |
| Filters + legends | 1204 | 89 | 182 | 697 |

4. Format -> Shading -> Worksheet = None (so the white panels show through). Hide sheet titles. Title text white on the navy band.
5. Filters (right-hand panel): `origin_region`, `carrier_name`, `risk_tier`, `month_start`. For each: dropdown -> **Apply to Worksheets -> All Using This Data Source**.
6. Click **Use as Filter** on *Top risk routes* and *Risk mix by carrier*; add a **Highlight** action on `carrier_name` (Dashboard -> Actions).
7. Save as `dashboard/ops_dashboard.twbx` (File -> Save As -> Packaged Workbook) and commit it.

## 5. Sanity checks (numbers you should see)
* Shipments = **6,000**; Actual late rate about **22 %** (test period; 17 % over the full two years); High-risk shipments = **488**; RMSE = **1.52**.
* Risk mix: High tier is only ~8 % of shipments. Carriers C04/C06/C08 should show the largest red share.
