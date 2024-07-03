from flask import Flask, render_template, request , jsonify
import pickle, os, json
import numpy as np
import util_hcm_room_rent
import requests

app = Flask(__name__)

# global _districts
basedir = r"C:/Users/84393/OneDrive - CÔNG TY TNHH OFFICIENCE/PYTHON/ML_House_Rent/"
model_path = os.path.join(basedir, 'hcm_room_price_prediction_model.pickle')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/get_district_names', methods=['GET'])
def get_district_names():
    districts = util_hcm_room_rent.get_districts()
    return jsonify({'districts': districts})

@app.route('/')
def home():
    # Fetch districts list from /get_district_names endpoint
    global districts
    try:
        response = requests.get('http://127.0.0.1:1000/get_district_names')
        if response.status_code == 200:
            districts = response.json().get('districts', [])
        else:
            districts = []  # Default empty list
    except requests.exceptions.RequestException as e:
        print(f"Error fetching districts: {e}")
        districts = []  # Default empty list
    
    return render_template('index.html', districts=districts)

@app.route('/predict', methods=['POST'])
def predict_room_price():
    if request.method == 'POST':
        acreage = request.form.get('acreage')
        district = request.form.get('district')
        if acreage and district:
            estimated_price = util_hcm_room_rent.get_estimated_price(district, acreage)
            estimated_price = round(estimated_price,3)
            # home()
            return render_template('index.html', result=estimated_price, districts=districts, district=district, acreage=acreage)
        else:
            return render_template('index.html', error_message="Invalid input. Please enter both acreage and district.")

if __name__ == '__main__':
    util_hcm_room_rent.load_saved_artifacts()
    app.run(debug=True, port=1000)
    
    