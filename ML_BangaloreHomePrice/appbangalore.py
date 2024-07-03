import pickle, os
from flask import Flask, render_template, request, jsonify
import utilbangalore as util # the utile.py created in the folder

# tutorial https://www.youtube.com/watch?v=2LqrfEzuIMk&t=1006s
app1 = Flask(__name__)

# @app1.route('/')
# def home():
#     result= ''
#     # print("Rendering home page...")
#     return render_template('index.html', result=result)
#     # return 'Hello World!'

@app1.route('/get_location_names', methods = ['GET'])
def get_location_names():
    result=''
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app1.route('/predict_home_price', methods = ['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print('Starting python flask server for bangalore home price prediction....')
    util.load_saved_artifacts()
    app1.run(debug=True, port=4000)