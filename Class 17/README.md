# NY Fed Yield Curve Recession Model Replication

## Objective
This project replicates the Federal Reserve Bank of New York's probability model for predicting US economic recessions 12 months ahead, utilizing logistic regression on the 10-Year minus 3-Month Treasury yield spread.

## Methodology
* **Data Acquisition & Engineering:** Sourced time-series macroeconomic data via the FRED API (`T10Y3M` yield spread and `USREC` indicators) spanning from 1970 to the present. Resampled daily spread data to a monthly frequency and applied a 12-month forward lag to construct the predictive feature matrix.
* **Baseline Evaluation:** Built a baseline Linear Probability Model (LPM) utilizing `scikit-learn`, explicitly demonstrating the structural limitations of OLS for binary classification (i.e., generating logically impossible probabilities outside the $[0, 1]$ bound on real-world data).
* **Logistic Regression Modeling:** Fitted a logistic S-curve to properly model the binary NBER recession outcomes based on the lagged yield spread.
* **Statistical Inference:** Leveraged `statsmodels` to extract coefficients, standard errors, odds ratios, and 95% confidence intervals, enabling rigorous econometric interpretation of the spread parameter.

## Key Findings
* **Structural Validation:** Demonstrated the necessity of logistic regression over linear probability models for macroeconomic binary classification by visualizing the out-of-bounds errors of the OLS approach.
* **Quantifiable Risk:** Successfully extracted the yield spread odds ratio with a 95% confidence interval, quantifying the exact impact of yield curve steepening (or inversion) on future recession probabilities.
* **Historical Anomalies:** Generated the historical recession probability time series. The model accurately mapped prior NBER recessions but highlighted the contested 2022–2024 inversion period. During this window, the model signaled significantly elevated recession risk, though no NBER recession materialized, illustrating the nuances of interpreting probabilistic forecasts in highly unusual macroeconomic environments.