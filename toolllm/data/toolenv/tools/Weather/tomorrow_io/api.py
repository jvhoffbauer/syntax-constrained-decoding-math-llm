import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def retrieveatile_basic(zoom: str, x: str, field: str, y: str, timeformat: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/map/tile/{zoom}/{x}/{y}/{field}/{timeformat}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveanalert(alertid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/alerts/{alertid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def linkedlocations(alertid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/alerts/{alertid}/locations"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def listalerts(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/alerts"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveevents_basic(insights: str, buffer: str, location: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    insights: (Required) Pre-defined category names or custom insight IDs
        buffer: The buffer around locations, in case of pre-defined insight categories (in km)
        location: (Required) ID of a pre-defined location or latlong string
        
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/events"
    querystring = {'insights': insights, 'buffer': buffer, 'location': location, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def listlocations(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/locations"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveaninsight(insightid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/insights/{insightid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def listinsights(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/insights"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrievetimelines_basic(starttime: str, fields: str, endtime: str, timezone: str, units: str, timesteps: str, location: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    starttime: Start time in ISO 8601 format "2019-03-20T14:09:50Z" (defaults to now)
        fields: (Required) Selected fields from our data layers (polygon/polyline default to Max, if not suffix is not specified)
        endtime: End time in ISO 8601 format "2019-03-20T14:09:50Z" 
        timezone: Timezone of time values, according to IANA Timezone Names (defaults to UTC)
        units: Units of field values, either "metric" or "imperial" (defaults to metric)
        timesteps: Timesteps of the timelines: "1m", "5m", "15m", "30m", "1h", "1d", and "current"
        location: (Required) ID of a pre-defined location or latlong string
        
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/timelines"
    querystring = {'startTime': starttime, 'fields': fields, 'endTime': endtime, 'timezone': timezone, 'units': units, 'timesteps': timesteps, 'location': location, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrievealocation(locationid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://tomorrow-io1.p.rapidapi.com/locations/{locationid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tomorrow-io1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

