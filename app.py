from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
app = Flask(__name__)
# Charger le modèle
model = joblib.load('model/model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données du formulaire
    data = request.form.to_dict()
    # Convertir les données en DataFrame
    input_data = pd.DataFrame([data])
    input_data = input_data.astype({
        'male': 'int64',
        'age': 'int64',
        'education': 'float64',
        'currentSmoker': 'int64',
        'cigsPerDay': 'float64',
        'BPMeds': 'float64',
        'prevalentStroke': 'int64',
        'prevalentHyp': 'int64',
        'diabetes': 'int64',
        'totChol': 'float64',
        'sysBP': 'float64',
        'diaBP': 'float64',
        'BMI': 'float64',
        'heartRate': 'float64',
        'glucose': 'float64'
    })
    # Faire une prédiction
    prediction = model.predict(input_data)
    # Retourner la prédiction
    return jsonify({'TenYearCHD': int(prediction[0])})
if __name__ == '__main__':
    app.run(debug=True)
