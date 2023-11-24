import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def macronutrient_distribution(activity_level: str, body_composition_goal: str, dietary_preferences: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint calculates the optimal distribution of macronutrients (carbohydrates, proteins, and fats) based on factors such as activity level, body composition goals, and dietary preferences."
    activity_level: The activity_level parameter accepts the following values:

**sedentary** - Little to no exercise.
**moderately_active** - Moderate exercise/sports 3-5 days/week.
**very_active** - Hard exercise/sports 6-7 days/week.
        body_composition_goal: The body_composition_goal parameter accepts the following values:

**weight_loss** - Goal of losing weight.
**maintenance** - Goal of maintaining current weight.
**muscle_gain** - Goal of gaining muscle.

        dietary_preferences: The dietary_preferences parameter allows users to specify their dietary preferences. It can be any string value representing the individual's dietary choices or restrictions, such as \"**vegetarian**,\" \"**vegan**,\" \"**pescatarian**,\" or \"**gluten-free**.\"
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/mnd"
    querystring = {'activity_level': activity_level, 'body_composition_goal': body_composition_goal, 'dietary_preferences': dietary_preferences, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def target_heart_rate(fitness_level: str, age: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint calculates the target heart rate range for cardiovascular exercise based on the user's age and fitness level. It uses the Karvonen method to determine the target heart rate zone."
    fitness_level: The fitness level of the user.

The fitness_level parameter accepts the following values:
**beginner** - Beginner fitness level.
**intermediate** - Intermediate fitness level.
**advanced** - Advanced fitness level.
        age: The age of the user in years.
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/thr"
    querystring = {'fitness_level': fitness_level, 'age': age, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def daily_water_intake(climate: str, activity_level: str, weight: int, unit: str='liters', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Daily Water Intake Recommendation endpoint calculates the daily recommended water intake based on factors such as weight, activity level, and climate. It provides flexibility by allowing you to specify the unit of measurement for the water intake, either in liters or ounces."
    climate: The climate in which the individual is located.

The climate parameter accepts the following values:
**normal** - Average climate
**hot** - Hot climate
**cold** - Cold climate
        activity_level: The activity level of the individual. 

The activity_level parameter accepts the following values:
**sedentary** - Little to no exercise
**lightly_active** - Light exercise/sports 1-3 days/week
**moderately_active** - Moderate exercise/sports 3-5 days/week
**very_active** - Hard exercise/sports 6-7 days/week
**extra_active** - Very hard exercise/sports and physical job or 2x training
        weight: The weight of the individual in **kilograms (kg)**.
        unit: The unit of measurement for the water intake. 
(Default) **ounces**
 Specify **liters** to get the result in liters instead.
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/dwi"
    querystring = {'climate': climate, 'activity_level': activity_level, 'weight': weight, }
    if unit:
        querystring['unit'] = unit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def daily_caloric_needs(activity_level: str, gender: str, goal: str, weight: int, height: int, age: int, equation: str='mifflin', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint provides a simple and efficient way to calculate daily caloric needs based on various factors such as age, weight, height, activity level, and goal. It offers different formulas or approaches for caloric needs estimation, including the popular Harris-Benedict equation and Mifflin-St. Jeor equation."
    activity_level: The activity level of the person. Valid values are \"**sedentary**\", \"**lightly_active**\", \"**moderately_active**\", \"**very_active**\", or \"**extra_active**\".
        gender: The gender of the person. Valid values are \"**male**\" or \"**female**\".
        goal: The goal of the person. Valid values are \"**weight_loss**\", \"**maintenance**\", or \"**weight_gain**\".
        weight: The weight of the person in **kilograms**.
        height: The height of the person in **centimeters**.
        age: The age of the person in years.
        equation: The equation to use for caloric needs estimation. Valid values are \"**harris**\" (default) or \"**mifflin**\".
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/dcn"
    querystring = {'activity_level': activity_level, 'gender': gender, 'goal': goal, 'weight': weight, 'height': height, 'age': age, }
    if equation:
        querystring['equation'] = equation
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ideal_body_weight(gender: str, height: int, body_frame: str, formula: str='hamwi', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint allows you to calculate the ideal weight range based on factors like height, body frame size, and gender. The endpoint provides different formulas and approaches for ideal weight estimation, such as the Hamwi method and the Devine formula."
    gender: The gender of the person. It can be either \"**male**\" or \"**female**\".
        height: The height in **centimeters (cm)** of the person for whom you want to calculate the ideal weight.
        body_frame: The body frame size of the person. It can be one of the following values: \"**small**\", \"**medium**\", or \"**large**\".
        formula: You can include an optional query parameter to specify the formula or approach for ideal weight estimation. It can be one of the following values:
\"**hamwi**\" (default): The Hamwi method for ideal weight calculation.
\"**devine**\": The Devine formula for ideal weight calculation.
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/ibw"
    querystring = {'gender': gender, 'height': height, 'body_frame': body_frame, }
    if formula:
        querystring['formula'] = formula
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def basal_metabolic_rate_bmr(weight: int, height: int, age: int, gender: str, equation: str='mifflin', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint allows you to calculate the Basal Metabolic Rate (BMR) based on age, weight, height, and gender parameters. The BMR represents the number of calories needed to maintain basic bodily functions at rest."
    weight: The weight in **kilograms**.
        height: The height in **centimeters**.
        age: The age in **years**.
        gender: The gender (either "**male**" or "**female**").
        equation: (optional string): The equation to use for the calculation. Valid options are "**mifflin**" (default) or "**harris**".
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/bmr"
    querystring = {'weight': weight, 'height': height, 'age': age, 'gender': gender, }
    if equation:
        querystring['equation'] = equation
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def body_mass_index(height: int, weight: int, units: str='metric', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint calculates the BMI based on the provided height and weight parameters."
    height: The height in **centimeters**. Required.
        weight: The weight in **kilograms**. Required.
        units: The desired units of measurement to implement in the JSON Response. Possible values are **metric** (default) or **imperial**. (Optional).
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/bmi"
    querystring = {'height': height, 'weight': weight, }
    if units:
        querystring['units'] = units
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bmi_imperial(weight: int, height: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint calculates the BMI based on the provided height and weight parameters in imperial units."
    weight: The weight in **pounds**. Required
        height: The height in **inches**. Required
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/bmi/imperial"
    querystring = {'weight': weight, 'height': height, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bodyfat(height: int, weight: int, gender: str, age: int, unit: str='metric', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint calculates the body fat percentage based on the provided gender, age, height, and weight parameters."
    height: The height in **centimeters**. Required.
        weight: The weight in **kilograms**. Required.
        gender: The gender of the person. Possible values are **male** or **female**. Required.
        age: The age of the person in years. Required.
        unit: The desired units of measurement to implement in the JSON Response. Possible values are **metric** (default) or **imperial**. (Optional).
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/bodyfat"
    querystring = {'height': height, 'weight': weight, 'gender': gender, 'age': age, }
    if unit:
        querystring['unit'] = unit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bodyfat_imperial(age: int, weight: int, gender: str, height: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint calculates the body fat percentage based on the provided gender, age, height, and weight parameters in imperial units."
    age: The age of the person in **years**. Required.
        weight: The weight of the person in **pounds**. Required.
        gender: The gender of the person. Must be either '**male**' or '**female**'. Required.
        height: The height of the person in **inches**. Required.
        
    """
    url = f"https://health-calculator-api.p.rapidapi.com/bodyfat/imperial"
    querystring = {'age': age, 'weight': weight, 'gender': gender, 'height': height, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "health-calculator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

