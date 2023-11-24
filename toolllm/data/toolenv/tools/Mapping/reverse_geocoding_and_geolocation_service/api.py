import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def gettimezone(longitude: int, latitude: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Finds the local timezone for any given geo-location point by lat and long and returns timezone information with Timezone name, Timezone id and current local time."
    
    """
    url = f"https://geocodeapi.p.rapidapi.com/GetTimezone"
    querystring = {'longitude': longitude, 'latitude': latitude, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "geocodeapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getnearestcities(latitude: int, longitude: int, range: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a readable place name as nearest 3 cities with population, country and distance based on given latitude/longitude pair."
    latitude: latitude in decimal degrees (wgs84)
        longitude: longitude in decimal degrees (wgs84)
        range: max radial range for lookup in meter (0=no range)
        
    """
    url = f"https://geocodeapi.p.rapidapi.com/GetNearestCities"
    querystring = {'latitude': latitude, 'longitude': longitude, 'range': range, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "geocodeapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getlargestcities(latitude: int, longitude: int, range: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns 5 largest cities within a given radial range with name, population, country and distance."
    latitude: latitude in decimal degrees (wgs84)
        longitude: longitude in decimal degrees (wgs84)
        range: radial lookup range in meters (max 100.000)
        
    """
    url = f"https://geocodeapi.p.rapidapi.com/GetLargestCities"
    querystring = {'latitude': latitude, 'longitude': longitude, 'range': range, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "geocodeapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

