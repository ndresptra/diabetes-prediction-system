Diabetes Prediction System (Flask + KNN Machine Learning)

A web-based diabetes prediction system built using Python and Flask, integrated with a K-Nearest Neighbors (KNN) machine learning model to classify patient health data and provide personalized health recommendations.

🧠 Overview

This application predicts whether a patient is likely to have diabetes based on input health parameters. The system uses a trained KNN model and provides health tips based on the prediction result.

🖼️ Preview
<img width="1365" height="599" alt="image" src="https://github.com/user-attachments/assets/3c83cbd5-34b2-4b6f-8cde-f815bfb6f7e0" />


🚀 Features
Diabetes prediction using KNN algorithm
Web-based interface using Flask
Input validation for user data
Health recommendations based on prediction
Model trained using real dataset
Simple and user-friendly UI

🧪 Machine Learning
Algorithm: K-Nearest Neighbors (KNN)
Dataset: Pima Indians Diabetes Dataset
Output: Positive / Negative prediction

🔄 Workflow
User inputs health data (glucose, BMI, age, etc.)
Data is sent to backend (Flask)
KNN model processes input
Prediction result is returned
System displays result + health tips

🧱 Tech Stack
Python
Flask
Scikit-learn
Pandas / NumPy
HTML / CSS / JavaScript

📂 Project Structure
prediksi-diabetes/
│── app.py
│── routes.py
│── cek_model.py
│── check_features.py
│── train_knn_model.py
│── knn_diabetes_model.pkl
│── requirements.txt
│── templates/
│   └── index.html
│── static/
│   ├── js/
│   └── video/

⚙️ Installation & Run
Clone repository
git clone https://github.com/USERNAME/diabetes-prediction-system.git
Masuk folder project
cd diabetes-prediction-system
Buat virtual environment
python -m venv env
env\Scripts\activate
Install dependencies
pip install -r requirements.txt
Jalankan aplikasi
python app.py
Buka di browser
http://127.0.0.1:5000

💡 Future Improvements
Add more machine learning models (Logistic Regression, Random Forest)
Improve UI/UX design
Add API endpoint
Deploy to cloud (Render / Railway)

👨‍💻 Author

ndresptra
