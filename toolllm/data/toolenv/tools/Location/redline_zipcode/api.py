import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def multiple_zip_codes_to_location_information(zipcodes: str, units: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns location information for multiple zip codes (up to 100).  This information includes city, state, latitude, longitude, and time zone information.  It also contains a list of other acceptable city names for the locations.  Each zip code provided will count as a separate request. For example, if you send 5 zip codes, you will be charged for 5 requests."
    zipcodes: Zip Codes (Comma separated) - 100 Max
        units: Units: degrees or radians
        
    """
    url = f"https://redline-redline-zipcode.p.rapidapi.com/rest/multi-info.json/{zipcodes}/{units}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redline-redline-zipcode.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def zip_codes_within_radius(radius: int, zipcode: int, units: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all zip codes within a radius of the given zip code."
    radius: Radius (in appropriate units)
        zipcode: Zipcode
        units: Distance units: mile or km
        
    """
    url = f"https://redline-redline-zipcode.p.rapidapi.com/rest/radius.json/{zipcode}/{radius}/{units}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redline-redline-zipcode.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def distance_between_zip_codes(zipcode1: int, zipcode2: int, units: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Determine the distance between two zip codes."
    zipcode1: First zip code
        zipcode2: Second zip code
        units: Distance units: mile or km
        
    """
    url = f"https://redline-redline-zipcode.p.rapidapi.com/rest/distance.json/{zipcode1}/{zipcode2}/{units}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redline-redline-zipcode.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def zip_code_to_location_information(zipcode: int, units: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns location information for a zip code.  This information includes city, state, latitude, longitude, and time zone information.  It also contains a list of other acceptable city names for the location."
    zipcode: Zipcode
        units: Units: degrees or radians
        
    """
    url = f"https://redline-redline-zipcode.p.rapidapi.com/rest/info.json/{zipcode}/{units}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redline-redline-zipcode.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def location_to_zip_code(city: str, state: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns zip codes for a given city."
    city: City
        state: State
        
    """
    url = f"https://redline-redline-zipcode.p.rapidapi.com/rest/city-zips.json/{city}/{state}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redline-redline-zipcode.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def state_to_zip_codes(state: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all zip codes for a state.  Each 10 zip codes returns are charged as separate request. For example, if the state you select returns 200 zip codes, you will be charged for 20 requests."
    state: State Abbreviation (e.g. RI)
        
    """
    url = f"https://redline-redline-zipcode.p.rapidapi.com/rest/state-zips.json/{state}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redline-redline-zipcode.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

