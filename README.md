<img width="1231" height="666" alt="image" src="https://github.com/user-attachments/assets/7e33f543-5ec8-40d4-94d8-ee3495e46f2d" /># 📦 Amazon Delivery Time Prediction 🚚  
_End-to-End Machine Learning Project with MLOps & Streamlit_

---

##  Table of Contents  
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

##  Problem Statement  
In the fast-growing e-commerce ecosystem, **on-time delivery** is crucial.  
This project predicts **order delivery time** using:  

- Distance (KM)  
- Traffic & Weather conditions  
- Agent details (age, rating, vehicle)  
- Order category  

This allows companies to optimize **logistics, ETAs, and customer satisfaction**.

---

##  Project Workflow  

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

### 1. Distribution of Delivery Times  
![Delivery Time Distribution](https://github.com/user-attachments/assets/your-image-id-1)<img width="863" height="553" alt="Distribution of Delivery Times" src="https://github.com/user-attachments/assets/bf550974-acaf-4e7c-9ebf-7fea1f803355" />

### 2. Boxplot of Delivery Times 
![Boxplot of Delivery Times]<img width="695" height="539" alt="download" src="https://github.com/user-attachments/assets/8c0cd4f5-ebf0-4eff-9875-a94f04aaa98a" />

### 3. Geographical Map
![Geographical Map]<img width="1278" height="682" alt="World Map" src="https://github.com/user-attachments/assets/65d5418f-91fd-4c46-b83e-c075b951880c" />
<img width="1231" height="666" alt="India_image" src="https://github.com/user-attachments/assets/3c65dfff-6748-4401-bf0c-d09c9334e102" />

### 4. Histogram for Agent Performance Analysis
![Histogram for Agent Performance Analysis]<img width="872" height="553" alt="download" src="https://github.com/user-attachments/assets/4b470448-c76d-49a8-ba2a-e363161d511f" />


### 5. Box Plot View for Delivery Time vs. Agent Rating  
![Box Plot View for Delivery Time vs. Agent Rating]<img width="854" height="553" alt="download" src="https://github.com/user-attachments/assets/95fae774-de46-47ea-b4b2-b82163f84143" />


### 6. Bar Plot for Weather Impact Analysis  
![Bar Plot for Weather Impact Analysis]<img width="1009" height="607" alt="download" src="https://github.com/user-attachments/assets/a23b085e-cd4f-4124-893f-7446fc7b80a0" />

### 7. Barplot for Average Delivery Time Analysis by Traffic Condition
![Barplot for Average Delivery Time Analysis by Traffic Condition]<img width="1009" height="553" alt="download" src="https://github.com/user-attachments/assets/c0e570e6-d0e6-465f-be18-7a5d4b8f5d63" />

### 8. Bar Plot for Product Category vs. Delivery Time Analysis
![Bar Plot for Product Category vs. Delivery Time Analysis]<img width="1009" height="609" alt="download" src="https://github.com/user-attachments/assets/1a504e4e-8f01-43ed-a3bc-c7ecc931bee0" />

### 9. Distance vs Delivery Time
![Distance vs Delivery Time]<img width="854" height="553" alt="download" src="https://github.com/user-attachments/assets/ca06d7e1-de4c-4a9b-9b81-96c9dc00bc17" />

### 4. Feature Importance  
![Feature Importance]<img width="972" height="547" alt="download" src="https://github.com/user-attachments/assets/0b18b12b-1312-4e79-ad5b-ef88db5cf3e1" />


---

##  Model Training & Results  

| Model              | MAE   | RMSE  | R²    |
|--------------------|-------|-------|-------|
| Linear Regression  | 28.32 | 36.71 | 0.54  |
| Random Forest      | 21.17 | 26.43 | 0.77  |
| XGBoost            | 18.84 | 23.51 | 0.81  |
| **LightGBM** ✅     | **17.12** | **22.10** | **0.82** |

---

##  MLOps with MLflow  

- All experiments logged in MLflow UI.  
- Comparison of multiple models made easy.  
- Example MLflow Run:  

![MLflow Experiment]<img width="1908" height="968" alt="ML Flow Experiment View" src="https://github.com/user-attachments/assets/b9a79b25-9d04-468f-929d-59842f799c5f" />
  

---

##  Streamlit Application  

### Features  
- Input: Distance, Weather, Traffic, Agent details, Order Category.  
- Output: Predicted Delivery Time.   

### Deployed App Screenshot  
![Streamlit UI]<img width="922" height="816" alt="Streamlit UI" src="https://github.com/user-attachments/assets/978f20b2-2506-4b38-ae9d-3647653c81e0" />
  

---

## Key Learnings  
- Built **end-to-end ML pipeline** for regression.  
- Hands-on **MLOps**: experiment tracking & model registry using MLflow.  
- Optimized **tree-based models** with hyperparameter tuning.  
- Built **Streamlit app** for business-facing predictions.  

---

##  Future Improvements  
- Add live APIs for **real-time traffic & weather**.  
- Deploy with **Docker + AWS/GCP/Azure**.  
- Automate retraining with **CI/CD pipelines**.  

---

##  Author  
**Uttam Singh Chaudhary**  
- Data Science & AI Enthusiast  
- [LinkedIn](https://linkedin.com/in/uttam-singh-chaudhary) | [GitHub](https://github.com/ut-si-ch)  

---

