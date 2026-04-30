from flask import Blueprint, request, jsonify
import numpy as np
import joblib
import logging
import pandas as pd

predict_blueprint = Blueprint('predict', __name__)
logging.basicConfig(level=logging.INFO)

# Load KNN Model
model_path = "knn_diabetes_model.pkl"
try:
    model = joblib.load(model_path)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load model: {e}")
    model = None

# Mapping categorical fields
gender_mapping = {"Male": 1, "Female": 0}
binary_mapping = {"Yes": 1, "No": 0}

# Define health tips
def get_health_tips(prediction):
    if prediction == "Positive":
        return {
            "tips": [
                "Jaga pola makan sehat dengan rendah gula.",
                "Periksa kadar gula darah secara rutin.",
                "Lakukan olahraga secara teratur untuk menjaga berat badan.",
                "Selalu konsultasikan dengan dokter untuk saran yang tepat."
            ]
        }
    else:
        return {
            "tips": [
                "Jaga pola makan sehat dengan gula rendah.",
                "Tetap aktif dengan rutin berolahraga.",
                "Kontrol berat badan Anda dalam batas sehat.",
                "Hindari merokok dan alkohol berlebihan."
            ]
        }

@predict_blueprint.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"status": "error", "message": "Model not loaded correctly."}), 500

    try:
        # Parse JSON payload
        data = request.get_json()

        # Validate fields
        required_fields = [
            'Age', 'Gender_Male', 'Polyuria_Yes', 'Polydipsia_Yes', 'sudden_weight_loss_Yes', 
            'weakness_Yes', 'Polyphagia_Yes', 'Genital_thrush_Yes', 'visual_blurring_Yes', 
            'Itching_Yes', 'Irritability_Yes', 'delayed_healing_Yes', 'partial_paresis_Yes', 
            'muscle_stiffness_Yes', 'Alopecia_Yes', 'Obesity_Yes'
        ]

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"status": "error", "message": f"Missing fields: {', '.join(missing_fields)}"}), 400

        # Convert input fields
        input_features = []
        for field in required_fields:
            try:
                value = int(data.get(field, 0))  # Default to 0 if field is missing
                input_features.append(value)
            except ValueError:
                return jsonify({
                    "status": "error",
                    "message": f"Invalid value for field '{field}', expected integer."
                }), 400

         # Create a pandas DataFrame with proper feature names
        input_df = pd.DataFrame([input_features], columns=required_fields)

        # Predict
        prediction = model.predict(input_df)[0]
        result = "Positive" if prediction == 1 else "Negative"
        
        logging.info(f"Model prediction: {result}")

        # Get health tips based on prediction result
        health_tips = get_health_tips(result)

        # Return response
        return jsonify({
            "status": "success",
            "prediction": result,
            "health_tips": health_tips
        })

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Error during prediction: {str(e)}")
        return jsonify({"status": "error", "message": f"An error occurred: {str(e)}"}), 500