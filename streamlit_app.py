import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Student Math Score Predictor 🎓",
    page_icon="📊",
    layout="centered"
)

# -------------------------------
# Header
# -------------------------------
st.markdown(
    """
    <div style='text-align: center; padding: 10px'>
        <h1>🎓 Student Math Score Predictor</h1>
        <p style='font-size:18px;'>Predict a student's <b>Math Score</b> based on their details and past performance.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Load model and preprocessor
# -------------------------------
try:
    model = pickle.load(open("artifacts/model.pkl", "rb"))
    preprocessor = pickle.load(open("artifacts/preprocessor.pkl", "rb"))
    st.sidebar.success("✅ Model and Preprocessor Loaded Successfully!")
except Exception as e:
    st.sidebar.error(f"⚠️ Error loading model/preprocessor: {e}")

# -------------------------------
# Sidebar Information
# -------------------------------
st.sidebar.header("About this App 📘")
st.sidebar.write("""
This app predicts the **Math Score** of a student 
based on their background and previous scores.  
Built with **Streamlit, CatBoost, and Scikit-learn**.
""")

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 *Created by Sohel Kumar*")

# -------------------------------
# Input Fields
# -------------------------------
st.subheader("🧍‍♂️ Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["male", "female"])
    race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parent_education = st.selectbox("Parental Level of Education", [
        "some high school", "high school", "some college",
        "associate's degree", "bachelor's degree", "master's degree"
    ])

with col2:
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.slider("Reading Score", 0, 100, 70)
    writing_score = st.slider("Writing Score", 0, 100, 70)

# -------------------------------
# Create DataFrame
# -------------------------------
input_data = pd.DataFrame({
    'gender': [gender],
    'race/ethnicity': [race_ethnicity],
    'parental level of education': [parent_education],
    'lunch': [lunch],
    'test preparation course': [test_prep],
    'reading score': [reading_score],
    'writing score': [writing_score]
})


st.markdown("---")
st.write("### 👇 Input Summary")
st.dataframe(input_data, use_container_width=True)

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔮 Predict Math Score"):
    try:
        transformed = preprocessor.transform(input_data)
        prediction = model.predict(transformed)
        score = round(prediction[0])
        score = max(0, min(100, score))


        st.markdown(
            f"""
            <div style='text-align:center; background-color:#F0F8FF; padding:20px; border-radius:10px;'>
                <h2>🎯 Predicted Math Score: <span style='color:#2E8B57;'>{score}</span></h2>
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Made with ❤️ by **Sohel** | Student Performance ML Project (Regression)")
