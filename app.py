# -*- coding: utf-8 -*-
import numpy as np
import joblib  # Ensure joblib is used if the model was saved with it
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)
try:
    model = joblib.load('ADA.joblib')  # Use joblib to load the model
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict')
def predict():
    """Render the prediction page."""
    return render_template('predict.html')

@app.route('/submit', methods=["POST"])
def submit():
    """Handle form submission and make predictions."""
    try:
        # Reading the inputs given by the user
        input_feature = [x for x in request.form.values()]
        input_feature = [np.array(input_feature)]
        print(input_feature)
        # Define column names
        names = ['age', 'workclass', 'education', 'occupation', 'relationship', 'race',
       'sex', 'hours.per.week', 'marital_status', 'native_country',
       'capital_gain', 'capital_loss']

        # Create a DataFrame
        data = pd.DataFrame(input_feature, columns=names)
        print(data)
        # Predictions using the loaded model file
        prediction = model.predict(data)

        # Determine the result message based on the prediction value
        if prediction[0] == 0:
            result = "Your earns more than 50,000. Yes, you are ready for investment. Invest wisely."
            prediction = ">50k"
        else:
            result = "Your earns less than 50,000. Better to invest your money to learn skills."
            prediction = "<=50k"
        
        return render_template("result.html", result=result, prediction=prediction)
    except Exception as e:
        # Handle exceptions and print error for debugging
        print(f"Error during prediction: {e}")
        return render_template("result.html", result="An error occurred. Please try again.")

if __name__ == "__main__":
    app.run(debug=True, port=4000)  # Running the app with debug enabled
