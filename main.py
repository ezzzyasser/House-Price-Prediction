import pandas as pd
import numpy as np
import joblib
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

model_filename = 'model.pkl'
model = joblib.load(model_filename)

@app.route("/")
def root():
    return render_template('input.html')

def root():
    return render_template('input.html')

def predict_price(data):
    predicted_price = model.predict(data)[0]
    return predicted_price

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        # Create a dictionary with zeros for all options
        ocean_proximity_options = ['NEAR BAY', 'INLAND', '<1H OCEAN', 'ISLAND', 'NEAR OCEAN']
        user_data = {
            'longitude': [float(request.form['longitude'])],
            'latitude': [float(request.form['latitude'])],
            'housing_median_age': [float(request.form['housing_median_age'])],
            'total_rooms': [float(request.form['total_rooms'])],
            'total_bedrooms': [float(request.form['total_bedrooms'])],
            'population': [float(request.form['population'])],
            'households': [float(request.form['households'])],
            'median_income': [float(request.form['median_income'])],
        }
        
        # Set a binary value of 1 for the selected 'ocean_proximity'
        selected_proximity = request.form['ocean_proximity']
        for option in ocean_proximity_options:
            user_data[option] = [1.0 if option == selected_proximity else 0.0]
        
        user_input = pd.DataFrame(user_data)
        predicted_price = predict_price(user_input)
        
        return redirect(url_for('results', predicted_price=predicted_price))  # Corrected endpoint name

@app.route('/results/<predicted_price>')  # Corrected endpoint name
def results(predicted_price):
    return render_template('result.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
