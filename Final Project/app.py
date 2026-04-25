import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# ==========================================
# 1. SETUP & MODEL LOADING
# ==========================================
st.set_page_config(page_title="LoL 10-Min Predictor", layout="wide")
st.title("League of Legends: 10-Minute Match Predictor")
st.markdown("Adjust the early game statistics in the sidebar to see how they impact the probability of the Blue Team winning.")

# Load the model and scaler (wrapped in a try-except block to handle missing files gracefully)
try:
    model = joblib.load('logreg_model.pkl')
    scaler = joblib.load('scaler.pkl')
except FileNotFoundError:
    st.error("Model or scaler not found. Please ensure 'logreg_model.pkl' and 'scaler.pkl' are in the same directory as this script.")
    st.stop()

# ==========================================
# 2. PARAMETER CONTROLS (Rubric Requirement)
# ==========================================
st.sidebar.header("Adjust 10-Minute Stats")

# Sliders and widgets for the features we chose
gold_diff = st.sidebar.slider(
    "Blue Gold Difference", 
    min_value=-10000, max_value=10000, value=0, step=100,
    help="Positive means Blue team is ahead in gold."
)
exp_diff = st.sidebar.slider(
    "Blue Experience Difference", 
    min_value=-10000, max_value=10000, value=0, step=100,
    help="Positive means Blue team has an XP advantage."
)
blue_kills = st.sidebar.number_input(
    "Blue Team Kills", 
    min_value=0, max_value=50, value=5
)
blue_dragons = st.sidebar.selectbox(
    "Blue Team Dragons Secured", 
    options=[0, 1]
)

# Compile user inputs into a DataFrame
input_data = pd.DataFrame({
    'blueGoldDiff': [gold_diff],
    'blueExperienceDiff': [exp_diff],
    'blueKills': [blue_kills],
    'blueDragons': [blue_dragons]
})

# Scale the data using the same scaler fitted on the training data
input_scaled = scaler.transform(input_data)

# ==========================================
# 3. PREDICTION & UNCERTAINTY (Rubric Requirement)
# ==========================================
st.subheader("Match Prediction")

# Get prediction (0 or 1) and probabilities
prediction = model.predict(input_scaled)[0]
probabilities = model.predict_proba(input_scaled)[0]

# Extract specific probabilities
blue_win_prob = probabilities[1]
red_win_prob = probabilities[0]

# Display the prediction with confidence/uncertainty intervals
col1, col2 = st.columns(2)

with col1:
    if prediction == 1:
        st.success(f"🏆 **Predicted Winner: Blue Team**")
    else:
        st.error(f"🏆 **Predicted Winner: Red Team**")

with col2:
    st.info(f"**Model Confidence:**\n* Blue Win: {blue_win_prob * 100:.1f}%\n* Red Win: {red_win_prob * 100:.1f}%")

st.divider()

# ==========================================
# 4. INTERACTIVE VISUALIZATION (Rubric Requirement)
# ==========================================
st.subheader("Interactive Feature Analysis: Win Probability vs. Gold Difference")
st.markdown("This chart updates dynamically based on the exact stats you entered above, showing how gaining or losing gold would shift the outcome.")

# Generate an array of gold differences to plot against
gold_range = range(-6000, 6000, 200)
win_probabilities = []

# Calculate probability for each gold difference point while holding other inputs constant
for g in gold_range:
    temp_df = pd.DataFrame({
        'blueGoldDiff': [g],
        'blueExperienceDiff': [exp_diff], # Locked to user's sidebar input
        'blueKills': [blue_kills],        # Locked to user's sidebar input
        'blueDragons': [blue_dragons]     # Locked to user's sidebar input
    })
    temp_scaled = scaler.transform(temp_df)
    prob = model.predict_proba(temp_scaled)[0][1] # Get probability of class 1 (Blue Win)
    win_probabilities.append(prob)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(list(gold_range), win_probabilities, color='blue', linewidth=2)

# Plot a red dot representing the user's specific input on the curve
ax.scatter([gold_diff], [blue_win_prob], color='red', s=100, zorder=5, label='Your Current Scenario')

# Add formatting to the chart
ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.7)
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.7)
ax.set_xlabel("Blue Gold Difference at 10 Minutes")
ax.set_ylabel("Probability of Blue Team Winning")
ax.set_ylim(0, 1)
ax.legend()
ax.grid(alpha=0.3)

# Render the plot in Streamlit
st.pyplot(fig)