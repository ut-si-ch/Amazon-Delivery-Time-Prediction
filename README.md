# 📦 Amazon Delivery Time Prediction 🚚  
_End-to-End Machine Learning Project with MLOps & Streamlit_

---

## Table of Contents  
- [Problem Statement](#-problem-statement)  
- [Project Workflow](#-project-workflow)  
- [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)  
- [Model Training & Results](#-model-training--results)  
- [MLOps with MLflow](#-mlops-with-mlflow)  
- [Streamlit Application](#-streamlit-application)  
- [Repository Structure](#-repository-structure)  
- [Key Learnings](#-key-learnings)  
- [Future Improvements](#-future-improvements)  
- [Author](#-author)  

---

## Problem Statement  
In the fast-growing e-commerce ecosystem, **on-time delivery** is crucial.  
This project predicts **order delivery time** using:  

- Distance (KM)  
- Traffic & Weather conditions  
- Agent details (age, rating, vehicle)  
- Order category  

This enables businesses to optimize **logistics, ETAs, and customer satisfaction**.

---

## Project Workflow  

1. **Data Preprocessing**
   - Cleaned raw data and handled missing values.  
   - Created new features: `Distance_KM`, `Time_to_Pickup`, etc.  
   - Encoded categorical variables using **One-Hot Encoding**.  

2. **EDA & Feature Importance**
   - Identified distribution of delivery times.  
   - Plotted traffic/weather effects.  
   - Top important features:  
     - Category_Grocery  
     - Agent Rating  
     - Distance_KM  
     - Traffic Conditions  

3. **Modeling**
   - Trained and compared:  
     - Linear Regression  
     - Decision Tree  
     - Random Forest  
     - XGBoost  
     - **LightGBM (Best)**  

4. **MLOps**
   - Tracked experiments in **MLflow**.  
   - Logged metrics (MAE, RMSE, R²) and hyperparameters.  
   - Registered best-performing model.  

5. **Deployment**
   - Built **Streamlit UI** for real-time predictions.  

---

## Exploratory Data Analysis (EDA)  

### Distribution of Delivery Times & Boxplot
<div style="display: flex; justify-content: space-around;">
  <img src="https://github.com/user-attachments/assets/bf550974-acaf-4e7c-9ebf-7fea1f803355" alt="Delivery Time Distribution" width="45%"/>
  <img src="https://github.com/user-attachments/assets/8c0cd4f5-ebf0-4eff-9875-a94f04aaa98a" alt="Boxplot of Delivery Times" width="45%"/>
</div>

### Geographical Analysis
<div style="display: flex; justify-content: space-around;">
  <img src="https://github.com/user-attachments/assets/65d5418f-91fd-4c46-b83e-c075b951880c" alt="World Map" width="48%"/>
  <img src="https://github.com/user-attachments/assets/3c65dfff-6748-4401-bf0c-d09c9334e102" alt="India Map" width="48%"/>
</div>

### Agent & Rating Analysis
<div style="display: flex; justify-content: space-around;">
  <img src="https://github.com/user-attachments/assets/4b470448-c76d-49a8-ba2a-e363161d511f" alt="Agent Histogram" width="45%"/>
  <img src="https://github.com/user-attachments/assets/95fae774-de46-47ea-b4b2-b82163f84143" alt="Delivery vs Agent Rating" width="45%"/>
</div>

### Weather & Traffic Impact
<div style="display: flex; justify-content: space-around;">
  <img src="https://github.com/user-attachments/assets/a23b085e-cd4f-4124-893f-7446fc7b80a0" alt="Weather Impact" width="45%"/>
  <img src="https://github.com/user-attachments/assets/c0e570e6-d0e6-465f-be18-7a5d4b8f5d63" alt="Traffic Impact" width="45%"/>
</div>

### Product Category & Distance Analysis
<div style="display: flex; justify-content: space-around;">
  <img src="https://github.com/user-attachments/assets/1a504e4e-8f01-43ed-a3bc-c7ecc931bee0" alt="Product Category Impact" width="45%"/>
  <img src="https://github.com/user-attachments/assets/ca06d7e1-de4c-4a9b-9b81-96c9dc00bc17" alt="Distance vs Delivery Time" width="45%"/>
</div>

### Feature Importance  
<img src="https://github.com/user-attachments/assets/0b18b12b-1312-4e79-ad5b-ef88db5cf3e1" alt="Feature Importance" width="70%"/>

---

## Model Training & Results  

| Model              | MAE   | RMSE  | R²    |
|--------------------|-------|-------|-------|
| Linear Regression  | 28.32 | 36.71 | 0.54  |
| Random Forest      | 21.17 | 26.43 | 0.77  |
| XGBoost            | 18.84 | 23.51 | 0.81  |
| **LightGBM** ✅     | **17.12** | **22.10** | **0.82** |

---

## MLOps with MLflow  

- All experiments tracked in **MLflow UI**.  
- Easy comparison of multiple models.  
- Example MLflow Run:  

<img src="https://github.com/user-attachments/assets/b9a79b25-9d04-468f-929d-59842f799c5f" alt="MLflow Experiment View" width="85%"/>

---

## Streamlit Application  

### Features  
- Input: Distance, Weather, Traffic, Agent details, Order Category.  
- Output: Predicted Delivery Time.  

### Deployed App Screenshot  
<img src="https://github.com/user-attachments/assets/978f20b2-2506-4b38-ae9d-3647653c81e0" alt="Streamlit UI" width="65%"/>

---

## Key Learnings  
- Built **end-to-end ML pipeline** for regression.  
- Hands-on **MLOps**: experiment tracking & model registry using MLflow.  
- Optimized **tree-based models** with hyperparameter tuning.  
- Built **Streamlit app** for business-facing predictions.  

---

## Future Improvements  
- Add live APIs for **real-time traffic & weather**.  
- Deploy with **Docker + AWS/GCP/Azure**.  
- Automate retraining with **CI/CD pipelines**.  

---

## Author  
**Uttam Singh Chaudhary**  
- Data Science & AI Enthusiast  
- [LinkedIn](https://linkedin.com/in/uttam-singh-chaudhary) | [GitHub](https://github.com/ut-si-ch)  

---
