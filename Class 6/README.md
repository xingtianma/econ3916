# Lab 5: The Architecture of Bias

## 1. Objective
To investigate the Data Generating Process (DGP) and quantify the hidden dangers of Sampling Bias in machine learning pipelines. This lab moves beyond "black box" model fitting to focus on the statistical validity of the data ingestion and splitting phases.

## 2. Tech Stack
* **Core:** Python, Pandas, NumPy
* **Statistical Analysis:** SciPy (`chisquare`, `stats`)
* **Machine Learning:** Scikit-Learn (`train_test_split`, `StratifiedShuffleSplit`)

## 3. Methodology & Key Implementations
* **Manual Sampling Simulation (The "Muscle Memory" Phase):**
    * Bypassed `sklearn` to manually implement array slicing and randomization using NumPy indices.
    * **Outcome:** Visualized how "Simple Random Sampling" creates significant variance (Sampling Error) in small-to-medium datasets, leading to unrepresentative training sets.
* **Stratified Sampling Implementation:**
    * Engineered a robust split using Stratified Sampling to lock the distribution of target variables (e.g., `pclass` in Titanic).
    * **Outcome:** Eliminated **Covariate Shift**, ensuring that the Training and Test sets were statistically identical reflections of the population.
* **Forensic A/B Test Audit (SRM Detection):**
    * Developed a forensic script using the **Chi-Square Goodness of Fit** test to audit A/B test assignments.
    * **Outcome:** Successfully identified "Sample Ratio Mismatch" (SRM) in a skewed 550/450 split ($p < 0.01$), distinguishing critical infrastructure failures from random chance.

---

## Theoretical Analysis: Survivorship Bias & The Heckman Correction

**Q: Why does analyzing only successful Unicorn startups lead to Survivorship Bias?**

Analyzing only Unicorns on TechCrunch creates **Selection Bias** (specifically Survivorship Bias) because you are conditioning your analysis on the outcome ($Y=1$).
* **The Flaw:** You might observe that "80% of Unicorn founders dropped out of college." Without seeing the failed companies, you cannot know if 80% of *failed* founders also dropped out. If the trait exists equally in both groups, it is not a predictor of success; it is just a common trait.
* **The Result:** Your model learns $P(Feature | Success)$ instead of the required $P(Success | Feature)$.

**Q: What specific "Ghost Data" is needed for a Heckman Correction?**

To fix this using a **Heckman Correction (Heckit Model)**, you need the data of the **failed startups** (the "invisible" or "ghost" data).

Specifically, the Heckman Correction is a two-step process that requires:
1.  **The Selection Equation (Probit):** You need a dataset containing **BOTH** successful and failed startups to model the probability of "making it into the dataset" (i.e., becoming a Unicorn).
2.  **The Correction:** This model generates a bias-correction term (the *Inverse Mills Ratio*) which is then added to your original regression on the successful startups.

**The "Ghost Data" is the full population of startups that died in obscurity.** Without them, the correction is mathematically impossible.