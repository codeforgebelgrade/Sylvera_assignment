import statistics
from JSON_models import *
from pydantic import BaseModel

def calculate_comfot_index(weather_data: WeatherData):
    score = (100 - weather_data.humidity) + (30 - weather_data.temperature)
    
    if weather_data.wind_speed != None:
        score = score + weather_data.wind_speed/2
    
    weather_output = WeatherDataOutput(comfort_index = score)
    return weather_output

def calculate_traffic_efficiency_flow(traffic_data: TrafficData):
    score = traffic_data.average_speed / (sum(traffic_data.traffic_density) + 1)
    if traffic_data.incident_reports != None:
        score = score - (2 * traffic_data.incident_reports)

    traffic_efficiency_output = TrafficEfficiencyOutput(traffic_efficiency_flow=score)
    return traffic_efficiency_output