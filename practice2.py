from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class name(BaseModel):
    a:int
    b:int
@app.post("/add")
def num(data:name):
    result = data.a+data.b
    return{"sum":result }