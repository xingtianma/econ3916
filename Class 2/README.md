# The Illusion of Growth & the Composition Effect  
**Deflating History with FRED**

## Objective
This project investigates long-run U.S. wage growth by distinguishing between nominal wages, real purchasing power, and statistical distortions that arise during economic shocks. Using live data from the Federal Reserve Economic Data (FRED) API, the analysis evaluates whether observed wage increases reflect genuine improvements in worker compensation or are driven by compositional biases in the labor force.

## Methodology
- Built a Python data pipeline to ingest and process macroeconomic time-series data directly from the FRED API.
- Retrieved nominal average hourly earnings (AHETPI) and Consumer Price Index (CPI) data to construct an inflation-adjusted real wage series.
- Visualized long-run trends to highlight the “money illusion,” where nominal wage growth masks stagnation in real purchasing power.
- Identified an apparent wage spike in 2020 and tested its validity.
- Incorporated the Employment Cost Index (ECI), which holds job composition constant, to control for the composition effect caused by disproportionate job losses among low-wage workers during the COVID-19 pandemic.
- Rebased and compared series to isolate artificial movements from true underlying wage growth.

**Tech Stack:** Python, fredapi, pandas, matplotlib

## Key Findings
- Despite steady nominal wage growth over the past five decades, real wages show minimal long-term improvement after accounting for inflation.
- The sharp rise in average wages observed in 2020 represents a statistical artifact rather than a genuine increase in labor demand or worker bargaining power.
- When controlling for labor-force composition using the Employment Cost Index, wage growth during the pandemic period remains comparatively stable.
- This “Pandemic Paradox” illustrates how aggregate averages can mislead economic interpretation during periods of structural disruption.
