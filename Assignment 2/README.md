# Audit 02: Deconstructing Statistical Lies

**Tools:** Python, NumPy, Pandas, Matplotlib, SciPy  
**Focus:** Bayesian Inference, Chi-Square Testing, Monte Carlo Simulation

## 1. Executive Summary
In an era of "data-driven" decision-making, metrics are often weaponized to mislead. This audit focuses on three specific statistical fallacies—**The False Positive Paradox**, **Sample Ratio Mismatch (SRM)**, and **Survivorship Bias**. Using Python, I built rigorous audit functions to deconstruct these claims, revealing that high "accuracy" does not equal reliability and that "average" returns are often statistical illusions.

---

## 2. The False Positive Paradox (Bayesian Analysis)
**The Scenario:** An AI plagiarism detector boasts "98% Accuracy" (Sensitivity & Specificity). In a high-stakes Honors Seminar where cheating is rare (0.1%), a student is flagged. Is he guilty?

**The Audit:**
I wrote a custom function, `bayesian_audit()`, to calculate the Posterior Probability $P(\text{Cheater} | \text{Flagged})$ rather than relying on the raw accuracy metric.

**Key Findings:**
* **Intuition:** Most people assume a 98% accurate tool implies a 98% probability of guilt.
* **Reality:** In a low-prevalence environment (0.1% base rate), the probability of guilt is only **4.68%**.
* **Conclusion:** The detector generates **~20 false positives for every 1 real cheater**. Blind reliance on "98% accuracy" in this context would lead to mass wrongful accusations.

> **Key Insight: The Base Rate Fallacy** > Even with 98% sensitivity, the False Positives from the honest majority drown out the True Positives.
> *Scenario C (Honors Seminar): Base Rate = 0.1%, P(Cheater | Flagged) = 4.67%*

---

## 3. Investigating Latency Skew (Sample Ratio Mismatch)
**The Scenario:** A fintech app ("FinFlash") ran an A/B test with 100,000 users. The Treatment group ended up with 500 fewer users than the Control group.
* *Hypothesis:* The new feature caused latency, causing users to crash/drop out before assignment (Latency Skew).

**The Audit:**
I performed a **Chi-Square Goodness of Fit Test** to determine if the deviation (50,250 vs 49,750) was statistically significant or just random noise.

**Key Findings:**
* **Chi-Square Statistic:** `2.50`
* **Critical Threshold:** `3.84` ($p=0.05$)
* **Conclusion:** Since $2.50 < 3.84$, the result was **Not Significant**.
* **Impact:** The "missing" users were due to random variance, not a system failure. We avoided a costly engineering "fix" for a problem that didn't exist.

---

## 4. Visualizing Survivorship Bias (Crypto Simulation)
**The Scenario:** Crypto media often cites the "average market cap" of successful tokens to imply high expected returns. This ignores the thousands of tokens that failed and were delisted.

**The Audit:**
I simulated 10,000 token launches using a **Pareto Distribution (Power Law)** to model realistic wealth disparity. I compared the metrics of the "Survivors" (Top 1%) against the "Graveyard" (All Launches).

**Key Findings:**
* **The Illusion:** The "Survivor Mean" (Top 1%) was **~$1.2M**.
* **The Reality:** The "True Mean" (All Tokens) was **~$33k**.
* **Bias Factor:** Viewing only survivors inflated the perceived value by **37x**.
* **Takeaway:** Any financial analysis that excludes delisted assets is fundamentally broken.

![Survivorship Bias Visualization](survivorship_bias_crypto.png)

---

## 5. Final Reflection
This audit demonstrates that **context is king**. A 98% accuracy score is worthless without a Base Rate; a "missing" cohort is meaningless without a significance test; and an "average return" is a lie without accounting for failures. As a Data Scientist, my role is to look past the summary statistic to find the underlying distribution.