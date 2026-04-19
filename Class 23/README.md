# FedSpeak Analysis – NLP on FOMC Minutes

### Objective
To quantify the evolution of Federal Reserve monetary policy discourse by applying advanced Natural Language Processing (NLP) techniques and unsupervised learning to over two decades of FOMC meeting minutes.

### Methodology
* **Data Pipeline:** Ingested and preprocessed 20+ years of FOMC transcripts using a structured pipeline including tokenization, lemmatization, and domain-specific stop-word filtration.
* **Vectorization:** Engineered a high-dimensional document-term matrix using TF-IDF (Term Frequency-Inverse Document Frequency) to capture both unigram and bigram linguistic features.
* **Sentiment Modeling:** Leveraged the Loughran-McDonald financial lexicon to compute specialized sentiment scores, specifically isolating "net sentiment" and "uncertainty" metrics to track policy hawkishness and market ambiguity.
* **Dimensionality Reduction & Clustering:** Implemented Principal Component Analysis (PCA) to condense the feature space followed by K-Means clustering to identify latent thematic shifts in central bank communications.
* **Comparative Analysis:** Conducted a longitudinal study of sentiment distributions, contrasting the stable pre-COVID-19 era against the volatile post-pandemic policy landscape.

### Key Findings
* **Thematic Regimes:** Unsupervised clustering successfully identified distinct "policy regimes," grouping documents by prevailing economic anxieties such as "Systemic Liquidity Risk" versus "Inflationary Persistence."
* **Sentiment Divergence:** Analysis revealed a statistically significant increase in the "Uncertainty" index during the 2020-2022 period, which remained elevated compared to the historical 20-year baseline.
* **Structural Narrative Shift:** The post-COVID distribution showed a marked transition in linguistic priorities, with bigram analysis highlighting a move away from "quantitative easing" toward "labor market tightness" and "price stability" as dominant narrative drivers.