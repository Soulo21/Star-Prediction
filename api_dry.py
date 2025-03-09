from fastapi import FastAPI
import uvicorn
from predictor import load_model,make_predictions

app =FastAPI()

model = load_model('pipeline.pk1')

@app.get('/')
def index_route():
    return {"Health" : "Ok"}

@app.post('/predict')
def prediction(tempature,luminosity,radius,abs_mag):
    data_set = [tempature,luminosity,radius,abs_mag]
    probability = make_predictions(model,data_set)

    return probability
