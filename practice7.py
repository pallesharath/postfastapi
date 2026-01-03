from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class name(BaseModel):
    number:list[int]

@app.post("/sum")
def marks(data:name):
    total=sum(data.number)
    return{"total sum of number",total}