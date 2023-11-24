import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def list_all_layers(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    ""
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/geosimulator/layers?page=1&search=&filter="
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_all_simulations(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    ""
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/geosimulator/simulation"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_applications(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List all your applications"
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/geosimulator/application"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_all_simulations_of_a_group(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Enter groupID in the route"
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/geosimulator/group/groupID/simulations"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def view_application(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Enter your applicationID in the route"
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/geosimulator/application/applicationID"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def view_simulation(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Enter simulationID in route"
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/geosimulator/simulation/simulationID"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_all_groups(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List All Groups"
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/geosimulator/group"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def simulations_by_application_id(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Enter applicationID in route"
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/geosimulator/application/simulations/applicationID"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def view_layer(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Enter layerID in route"
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/geosimulator/layers/layerID"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def view_user_s_profile(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "View Profile (Enter your user-id in route)"
    
    """
    url = f"https://nisostech-geosimulator-apis-v1.p.rapidapi.com/api/v1/user/user-id"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nisostech-geosimulator-apis-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

