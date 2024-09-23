from fastapi import FastAPI, HTTPException, status, UploadFile
from schema.user import User
from crud.user import createUser, getUserByUserName
#from utils.prediction import makePrediction
from utils.chain import get_solution

app=FastAPI()

@app.post("/register", tags=['User'])
async def register(user:User):
    _status=createUser(user=user)
    if _status==201:
        return {"detail":"user created successfully"}
    else:
        raise HTTPException(400, detail="Email already registered")
        
        
@app.post("/login", tags=['User', 'Admin'])
async def login(user_name:str, password:str):
    _status=getUserByUserName(userName=user_name, rowPassword=password)
    
    if _status == 200:
        return {"detail":"user logging successfully"}
    elif _status == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Bad request")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect email")

@app.post("/prediction", tags=["User"])
async def prediction(imageFile: UploadFile):
    #disease, confidence=makePrediction(uploadedFile=imageFile)
    
    disease, confidence="brown-spot", 98

    solution=get_solution(disease=prediction)
    
    if disease and confidence and solution:
        return {
            "detail":"disease identification successfully",
            "disease":disease,
            "confidence":confidence,
            "solution":solution
        }
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Bad request")