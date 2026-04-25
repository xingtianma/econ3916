
This project predicts the winning team of a League of Legends match based on early-game statistics recorded at the 10-minute mark. It includes a complete data analysis pipeline and an interactive Streamlit dashboard.

## Reproducibility Instructions

Follow the steps below to clone this repository and reproduce the results on your local machine.

### 1. Environment Setup

First, clone the repository and navigate into the project directory:

```bash
git clone <your-repository-url>
cd <your-repository-folder-name>
```

Next, install all required Python dependencies. It is recommended to do this within a virtual environment to avoid conflicts:

```bash
pip install -r requirements.txt
```

### 2. Data Acquisition

You do not need to download the dataset manually. The data acquisition is handled automatically within the analysis pipeline. The project uses the `kagglehub` library to fetch the "League of Legends Diamond Ranked Games (10 min)" dataset directly from Kaggle when you execute the notebook.

### 3. How to Run the Analysis Pipeline

The core analysis, data exploration, model training, and evaluation are contained within the Jupyter Notebook. 

1. Open `checkpoint.ipynb` using Jupyter Notebook, JupyterLab, or your preferred IDE (like VS Code).
2. Run the cells sequentially from top to bottom. This will automatically download the data, train the Logistic Regression model, evaluate its accuracy, and generate the necessary `.pkl` files (model and scaler).

### 4. How to Launch the Streamlit App Locally

The interactive web dashboard is built using Streamlit. To run it on your own machine:

1. Ensure that the generated model artifacts (`logreg_model.pkl` and `scaler.pkl`) are located in the same directory as the `app.py` script.
2. Run the following command in your terminal:

```bash
streamlit run app.py
```

This will start a local server and automatically open the interactive dashboard in your default web browser.