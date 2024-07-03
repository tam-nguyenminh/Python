import json ,os, numpy as np
import pickle
print('----------------------restart---------------')

__locations = None
__data_columns = None
__model = None

basedir = r"C:/Users/84393/OneDrive - CÔNG TY TNHH OFFICIENCE/PYTHON/ML_BangaloreHomePrice/"
location_path = os.path.join(basedir, 'columns.json')
model_path = os.path.join(basedir, 'banglore_home_prices_model.pickle')

# GET ESTIMATED PRICE
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0],2)

# GET LOCATION NAME
def get_location_names():
    return __locations 

def get_data_columns():
    return __data_columns

def load_saved_artifacts():
    print('loading saved artifacts ... start')
    global __data_columns
    global __locations
    global __model

    with open(location_path, 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    with open(model_path, 'rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts ... done')

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print("estimated price: ", get_estimated_price('6th phase jp nagar', 1000,3,3))
    print("estimated price: ", get_estimated_price('nri layout', 250,2,3))
    print("estimated price: ", get_estimated_price('1st phase jp nagar', 2000,4,1))