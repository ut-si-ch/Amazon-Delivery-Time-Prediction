import streamlit as st
import pandas as pd
import mlflow.pyfunc
import joblib

# Load the best model from MLflow (replace with actual run_id/model name if needed)

#logged_model = "runs:/47f8cd46b3bb45f2b2f0333deeb6ee80/model"
#model = mlflow.pyfunc.load_model(logged_model)

model = joblib.load("code_files/saved_models/model.pkl")

feature_columns = [
    'Agent_Age', 'Agent_Rating', 'Store_Latitude', 'Store_Longitude',
    'Drop_Latitude', 'Drop_Longitude', 'Order_Hour', 'Order_Day',
    'Order_Weekday', 'Is_Weekend', 'Pickup_Hour', 'Pickup_Day',
    'Pickup_Weekday', 'Time_to_Pickup', 'Distance_KM', 'Weather_Fog',
    'Weather_Sandstorms', 'Weather_Stormy', 'Weather_Sunny',
    'Weather_Windy', 'Traffic_Jam_', 'Traffic_Low_', 'Traffic_Medium_',
    'Vehicle_scooter_', 'Vehicle_van', 'Area_Other', 'Area_Semi_Urban_',
    'Area_Urban_', 'Category_Books', 'Category_Clothing',
    'Category_Cosmetics', 'Category_Electronics', 'Category_Grocery',
    'Category_Home', 'Category_Jewelry', 'Category_Kitchen',
    'Category_Outdoors', 'Category_Pet_Supplies', 'Category_Shoes',
    'Category_Skincare', 'Category_Snacks', 'Category_Sports',
    'Category_Toys'
]

def preprocess_user_input(user_input: dict):
    df_input = pd.DataFrame([user_input])
    df_input = pd.get_dummies(df_input, columns=['Weather','Traffic','Vehicle','Area','Category'])
    df_input = df_input.reindex(columns=feature_columns, fill_value=0)
    return df_input

st.title("🚚 Delivery Time Predictor")

# --- User Inputs (only important ones) ---
category = st.selectbox("Category", ["Books","Clothing","Cosmetics","Electronics","Grocery",
                                     "Home","Jewelry","Kitchen","Outdoors","Pet_Supplies",
                                     "Shoes","Skincare","Snacks","Sports","Toys"])

agent_rating = st.slider("Agent Rating", 1.0, 5.0, 4.5)
agent_age = st.slider("Agent Age", 18, 65, 30)
distance_km = st.number_input("Distance (KM)", 0.0, 50.0, 5.0)
traffic = st.selectbox("Traffic", ["Jam_", "Low_", "Medium_"])
weather = st.selectbox("Weather", ["Fog","Sandstorms","Stormy","Sunny","Windy"])

# --- Defaults for less important columns ---
user_input = {
    "Agent_Age": agent_age,
    "Agent_Rating": agent_rating,
    "Distance_KM": distance_km,
    "Weather": weather,
    "Traffic": traffic,
    "Category": category,
    "Vehicle": "scooter_",   # default
    "Area": "Urban_",        # default
    "Store_Latitude": 12.97, # default
    "Store_Longitude": 77.59,
    "Drop_Latitude": 12.98,
    "Drop_Longitude": 77.60,
    "Order_Hour": 14,
    "Order_Day": 15,
    "Order_Weekday": 2,
    "Is_Weekend": 0,
    "Pickup_Hour": 15,
    "Pickup_Day": 15,
    "Pickup_Weekday": 2,
    "Time_to_Pickup": 10
}

# --- Preprocess & Predict ---
df_input = preprocess_user_input(user_input)

if st.button("Predict Delivery Time"):
    prediction = model.predict(df_input)[0]
    st.success(f"⏱ Estimated Delivery Time: {prediction:.2f} minutes")
