import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def openapi_openapi_json_get(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://places-in-radius.p.rapidapi.com/openapi.json"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "places-in-radius.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def places_in_radius_places_in_radius_get(location_types: str, distance: int, starting_point: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns:
		-  all the facilities that meet specified category (grocery_store, gym, railway_station etc.)
		- are within specified radius from starting_point
		
		Returned data (please let us know, what additional data to provide to your plan):
		 - unique place_id
		- location (lat,lng)
		- type
		- distance data (walking and driving, counting from origin)
		- business details : email (if provided), phone"
    location_types: List of location types
        distance: Distance in meters
        starting_point: Starting point coordinates (latitude,longitude)
        
    """
    url = f"https://places-in-radius.p.rapidapi.com/places_in_radius"
    querystring = {'location_types': location_types, 'distance': distance, 'starting_point': starting_point, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "places-in-radius.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

