from pydantic import BaseModel
from typing import Optional

class WeatherData(BaseModel):
    temperature: int
    humidity: float
    wind_speed: Optional[float] 

class TrafficData(BaseModel):
    average_speed: float
    traffic_density: list[float]
    incident_reports: Optional[int]

class RoadConditionsData(BaseModel):
    road_quality: int
    lighting_conditions: int
    accident_history: int