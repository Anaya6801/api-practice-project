import streamlit as st
import datetime

st.set_page_config(page_title="Hospital Readmission Predictor", page_icon="🏥")

st.title("🏥 Hospital Readmission Predictor")
st.write("Fill out the information below. The prediction model will be added later.")

# --- User Inputs ---
st.header("Patient Information")

age = st.number_input("Age", min_value=0, max_value=120, step=1)

gender = st.selectbox("Gender", ["Male", "Female", "Other"])

disease = st.selectbox(
    "Disease Category",
    [
        "Heart Failure",
        "Diabetes",
        "COPD",
        "Kidney Disease",
        "Other"
    ]
)

last_admission = st.date_input(
    "Last Admission Date",
    value=datetime.date.today()
)

med_count = st.number_input(
    "Number of Medications",
    min_value=0,
    max_value=50,
    step=1
)

# --- Submit Button ---
if st.button("Submit Information"):
    st.subheader("📋 Submitted Data")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Disease:** {disease}")
    st.write(f"**Last Admission Date:** {last_admission}")
    st.write(f"**Medication Count:** {med_count}")

    st.info("This UI is ready. The prediction model will be connected later.")
