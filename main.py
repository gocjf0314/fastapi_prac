# Import for FastAPI
from fastapi import FastAPI

# This can show html file
from fastapi.responses import FileResponse

# Import for using data model
# Check data validation 
from pydantic import BaseModel

from enum import Enum

class Sex(str, Enum):
    male = 'M'
    female = 'F'
    other = 'O'

class TestModel(BaseModel):
    name :str
    address :str
    age :int
    sex :Sex

# Create Server APP(FastAPI class)
# app.get("route")
# app.post("route")
app = FastAPI()

# Receive request form user and processing
@app.post("/")
def getRequest():
    return 'Wow, You success call post!!!'

@app.post("/send")
async def getRequest(data : TestModel):
    print("Data is ", data)
    # await ....
    return data.name + 'request to you'

# Main page
@app.get("/")
def sayHello():
    return 'What\' your name?'

# Response file(html, ...)
@app.get("/view")
def showView():
    return FileResponse('./index.html')

# FastAPI validate data 
# if you declare data type
@app.get("/data/{data_id}")
def showData(data_id :int):
    return {
        "introduce": "My name is jimmy.",
        "data_id": data_id,
    }