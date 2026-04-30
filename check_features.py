import joblib

# Path ke file model
model_path = "knn_diabetes_model.pkl"

try:
    # Load model
    model = joblib.load(model_path)
    print("Model loaded successfully.")

    # Cek apakah atribut 'feature_names_in_' ada
    if hasattr(model, 'feature_names_in_'):
        feature_names = model.feature_names_in_
        print("Feature names used during training:")
        print(feature_names)
    else:
        print("The model does not have the 'feature_names_in_' attribute. The feature names might not be stored.")

except Exception as e:
    print(f"Failed to load model: {e}")
