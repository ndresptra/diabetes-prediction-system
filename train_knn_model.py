import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pickle

# 1. Membaca data dari file CSV
file_path = 'diabetes_data_upload.csv'  # Path file CSV
data = pd.read_csv(file_path)

# 2. Periksa beberapa baris data
print("Sample Data:")
print(data.head())

# 3. Mengganti nama kolom dengan spasi menjadi underscore
data.columns = data.columns.str.replace(' ', '_')

# 4. Encode data kategori ke numerik
# Mengubah kolom kategori menjadi angka
data_encoded = pd.get_dummies(data, drop_first=True)  # One-hot encoding
print("\nData setelah encoding:")
print(data_encoded.head())

# 5. Pisahkan fitur dan label
X = data_encoded.iloc[:, :-1]  # Semua kolom kecuali kolom target
y = data_encoded.iloc[:, -1]   # Kolom terakhir sebagai target

# 6. Bagi data menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Inisialisasi model KNN
knn = KNeighborsClassifier(n_neighbors=5)

# 8. Latih model
knn.fit(X_train, y_train)

# 9. Evaluasi model
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy of the model:", accuracy)

# 10. Simpan model ke file .pkl
model_file_path = 'knn_diabetes_model.pkl'
with open(model_file_path, 'wb') as model_file:
    pickle.dump(knn, model_file)

print("\nModel berhasil disimpan ke:", model_file_path)
