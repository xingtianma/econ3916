## The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

### Objective
To architect a multivariate hedonic pricing model utilizing 2026 California real estate metrics and manually execute the Frisch-Waugh-Lovell (FWL) theorem to mathematically validate algorithmic *ceteris paribus*.

### Methodology
*   **Data Pipeline & Baseline Modeling:** Leveraged Python 3.10+, `pandas`, and `statsmodels.formula.api` to process synthetic Zillow market data and estimate both naive and multivariate Ordinary Least Squares (OLS) regressions.
*   **Variance Partitioning:** Systematically partialled out the confounding spatial variance by regressing both the dependent variable (`Sale_Price`) and the primary independent variable (`Property_Age`) against the confounder (`Distance_to_Tech_Hub`).
*   **Residual Extraction:** Extracted the orthogonal error terms (residuals) from these auxiliary regressions, effectively isolating the pure variance of property age and sale price completely independent of geographic tech proximity.
*   **Mathematical Validation:** Regressed the isolated price residuals against the isolated age residuals to manually execute the FWL theorem, relying on `matplotlib` for diagnostic visualizations of the orthogonalized data.

### Key Findings
The initial naive model exhibited severe Omitted Variable Bias (OVB), falsely attributing inflated pricing power to the physical age of the home by failing to account for the hidden spatial dynamics of tech hub proximity. By manually applying the FWL theorem to strip out this shared covariance, the analysis successfully isolated the true marginal penalty of property aging. The exact mathematical convergence between the manual residual regression and the multivariate OLS output explicitly proves the algorithm's internal correction mechanism, demonstrating exactly how multivariate regression controls for confounding variables in high-dimensional space.