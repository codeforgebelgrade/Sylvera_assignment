from pydantic import BaseModel
from typing import Optional

class WeatherDataModel(BaseModel):
    temperature: int
    humidity: float
    wind_speed: Optional[float] 

class TrafficDataModel(BaseModel):
    average_speed: float
    traffic_density: list[float]
    incident_reports: Optional[int]

class RoadConditionsDataModel(BaseModel):
    road_quality: int
    lighting_conditions: int
    accident_history: int
    traffic_density: list[float]
    average_speed: float
    incident_reports: Optional[int]
    wind_speed: Optional[float]

class OverallCommuteQualityModel(BaseModel):
    overall_commute_quality_score: float
    overall_commute_quality: str

class WeatherDataOutput(BaseModel):
    comfort_index: float

class TrafficEfficiencyOutput(BaseModel):
    traffic_efficiency_flow: float

class SafetyScoreOutput(BaseModel):
    safety_score: float
