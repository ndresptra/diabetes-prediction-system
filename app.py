from flask import Flask, render_template
from routes import predict_blueprint

# Inisialisasi Flask
app = Flask(__name__)

# Register blueprint untuk route prediksi
app.register_blueprint(predict_blueprint)

# Route Halaman Utama
@app.route('/')
def index():
    return render_template('index.html')

# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
