import json
import os
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    model_path: str = str(BASE_DIR / "model" / "bengaluru_prediction_model.pkl")
    columns_path: str = str(BASE_DIR / "columns.json")

    def columns(self):
        with open(self.columns_path) as f:
            columns = json.load(f)['columns_names']
            return columns

    def locations(self):
        locations = self.columns()
        valid_locations = [location[9:] for location in locations[:-3]]
        return valid_locations

    class Config:
        env_file = ".env"

settings = Settings()