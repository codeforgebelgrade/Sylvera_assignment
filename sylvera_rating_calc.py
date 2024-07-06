import sys, json
from Transformations import *
from pydantic import ValidationError
from JSON_models import WeatherData, TrafficData, RoadConditionsData


# TODO: Exception handling for inputs? 
json_arg1 = sys.argv[1]
weather_data_input = sys.argv[1]
traffic_data_input = sys.argv[2]
road_conditions_input = sys.argv[3]

try:
    weather_data_json = json.loads(weather_data_input)
    traffic_data_json = json.loads(traffic_data_input)
    road_conditions_json = json.loads(road_conditions_input)

    weather_data_model = WeatherData(**weather_data_json)
    traffic_data_model = TrafficData(**traffic_data_json)
    road_conditions_model = RoadConditionsData(**road_conditions_json)

    print("Data loaded successfully:")
    print("Weather data: ", weather_data_model.model_dump())
    print("Trafic data: ", traffic_data_model.model_dump())
    print("Road conditions: ", road_conditions_model.model_dump())

    weather_output = calculate_comfot_index(weather_data_model)
    print(weather_output.comfort_index)

    traffic_output = calculate_traffic_efficiency_flow(traffic_data_model)
    print(traffic_output.traffic_efficiency_flow)

except ValidationError as e:
    print(e.errors())
except json.JSONDecodeError as e:
    print("Invalid JSON object submitted as an argument")


