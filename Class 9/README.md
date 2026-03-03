# Recovering Experimental Truths via Propensity Score Matching

## Objective
To systematically eliminate selection bias in observational data, isolating the true causal impact of an intervention when randomized control trials are unavailable.

## Methodology
* **Selection Bias Modeling:** Addressed non-random assignment in the observational subset of the Lalonde dataset by estimating the probability of treatment (propensity score) based on pre-intervention covariates.
* **Algorithm Implementation:** Built a logistic regression propensity model and developed a nearest-neighbor matching algorithm to pair treated and control units, creating a balanced pseudo-population.
* **Tech Stack:** Engineered the data processing, matching pipeline, and post-matching balance evaluations utilizing Python, Pandas, and Scikit-Learn.

## Key Findings
* **Bias Identification:** Demonstrated the severe distortion caused by unobserved confounding; the naive observational estimate yielded a deeply flawed Average Treatment Effect (ATE) of -$15,204.
* **Causal Recovery:** Successfully recovered the true, positive causal effect of approximately +$1,800 after applying the matching framework, robustly correcting the observational failure and aligning with experimental benchmarks.