import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def measurements(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GET enum array of all types of measurement"
    
    """
    url = f"https://measurement-unit-converter.p.rapidapi.com/measurements"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "measurement-unit-converter.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def convert_from_one_unit_to_another(measure: str, value: int, is_from: str, to: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Converts the given quantity in one unit to the equivalent quantity in another, for a given measurement, and returns a detailed answer."
    
    """
    url = f"https://measurement-unit-converter.p.rapidapi.com/{measure}"
    querystring = {'value': value, 'from': is_from, 'to': to, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "measurement-unit-converter.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def measurements_detailed(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GET a list of all the available measurements with unit details."
    
    """
    url = f"https://measurement-unit-converter.p.rapidapi.com/measurements/detailed"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "measurement-unit-converter.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def measure_units(measure: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GET enum array of all units of the given type."
    
    """
    url = f"https://measurement-unit-converter.p.rapidapi.com/{measure}/units"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "measurement-unit-converter.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

