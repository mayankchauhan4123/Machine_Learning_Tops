from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("linearmodel.pkl")

class datascience(BaseModel): 
    StudyHours:float  # je value aapde input ma aapiye chiye ey


# api end point 
@app.get("/")
def test():
    return { "msg" : "Uvicorn is running "}


@app.post("/predict")
def datainsert(ds:datascience):

    marks = model.predict([[ds.StudyHours]])

    return {"predicatedmarks" : round(float(marks[0]),2)}