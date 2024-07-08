import sys, json
from Transformations import *
from pydantic import ValidationError
from JSON_models import WeatherDataModel, TrafficDataModel, RoadConditionsDataModel


# TODO: Exception handling for inputs? 
json_arg1 = sys.argv[1]
weather_data_input = sys.argv[1]
traffic_data_input = sys.argv[2]
road_conditions_input = sys.argv[3]

try:
    weather_data_json = json.loads(weather_data_input)
    traffic_data_json = json.loads(traffic_data_input)
    road_conditions_json = json.loads(road_conditions_input)

    weather_data_model = WeatherDataModel(**weather_data_json)
    traffic_data_model = TrafficDataModel(**traffic_data_json)
    road_conditions_model = RoadConditionsDataModel(**road_conditions_json, **traffic_data_json, wind_speed=weather_data_model.wind_speed)

    print("Data loaded successfully:")
    print("Weather data: ", weather_data_model.model_dump())
    print("Trafic data: ", traffic_data_model.model_dump())
    print("Road conditions: ", road_conditions_model.model_dump())

    apply_transformations(weather_data_model, traffic_data_model, road_conditions_model)

except ValidationError as e:
    print(e.errors())
except json.JSONDecodeError as e:
    print("Invalid JSON object submitted as an argument")

