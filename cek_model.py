import pickle
import numpy as np

# Path file model Anda
model_path = 'knn_diabetes_model.pkl'

# Load model dari file
with open(model_path, 'rb') as file:
    knn_model = pickle.load(file)

# Periksa detail struktur model
print("Tipe Model:", type(knn_model))
print("\nAtribut Model yang Tersedia:")
print(dir(knn_model))

# Jika model memiliki atribut 'n_neighbors', tampilkan nilainya
if hasattr(knn_model, 'n_neighbors'):
    print("\nJumlah Tetangga (n_neighbors):", knn_model.n_neighbors)

# Jika model memiliki fungsi score, periksa akurasi dengan contoh data dummy
dummy_data = [
    45,             # Age
    1,              # Gender_Male
    0,              # Polyuria_Yes
    1,              # Polydipsia_Yes
    0,              # sudden_weight_loss_Yes
    1,              # weakness_Yes
    0,              # Polyphagia_Yes
    0,              # Genital_thrush_Yes
    1,              # visual_blurring_Yes
    1,              # Itching_Yes
    0,              # Irritability_Yes
    1,              # delayed_healing_Yes
    1,              # partial_paresis_Yes
    1,              # muscle_stiffness_Yes
    0,              # Alopecia_Yes
    1               # Obesity_Yes
]
import numpy as np
import pandas as pd
import pickle

# Path file model Anda
model_path = 'knn_diabetes_model.pkl'

# Load model dari file
with open(model_path, 'rb') as file:
    knn_model = pickle.load(file)

# Data dummy
dummy_data = [
    50,             # Age
    1,              # Gender_Male
    1,              # Polyuria_Yes
    1,              # Polydipsia_Yes
    1,              # sudden_weight_loss_Yes
    1,              # weakness_Yes
    1,              # Polyphagia_Yes
    1,              # Genital_thrush_Yes
    1,              # visual_blurring_Yes
    1,              # Itching_Yes
    1,              # Irritability_Yes
    1,              # delayed_healing_Yes
    1,              # partial_paresis_Yes
    1,              # muscle_stiffness_Yes
    1,              # Alopecia_Yes
    1               # Obesity_Yes
]

# Membuat DataFrame dengan nama kolom yang sesuai dengan format model yang dilatih
columns = [
    'Age', 'Gender_Male', 'Polyuria_Yes', 'Polydipsia_Yes', 'sudden_weight_loss_Yes', 
    'weakness_Yes', 'Polyphagia_Yes', 'Genital_thrush_Yes', 'visual_blurring_Yes', 
    'Itching_Yes', 'Irritability_Yes', 'delayed_healing_Yes', 'partial_paresis_Yes', 
    'muscle_stiffness_Yes', 'Alopecia_Yes', 'Obesity_Yes'
]

# Mengubah data dummy menjadi DataFrame dengan kolom yang sesuai
input_data = pd.DataFrame([dummy_data], columns=columns)

# Periksa nama fitur model
print("Nama fitur yang digunakan model:", knn_model.feature_names_in_)

# Melakukan prediksi
if hasattr(knn_model, 'predict'):
    try:
        prediction = knn_model.predict(input_data)
        print("\nPrediksi untuk data dummy:", prediction)
    except Exception as e:
        print("\nTidak bisa memprediksi data dummy:", e)
