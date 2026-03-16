from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# load model
model = pickle.load(open("model/model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.get("/predict")
def predict(hours: float):

    prediction = model.predict(np.array([[hours]]))

    return {
        "hours_studied": hours,
        "predicted_score": float(prediction[0])
    }