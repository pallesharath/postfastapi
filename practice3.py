from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class name(BaseModel):
    strings:str
@app.post("/uppercase")
def uper(data:name):
    return{"inupercase":data.strings.upper()}

