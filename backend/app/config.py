import json
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_path: str = r"C:\Users\PC\Documents\Bengaluru housing project\model\bengaluru_prediction_model.pkl"
    
    def locations(self):
        with open(r"C:\Users\PC\Documents\Bengaluru housing project\columns.json") as f:
            locations = json.load(f)['columns_names']
            valid_locations = locations[:-3]
        return valid_locations

    class Config:
        env_file = ".env"

settings = Settings()