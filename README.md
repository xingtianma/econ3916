# 📊 Economic Data Science Portfolio

Welcome to my academic portfolio for **ECON 3916: Statistical & Machine Learning for Economics**.  
This repository documents my progression from classical econometric foundations to modern machine learning methods, with an emphasis on applying data-driven tools to economic questions.

---

## 👋 About Me

I am an undergraduate economics student preparing for roles in **Data Analysis, Economic Consulting, and Finance**.  
My academic focus is on bridging **traditional economic theory** with **modern statistical and machine learning techniques** to better understand, model, and predict real-world economic behavior.

This portfolio reflects both my technical development and my approach to learning: building from first principles and extending them into more powerful, scalable methods.

---

## 📁 About This Portfolio

This repository contains coursework, labs, and experiments developed throughout ECON 3916. The course follows a **concept extension philosophy**, where foundational statistical ideas—such as linear regression—are gradually expanded into machine learning frameworks.

Key themes include:
- Moving from **causal inference** to **predictive modeling**
- Understanding trade-offs between interpretability and performance
- Applying regularization and model selection techniques (e.g., Lasso)
- Using empirical methods to answer economic questions with data

Each folder represents a step in this learning process, combining theory, implementation, and interpretation.

---

## 🧠 Skills & Focus Areas

- Statistical modeling and inference  
- Machine learning for economic data  
- Regression, regularization, and prediction  
- Translating economic intuition into data-driven models  

---

## 🛠️ Tech Stack

- 🐍 **Python** – Core programming language  
- 🧮 **Pandas & NumPy** – Data manipulation and numerical computing  
- 🤖 **Scikit-learn** – Machine learning models and pipelines  
- 📈 **Statsmodels** – Econometric and statistical analysis  
- ☁️ **Google Colab** – Experimentation and reproducible notebooks  

---

### **Return-Aware Experimentation vs. The Academic Standard**

* **The Concept:** At companies like Netflix, **Return-Aware Experimentation** treats the decision to launch a feature as a trade-off between the cost of a false positive and the potential business upside.
* **The Difference:** While the academic standard of p < 0.05 is a rigid convention designed to prevent false discoveries in science, Netflix views the **p-value** as a tunable business parameter. 
* **The Logic:** If a feature has a massive potential "return" and a low cost of implementation, a lower confidence threshold (e.g., p < 0.10 or 0.20) may be mathematically optimal to avoid the high "opportunity cost" of rejecting a winner.
* **The Portfolio Note:** I understand that **Decision Thresholds** are not just scientific hurdles but strategic parameters; choosing a significance level is an act of balancing the risk of a "Type I" error (false alarm) against the "Type II" error (missed opportunity) based on specific business impact.

# Macroeconomic Time-Series Analysis: Navigating Spurious Correlation

**Objective:** To demonstrate and resolve common statistical traps—specifically spurious correlation and multicollinearity—in macroeconomic time-series data retrieved via the FRED API.

**Tools & Technologies:** Python, pandas, seaborn, statsmodels, FRED API, DAGs.

## Methodology

* **Exploratory Data Analysis:** Ingested raw level data and visualized initial relationships using pandas and seaborn to highlight the illusion of high correlation in non-stationary variables.
* **Statistical Diagnostics:** Applied Variance Inflation Factor (VIF) analysis using statsmodels to rigorously quantify multicollinearity and identify redundant variables.
* **Data Transformation:** Transformed non-stationary raw data into Year-over-Year (YoY) growth rates to achieve stationarity and eliminate time-trend biases.
* **Causal Mapping:** Utilized Directed Acyclic Graphs (DAGs) to move beyond simple correlation, mapping the true underlying structural and causal relationships between the macroeconomic indicators.

## 🚀 Looking Ahead

This portfolio is a living project that will continue to grow as I deepen my understanding of statistical learning and its applications in economics. My goal is to develop models that are not only predictive, but also economically meaningful.

Thank you for visiting!

