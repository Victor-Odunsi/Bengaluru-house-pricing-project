import pickle
import pandas as pd 
from backend.app.config import settings

class PriceModel:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        with open(settings.model_path, 'rb') as file:
            model = pickle.load(file)
        return model

    def predict(self, features: dict) -> float:
        columns = ['total_sqft', 'bath', 'bedroom']

        all_columns = settings.locations() + columns
        
        input_data = pd.DataFrame(columns=all_columns)
        
        if not features['location'].startswith('location_'): 
            location = f'location_{features["location"]}'
        else:
            location = features['location']

        input_data.loc[0] = 0

        input_data['total_sqft'] = features['total_sqft']
        input_data['bath'] = features['bath']
        input_data['bedroom'] = features['bedroom']

        if location in settings.locations():
            input_data[location] = 1
        else:
            print(f'Warning: Location {location} not in training data. Defaulting to 0')

        return self.model.predict(input_data)[0]

model = PriceModel()