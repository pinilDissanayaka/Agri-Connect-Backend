import os
import pickle
from fastapi import UploadFile, HTTPException, status
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras import utils as kerasUtils
import numpy as np
import logging
from tempfile import TemporaryFile
import warnings


warnings.filterwarnings(action="ignore")



logging.basicConfig(filename="log.log", level=logging.WARNING)

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

    
def loadModel():
    try:
        with open('model_labels.pkl', 'rb') as file:
            modelLabels=pickle.load(file)[0]
            
        model=load_model('model.keras')
        
        return modelLabels, model
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.args)
        
        
def preprocessImage(imageFile):
    try:
        imageArray=kerasUtils.img_to_array(imageFile)
        imageArray=imageArray/255
        imageArray=np.expand_dims(imageArray, axis=0)
        return imageArray
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=e.args)
    
def makePrediction(uploadedFile: UploadFile):
    try:
        modelLabels, model=loadModel()
        
        temp_file=uploadedFile.filename
                
        with open(temp_file, "wb") as img:
            img.write(uploadedFile.file.read())
            
        imageFile=kerasUtils.load_img(path=temp_file, target_size=(224, 224))
        
        if os.path.exists(temp_file):
            os.remove(temp_file)
        
        imageArray=preprocessImage(imageFile=imageFile)
        
        print(imageArray)
        
        prediction=model.predict(imageArray)
        
        print(prediction)
        
        confidence=round(100 * (np.max(prediction[0])), 2)
        
        prediction=modelLabels[np.argmax(prediction[0])]
        
        return prediction, confidence
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=e.args)
        
        
