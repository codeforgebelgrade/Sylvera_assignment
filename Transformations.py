from JSON_models import *

def calculate_comfot_index(weather_data: WeatherDataModel):
    score = (100 - weather_data.humidity) + (30 - weather_data.temperature)
    
    if weather_data.wind_speed != None:
        score += (weather_data.wind_speed/2)
    
    weather_output = WeatherDataOutput(comfort_index = score)
    return weather_output

def calculate_traffic_efficiency_flow(traffic_data: TrafficDataModel):
    score = traffic_data.average_speed / (sum(traffic_data.traffic_density) + 1)
    if traffic_data.incident_reports != None:
        score -= (2 * traffic_data.incident_reports)

    traffic_efficiency_output = TrafficEfficiencyOutput(traffic_efficiency_flow=score)
    return traffic_efficiency_output

def calculate_safety_score(weather_data: WeatherDataModel, traffic_data: TrafficDataModel, road_conditions_data: RoadConditionsDataModel):
    score = 1/sum(traffic_data.traffic_density)
    score += road_conditions_data.road_quality * (1/road_conditions_data.accident_history + 1)
    score += (road_conditions_data.lighting_conditions * road_conditions_data.average_speed)
    
    if road_conditions_data.incident_reports != None:
        score -= road_conditions_data.incident_reports

    if weather_data.wind_speed != None:
        score -= weather_data.wind_speed

    safety_score_output = SafetyScoreOutput(safety_score = score)
    return safety_score_output

def calculate_overall_commute_quality(comfort_index:float, traffic_flow_efficiency:float, safety_score:float):
    score = (comfort_index + traffic_flow_efficiency + safety_score)/3
    description = __resolve_descriptive_value(score)
    
    overall_commute_quality_output = OverallCommuteQualityModel(overall_commute_quality_score=score, overall_commute_quality=description)
    return overall_commute_quality_output

def __resolve_descriptive_value(overall_quality_score):
    if overall_quality_score < 0:
        return "Poor"
    elif 0 < overall_quality_score < 50:
        return "Average"
    elif overall_quality_score > 50:
        return "Good"

 #Applies the transformations and calculates the overall commute quality   
def apply_transformations(weather_data_model, traffic_data_model, road_conditions_model):
    weather_output = calculate_comfot_index(weather_data_model)
    traffic_output = calculate_traffic_efficiency_flow(traffic_data_model)
    safety_score_output = calculate_safety_score(weather_data_model, traffic_data_model, road_conditions_model)

    overall_commute_quality = calculate_overall_commute_quality(weather_output.comfort_index, traffic_output.traffic_efficiency_flow, safety_score_output.safety_score)
    print("Overall commute quality: ", overall_commute_quality.model_dump())