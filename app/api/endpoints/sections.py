from urllib import response
from fastapi import APIRouter, Depends, HTTPException, Request
from app.api.schemas.models import (
    WindPowerDensityPredictionRequestSchema,
    WindPowerDensityPredictionResponseSchema
)
from app.model.operations import predict
from app.model.operations import __version__ as model_version

router = APIRouter()

@router.get("/")
async def home():
    return {
        "health_check": "OK",
        "model_version": model_version
        } 


@router.post('/wp_data_predict')
def retrieve_wp_data(request: WindPowerDensityPredictionRequestSchema):
   
    predictions = predict(list(request.dict().values()))
    return {"window power density": predictions}


