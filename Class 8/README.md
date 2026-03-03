# Hypothesis Testing & Causal Evidence Architecture

## Objective
In data science, simply estimating effects is often insufficient; true rigor requires stress-testing our assumptions. This project represents a deliberate pivot from standard 'Estimation' to strict 'Falsification'. Using the Lalonde (1986) dataset as our foundation, the objective was to operationalize the scientific method to adjudicate between competing narratives of causality regarding job training programs. By attempting to falsify our own hypotheses, we establish a much higher burden of proof for causal claims.

## Technical Approach
To ensure our findings were robust against the realities of real-world data, the analysis leveraged a dual-testing architecture using `scipy`:
* **Parametric Evaluation:** Computed the signal-to-noise ratio utilizing Welch’s T-Test. This allowed us to estimate the Average Treatment Effect (ATE) of the job training program while relaxing the assumption of equal population variances. 
* **Non-Parametric Validation:** Designed and executed a Permutation Test utilizing 10,000 resamples. This served as a critical robustness check to validate our initial results against the heavily skewed, non-normal distribution typical of real earnings data.
* **Error Control:** The testing pipeline was strictly calibrated to control for Type I errors (false positives), ensuring that any detected lift was practically and statistically significant.

*Key Result: The architecture successfully isolated a statistically significant lift in real earnings (~$1,795), decisively rejecting the Null Hypothesis via proof by statistical contradiction.*

## Business Insight
In an era of hyper-scaled data and automated modeling, rigorous hypothesis testing acts as the fundamental 'Safety Valve' of the algorithmic economy. Without a strict framework of falsification, organizations are incredibly vulnerable to data grubbing, p-hacking, and deploying capital based on spurious correlations. By anchoring our analytic workflows in structural hypothesis testing, we prevent noise from masquerading as signal, ensuring that strategic business decisions are driven by verifiable, causal reality.