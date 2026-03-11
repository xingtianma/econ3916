### Mitigating Spurious Correlation in Macroeconomic Time-Series

**Project Overview**
This project explores the analytical risks of spurious correlation and multicollinearity when modeling macroeconomic time-series data sourced from the FRED API. 

**Methodology**
* **Visualizing Correlation Traps:** Utilized Python, Pandas, and Seaborn to build correlation matrices, highlighting the deceptive, trend-driven relationships present in raw, non-stationary level data.
* **Redundancy Diagnostics:** Applied Variance Inflation Factor (VIF) scoring via the Statsmodels library to systematically quantify multicollinearity and feature redundancy. 
* **Stationarity Transformation:** Mitigated statistical noise by transforming raw variables into stationary Year-over-Year (YoY) growth rates.
* **Causal Mapping:** Employed Directed Acyclic Graphs (DAGs)  to map out and isolate the true underlying structural relationships between the economic indicators.

**Technologies Used:** Python, Pandas, Seaborn, Statsmodels, FRED API