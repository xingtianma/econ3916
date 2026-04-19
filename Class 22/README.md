# Clustering World Economies with K-Means & PCA

### Objective
To identify latent socioeconomic patterns in global development data by applying unsupervised machine learning techniques to a multidimensional feature space of World Bank indicators.

### Methodology
* **Data Acquisition & Feature Engineering:** Programmatically retrieved 10 key development indicators for approximately 160 countries via the World Bank API (`wbgapi`), focusing on metrics such as GDP per capita, life expectancy, and infrastructure access.
* **Feature Standardization:** Applied `StandardScaler` to normalize features, ensuring that variables with higher absolute scales (e.g., GDP) did not disproportionately influence the Euclidean distance calculations within the clustering algorithm.
* **Dimensionality Reduction:** Utilized Principal Component Analysis (PCA) to compress the high-dimensional indicator space into a 2D coordinate system for visualization and to improve the signal-to-noise ratio of the clusters.
* **Hyperparameter Optimization:** Conducted heuristic evaluations using the **Elbow Method** (Within-Cluster Sum of Squares) and **Silhouette Analysis** to determine the statistically optimal number of clusters ($K$) between a range of 2 and 10.
* **Algorithmic Validation:** Performed a cross-tabulation analysis of the resulting algorithmic clusters against established World Bank income classifications (High, Middle, and Low income) to measure the alignment between data-driven groupings and traditional economic labels.
* **Comparative Scalability:** Extended the analytical pipeline to California Housing census tract data to evaluate the framework's robustness across disparate geographic and socioeconomic scales.

### Key Findings
* **Optimal Cluster Identification:** The Elbow and Silhouette analyses suggested that **$K=4$** provided the most meaningful separation, effectively balancing model complexity with cohesive group membership.
* **Income Group Alignment:** The algorithmic clusters demonstrated high fidelity with World Bank income classifications, particularly in distinguishing between High-Income and Low-Income economies. However, the model revealed significant "boundary economies" in the middle-income tiers, suggesting that development involves complex transitions that exceed simple GDP-based categorization.
* **Structural Nuance:** By including indicators like internet penetration and primary school enrollment alongside financial metrics, the model identified subgroups of nations that outperform their income peers in social infrastructure, highlighting the multidimensional nature of global development.