
from pydantic import BaseModel, Field

class WindPowerDensityPredictionResponseSchema(BaseModel):
    wind_power_density: float

class WindPowerDensityPredictionRequestSchema(BaseModel):
    wind_speed: float
    air_density: float
    temperature: float
    

