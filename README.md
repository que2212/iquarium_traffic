# **TrafficJams-Backend-**  
<p style="text-align: center;">This repository contains the backend part of the project. It is currently in the alpha version, so functionality and performance may change significantly as development progresses.</p>

---

### **Advantages**
- Scalability: can scale a project from streets to districts, counties, and even entire cities
- TFlexibility: can set different variables to retrain the model: weather, holidays, events, accidents, etc
- Simulations are possible: can simulate various events taking place in the city, for example, to see how traffic will look on Krasnaya st. at 14:00 with fog on City Day

---

### **Technologies**
- **Schedule**: for planning tasks
- **Selenium**: for data collection
- **Optuna**: for tuning hyperparameters
- **FastApi**: for connected between the operator and the server
- **TensorFlow**: used for data augmentation, stimulate the real behavior of the city
- **CatBoost with Fourier Series**: simulation of the traffic situation, RMSE = 0.15810, accuracy is up to 85%
