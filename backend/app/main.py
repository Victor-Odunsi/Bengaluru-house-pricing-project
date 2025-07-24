from fastapi import FastAPI, HTTPException
from backend.app.models import FitIn, FitOut
from backend.app.ml_model import model
from backend.app.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    #allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/get_locations')
def get_locations():
    return settings.locations()

@app.post('/predict_house_price', response_model = FitOut)
def predict_house_price(data: FitIn):
    try:
        price = model.predict(data.dict())
        return {"price": price}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))