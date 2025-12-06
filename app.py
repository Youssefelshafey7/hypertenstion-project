import streamlit as st
import pandas as pd

# Import your model scripts
import randomforest as rf
import knn as knn

st.title("Hypertension Prediction System")
st.write("GUI connected to Random Forest + KNN model files.")

# Load encoders and scaler from your files
encoders = rf.get_encoders()
scaler = knn.get_scaler()

# User inputs
age = st.number_input("Age", 1, 120, 40)
salt = st.number_input("Salt Intake", 0.0, 20.0, 8.0)
stress = st.number_input("Stress Score", 1, 10, 5)
bp = st.selectbox("BP History", encoders["BP_History"].classes_)
sleep = st.number_input("Sleep Duration", 0.0, 12.0, 7.0)
bmi = st.number_input("BMI", 10.0, 50.0, 23.5)
med = st.selectbox("Medication", encoders["Medication"].classes_)
fam = st.selectbox("Family History", encoders["Family_History"].classes_)
exercise = st.selectbox("Exercise Level", encoders["Exercise_Level"].classes_)
smoke = st.selectbox("Smoking Status", encoders["Smoking_Status"].classes_)

# Prepare input
user_df = pd.DataFrame([{
    "Age": age,
    "Salt_Intake": salt,
    "Stress_Score": stress,
    "BP_History": bp,
    "Sleep_Duration": sleep,
    "BMI": bmi,
    "Medication": med,
    "Family_History": fam,
    "Exercise_Level": exercise,
    "Smoking_Status": smoke
}])

# Encode values using the same encoders used in training
for col in user_df.columns:
    if col in encoders:
        user_df[col] = encoders[col].transform(user_df[col])

# Predict
if st.button("Predict"):
    # RF prediction
    rf_pred = rf.predict_rf(user_df)

    # KNN prediction (scaled)
    scaled_df = scaler.transform(user_df)
    knn_pred = knn.predict_knn(scaled_df)

    st.subheader("Results:")
    st.write(f"🔹 Random Forest: **{'Hypertension' if rf_pred == 1 else 'Normal'}**")
    st.write(f"🔹 KNN: **{'Hypertension' if knn_pred == 1 else 'Normal'}**")
