from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class name(BaseModel):
    username:str
    password:str
@app.post("/login")
def num(data:name):
   if data.username=="sharath" and data.password=="123":
       return{"correctuser"}
   else:
       return("incorrectuser")