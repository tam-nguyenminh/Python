import json, os, numpy as np
import pickle 
print('----------------------start here------------------------')

global _data_columns
global _path
global _model 
global _districts 

basedir = r"C:/Users/84393/OneDrive - CÔNG TY TNHH OFFICIENCE/PYTHON/ML_House_Rent/"
model_path = os.path.join(basedir, 'hcm_room_price_prediction_model.pickle')
datacol_path = os.path.join(basedir, 'columns.json')

def load_saved_artifacts():
    global _model, _data_columns, _districts
    with open(model_path, 'rb') as f:
        _model = pickle.load(f)

    with open(datacol_path, 'rb') as f:
        _data_columns = json.load(f)['data_columns']
        _districts = _data_columns[1:]

# Get estimated price
def get_estimated_price(district, acreage):
    global predict_result
    try:
        district_index = _data_columns.index(district.lower())
    except:
        district_index = -1
    x = np.zeros(len(_data_columns))
    x[0]=acreage
    if district_index >0:
        x[district_index] = 1
    
    predict_result = _model.predict([x])[0]
    return predict_result

def get_districts():
    return _districts

def get_data_columns():
    return _data_columns
# def get_acreage():
#     return acreage

if __name__ == '__main__':
    load_saved_artifacts()
    # print(_districts)
    print(_data_columns)
    # print(get_estimated_price('quận 1', 25))
    

