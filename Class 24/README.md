# Causal ML – Double Machine Learning for 401(k) Policy Evaluation

## Objective
To robustly estimate the causal impact of 401(k) eligibility on net financial assets by leveraging Double Machine Learning to overcome the regularization bias inherent in naive predictive modeling.

## Methodology
* **Regularization Bias Demonstration:** Simulated a Data Generating Process (DGP) with a known treatment effect (True ATE = 5.0) to empirically demonstrate the attenuation bias caused by the naive application of LASSO regularization in causal estimation.
* **DoubleML Framework:** Implemented a Partially Linear Regression (PLR) model via the `DoubleML` library to isolate the causal effect of 401(k) eligibility on wealth.
* **Nuisance Parameter Estimation:** Utilized Random Forest estimators to flexibly control for high-dimensional confounding covariates without imposing strict parametric assumptions.
* **Cross-Fitting:** Applied 5-fold cross-fitting to eliminate overfitting-induced bias during the estimation of nuisance functions.
* **Heterogeneity Analysis:** Estimated Conditional Average Treatment Effects (CATE) stratified by income quartiles to systematically analyze treatment effect heterogeneity.
* **Visualization:** Generated coefficient plots with robust confidence intervals to compare CATE estimates across income subgroups.

## Key Findings
* **Average Treatment Effect (ATE):** 401(k) eligibility increases net financial assets by approximately **$[INSERT_ATE_HERE]**.
* **Treatment Effect Heterogeneity (CATE):** The causal impact varies across the income distribution. The estimated effect for the highest income quartile is approximately **$[INSERT_Q4_CATE]**, compared to **$[INSERT_Q1_CATE]** for the lowest quartile. This indicates **[INSERT_DIRECTION_OF_HETEROGENEITY, e.g., stronger wealth accumulation effects among higher earners]**.
* **Methodological Validation:** As demonstrated on simulated data, naive machine learning approaches (e.g., standard LASSO) severely biased the treatment coefficient toward zero, confirming the absolute necessity of orthogonal score techniques (DoubleML) for valid causal inference.