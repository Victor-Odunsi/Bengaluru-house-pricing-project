from fastapi import FastAPI
from backend.app.models import FitIn, FitOut
from backend.app.ml_model import model

app = FastAPI()

@app.get('/predict_house_price', response_model = FitOut)
def predict_house_price(data: FitIn):
    model.predict(data)
    