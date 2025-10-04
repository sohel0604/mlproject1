## End to End Data Science Project.
# 🎓 Student Performance Prediction App

This project predicts a **student’s Math score (0–100)** based on their background and previous test performance.  
It is a complete **end-to-end Machine Learning pipeline** with a modern **Streamlit web app** for easy prediction and visualization.

---

## 🚀 Project Overview
- **Goal:** Predict a student's Math score using demographic and test data.  
- **Type:** Regression (continuous value prediction).  
- **Pipeline:** Data ingestion → Preprocessing → Model training → Evaluation → Deployment (Streamlit).  
- **Best Model:** CatBoost Regressor 🐱‍👤 (based on performance metrics).  

---

## 🧠 Key Learnings
- Designed a modular ML pipeline from scratch using **custom components**.  
- Processed categorical and numerical data using **ColumnTransformer**.  
- Trained and compared models like **Linear Regression**, **Ridge**, **KNN**, **RandomForest**, **XGBoost**, **CatBoost**, and **AdaBoost**.  
- Implemented **logging** and **exception handling** for professional project structure.  
- Deployed a fully working **Streamlit web app** for real-time predictions.

---

## 📂 Folder Structure
student-performance-prediction/
│
├── artifacts/ → model.pkl & preprocessor.pkl
├── artifact/ → raw.csv, train.csv, test.csv
├── notebooks/ → EDA and Model Training notebooks
├── src/mlproject/ → core ML pipeline modules
│ ├── components/ → ingestion, transformation, training scripts
│ ├── pipelines/ → training & prediction pipelines
│ ├── logger.py, exception.py, utils.py
│
├── app.py → main entry for model training
├── streamlit_app.py → Streamlit UI for predictions
├── requirements.txt → dependencies
├── setup.py → setup configuration
└── README.md → project documentation
## 🧰 Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, CatBoost, XGBoost, Streamlit, Matplotlib, Seaborn  
- **Version Control:** Git & GitHub  

---

