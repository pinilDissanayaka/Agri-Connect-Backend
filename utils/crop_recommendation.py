import pickle
import numpy as np
from fastapi import status, HTTPException

def loadModel():
    try:
        with open('crop_recommendation.pickle', 'rb') as model:
            model=pickle.load(model)
        
        
        return model
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=e.args)
        
        
def recommend_crop(n, p, k, temp, hum, ph, rf):
    input_data = [n, p, k, temp, hum, ph, rf]
    input_data_arr = np.asarray(input_data).reshape(1, -1)
    
    print(input_data)
    
    model=loadModel()
    
    recommended_crop=model.predict(input_data_arr)
    
    return recommended_crop
    
    
    