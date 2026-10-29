from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("linearmodel.pkl")

class datascience(BaseModel): 
    AdvertisingBudget:float 

@app.get("/")
def test():
    return { "msg" : "Uvicorn is running "}


@app.post("/predict")
def datainsert(ds:datascience):

    Sales = model.predict([[ds.AdvertisingBudget]])

    return {"predicated_Sales" : round(float(Sales[0]),2)}