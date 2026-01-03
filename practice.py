from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class name(BaseModel):
    name:str
    rollno:int
    place:str
    phone:int
@app.post("/obj_name")
def name(obj_name:name):
    return{
        "obj_name":obj_name
    }
