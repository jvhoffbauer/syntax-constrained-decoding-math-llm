import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_county_boundary(coordinates: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint retrieves the  county property boundaries associated with a given latitude and longitude coordinate, if any exist."
    
    """
    url = f"https://property-lines.p.rapidapi.com/getCountyBoundary"
    querystring = {'coordinates': coordinates, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "property-lines.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_counties_in_state_boundaries(coordinates: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint retrieves all county boundaries in the state associated with a given latitude and longitude coordinate, if any exist."
    
    """
    url = f"https://property-lines.p.rapidapi.com/getAllCountiesInStateBoundaries"
    querystring = {'coordinates': coordinates, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "property-lines.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_single_boundary(coordinates: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint retrieves the property boundaries associated with a given latitude and longitude coordinate, if any exist."
    
    """
    url = f"https://property-lines.p.rapidapi.com/getSingleBoundary"
    querystring = {'coordinates': coordinates, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "property-lines.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_state_boundary(coordinates: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint retrieves the  state property boundaries associated with a given latitude and longitude coordinate, if any exist."
    
    """
    url = f"https://property-lines.p.rapidapi.com/getStateBoundary"
    querystring = {'coordinates': coordinates, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "property-lines.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_radius_boundary(coordinates: str, radius: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint retrieves the property boundaries associated with a given latitude and longitude coordinate within a given radius, if any exist."
    radius: Radius of property boundaries to return. Optional. (Default value 100m)
        
    """
    url = f"https://property-lines.p.rapidapi.com/getRadiusBoundary"
    querystring = {'coordinates': coordinates, }
    if radius:
        querystring['radius'] = radius
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "property-lines.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

