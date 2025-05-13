from fastapi import FastAPI,HTTPException
from typing import Text,Optional
from uuid import uuid4 as uuid
from pydantic import BaseModel
from datetime import datetime
from database import Database
from copy import copy

app=FastAPI()

class User(BaseModel):
    id:Optional[str]=None
    name:str
    age:str
    profession:str
    about:Optional[Text]=None
    married:bool=False
    registered_at:str =str(datetime.now())


@app.get('/')
def read_root():
    return {'message':'Welcome to my RESTApi'}

@app.get('/users')
def allusers():
    return Database.select_all()

@app.get('/users/{user_id}')
def get_user(user_id:str):
    user=Database.select(user_id)

    if len(user)==0:
        raise HTTPException(status_code=404,detail="user not found")
    return user

@app.post('/users')
def adduser(user:User):
    user.id=str(uuid())

    users=Database.select_all()
    users.append(dict(user))
    Database.insert(users)

    confirmed_user=Database.confirm_last_save()

    return {"message":"User registered successfully","user":confirmed_user}

@app.delete('/users/{user_id}')
def delete_user(user_id:str):
    users=Database.select_all()

    for index,user in enumerate(users):
        if user["id"]==user_id:
            deleted_user=copy(user)
            users.pop(index)
            Database.insert(users)
            return {"message":"User have been deleted","user":deleted_user}
    
    raise HTTPException(status_code=404,detail=f"user with user id {user_id} not found")

@app.put('/user/{user_id}')
def update_user(user_id:str,updated_user:User):
    users=Database.select_all()

    for index,user in enumerate(users):
        if user["id"]==user_id:
            users[index]["name"]=updated_user.name
            users[index]["age"] = updated_user.age
            users[index]["profession"] = updated_user.profession
            users[index]["about"] = updated_user.about
            users[index]["married"] = updated_user.married
            Database.insert(users)
            return {"message":"user updated successfuly","user":users[index]}
        
    raise HTTPException(status_code=404,detail="User not found")


