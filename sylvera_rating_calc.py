import json
from Transformations import *
from pydantic import ValidationError
from JSON_models import WeatherDataModel, TrafficDataModel, RoadConditionsDataModel

try:
    weather_data_json = json.loads(input("Please enter weather data in JSON format: "))
    traffic_data_json = json.loads(input("Please enter traffic data in JSON format: "))
    road_conditions_json = json.loads(input("Please enter road conditions data in JSON format: "))

    weather_data_model = WeatherDataModel(**weather_data_json)
    traffic_data_model = TrafficDataModel(**traffic_data_json)
    road_conditions_model = RoadConditionsDataModel(**road_conditions_json, **traffic_data_json, wind_speed=weather_data_model.wind_speed)

    print("DATA LOADED SUCCESSFULLY:")
    print("Weather data: ", weather_data_model.model_dump())
    print("Trafic data: ", traffic_data_model.model_dump())
    print("Road conditions: ", road_conditions_model.model_dump())

    apply_transformations(weather_data_model, traffic_data_model, road_conditions_model)

except ValidationError as e:
    print(e.errors())
except json.JSONDecodeError as e:
    print("Invalid JSON object submitted as an argument")

