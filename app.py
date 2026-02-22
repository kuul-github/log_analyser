from fastapi import FastAPI
import os

app = FastAPI()

def analyze_log(file_path):
    error_count = 0
    warning_count = 0
    info_count = 0

    if not os.path.exists(file_path):
        return {"error": "File not found"}

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    return {
        "ERROR": error_count,
        "WARNING": warning_count,
        "INFO": info_count
    }

@app.get("/analyze")
def analyze(file: str):
    return analyze_log(file)

import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

vectorizer, model = joblib.load("model.pkl")

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(data: TextInput):
    X = vectorizer.transform([data.text])
    prediction = model.predict(X)[0]
    return {"prediction": int(prediction)}
