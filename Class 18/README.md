# Fraud Detection Model Evaluation — Metrics that Matter

**Objective:**
To evaluate the operational effectiveness of a logistic regression classifier in detecting credit card fraud within a highly imbalanced dataset, shifting the analytical focus from structurally flawed accuracy metrics to business-aligned performance indicators and capacity-constrained thresholding.

**Methodology:**
* **Data Ingestion & Preprocessing:** Processed the Kaggle Credit Card Fraud dataset, comprising 284,807 European transactions with PCA-anonymized features (V1–V28) and transaction amounts, explicitly handling the severe class imbalance (0.172% positive class).
* **Baseline Formulation:** Established a naive majority-class baseline to empirically demonstrate the "accuracy paradox" inherent in anomaly detection.
* **Model Estimation:** Estimated a regularized Logistic Regression model to predict the probability of fraudulent transactions.
* **Diagnostic Evaluation:** Computed comprehensive evaluation metrics including confusion matrices, Precision, Recall, and F1-Scores. Visualized model performance via Receiver Operating Characteristic (ROC) and Precision-Recall (PR) curves using `matplotlib` and `seaborn`.
* **Threshold Optimization & Operational Constraints:** Conducted structural threshold tuning to identify the F1-optimal operating point. Subsequently, applied a real-world business constraint—capping daily manual reviews at 500 cases—to determine the most operationally viable decision boundary.

**Key Findings:**
* **The Accuracy Paradox Quantified:** Confirmed that a naive baseline achieves 99.83% accuracy while capturing zero fraud, reinforcing that raw accuracy is a misleading key performance indicator (KPI) for highly skewed distributions.
* **Metric Superiority:** Demonstrated that while the model achieves strong ROC-AUC, the Precision-Recall Area Under the Curve (PR-AUC) provides a significantly more rigorous and informative assessment of performance on the minority class.
* **Suboptimality of Default Thresholds:** Proved that the default 0.5 probability threshold fails to minimize business costs. Calibrating the threshold to the F1-optimal point yielded a mathematically superior balance of Precision and Recall.
* **Bridging Statistics and Operations:** Successfully established an adjusted operating threshold that maximizes the capture rate of fraudulent transactions while strictly adhering to the 500-case daily investigation limit, ensuring the model remains practically deployable for a risk operations team.