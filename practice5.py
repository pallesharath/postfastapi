from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class name(BaseModel):
    num:int
@app.post("/cheeck")
def even(data:name):
    if data.num%2==0:
        return{"even"}
    else:
        return{"ODD"}
