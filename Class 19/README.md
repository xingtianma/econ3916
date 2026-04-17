# Tree-Based Models — Random Forests

**Objective:**
To evaluate and optimize tree-based ensemble methods against linear models for real estate valuation and classification tasks, demonstrating the superior non-linear predictive capabilities of Random Forests.

**Methodology:**
* **Data Ingestion:** Processed the California Housing dataset, comprising 20,640 observational units and 8 core economic and geographic features.
* **Model Benchmarking:** Estimated and compared baseline performance across a single Decision Tree Regressor, an L2-regularized Ridge Regressor, and an unoptimized Random Forest Regressor.
* **Hyperparameter Optimization:** Conducted an exhaustive cross-validated grid search (`GridSearchCV`) to optimize the Random Forest architecture, tuning critical parameters including `n_estimators`, `max_depth`, and `max_features` to minimize mean squared error.
* **Feature Importance Analysis:** Extracted and contrasted Mean Decrease in Impurity (MDI) importance from the training set against model-agnostic Permutation Importance evaluated on the holdout test set to identify primary drivers of housing value.
* **Classification Extension:** Engineered a binary classification target (above/below median price) and compared the discriminatory power of a Random Forest Classifier against a baseline Logistic Regression model using ROC-AUC metrics.
* **Interactive Visualization:** Developed a dynamic, interactive dashboard utilizing Plotly and `ipywidgets` to visually demonstrate the impact of hyperparameter adjustments on model convergence and feature importance in real-time.

**Key Findings:**
* **Predictive Superiority:** The tuned Random Forest model significantly outperformed linear approaches, achieving an out-of-sample $R^2$ of 0.8158, compared to the Ridge regression baseline $R^2$ of 0.5759.
* **Discriminatory Power:** In the classification task, the Random Forest classifier demonstrated vastly superior discriminatory capability, achieving a ROC-AUC of 0.9611 versus the Logistic Regression's 0.9087.
* **Structural Trade-offs:** While the Random Forest architecture provides a massive advantage in predictive accuracy, it introduces non-linear complexities that necessitate rigorous feature importance validation (Permutation over MDI) to ensure economic interpretability.
* **Diminishing Returns on Scale:** Interactive analysis revealed that increasing the number of estimators (`n_estimators`) yields rapid initial improvements in test $R^2$, but hits a strict performance ceiling, highlighting the necessity of optimized parameter tuning over sheer computational scale.