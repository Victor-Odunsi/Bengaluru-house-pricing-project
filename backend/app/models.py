from pydantic import BaseModel

class FitIn(BaseModel):
    total_sqft: float
    location: str
    bedroom: int
    bath: int

class FitOut(FitIn):
    price: float