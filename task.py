from fastapi import FastAPI
from pydantic import BaseModel

class item(BaseModel):
    name:str
    
app=FastAPI()
@app.post("/")

def name(obj:item):
    return {
         "name":obj.name
    }