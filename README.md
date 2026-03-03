# 🏠 House Price Prediction Web Application

## 📖 Overview

This project is a complete **Machine Learning Web Application** that predicts house prices based on property features.

It combines:

* A trained **Linear Regression** model
* Data preprocessing pipeline
* A **Flask** web application for user interaction

Users can input housing details through a web interface, and the system instantly predicts the estimated house price.



## 🧠 Machine Learning Model

The prediction model is built using:

* **Pandas & NumPy** for data handling
* **Scikit-learn** for preprocessing and training
* **Linear Regression Algorithm**

### 🔹 Data Processing Steps:

* Handling missing values using mean imputation
* Encoding categorical features (Ocean Proximity) using One-Hot Encoding
* Splitting data into training and testing sets
* Training a regression model on processed features

The trained model is saved as `model.pkl` using **Joblib** for later use in the web application.


## 🌐 Web Application

The web application is built using:

* **Flask Framework**
* HTML templates for user input and result display

### 🔹 How It Works:

1. User enters housing details:

   * Longitude
   * Latitude
   * Housing median age
   * Total rooms
   * Total bedrooms
   * Population
   * Households
   * Median income
   * Ocean proximity

2. The input is processed and formatted.

3. The trained model predicts the house price.

4. The result is displayed on a separate results page.




