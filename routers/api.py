from fastapi import FastAPI, HTTPException, status, UploadFile
from schema.user import User
from crud.user import createUser, getUserByUserName
from utils.resource import saveResourceAtDirectory

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
        
        
@app.post("/upload-resource", tags=['User'])
async def uploadResource(resources:list[UploadFile]):
    try:
        saveResourceAtDirectory(resources=resources)
        return {"detail" : "done"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                            detail=e.args)
        

        
        
            