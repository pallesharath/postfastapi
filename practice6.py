from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class name(BaseModel):
    result:int

@app.post("/result")
def marks(data:name):
    if data.result>70:
        return{"you pass",data.result}
    else:
        return{"youfail"}