import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def descriptor(zipcode: str, read_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "<code>GET</code> <code>/descriptor?zipcode={zipcode}&read_key={read_key}</code>
		
		### Parameters
		
		> | name    | type     | data type | description                |
		> | ------- | -------- | --------- | -------------------------- |
		> | zipcode | required | int       | zipcode of user's location |
		> | api_key | required | string    | user's purpleair API key   |
		
		### Responses
		
		> | http code | content-type       | response                                                       |
		> | --------- | ------------------ | -------------------------------------------------------------- |
		> | `200`     | `application/json` | `JSON object`                                                  |
		> | `400`     | `application/json` | `{error: "Invalid zipcode"}`                                   |
		> | `400`     | `application/json` | `{"error": "No sensors found within the range of "x" miles."}` |
		> | `400`     | `application/json` | `{"error": "No read key or zipcode provided."}`                |
		
		### Example response
		
		> ```py
		>    {
		>        "description": "Good",
		>        "zipcode": 11101
		>    }
		> ```"
    
    """
    url = f"https://coolcorridors.p.rapidapi.com/descriptor"
    querystring = {'zipcode': zipcode, 'read_key': read_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "coolcorridors.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def color(zipcode: str, read_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "<code>GET</code> <code>/color?zipcode={zipcode}&read_key={read_key}</code>
		
		### Parameters
		
		> | name    | type     | data type | description                |
		> | ------- | -------- | --------- | -------------------------- |
		> | zipcode | required | int       | zipcode of user's location |
		> | api_key | required | string    | user's purpleair API key   |
		
		### Responses
		
		> | http code | content-type       | response                                                       |
		> | --------- | ------------------ | -------------------------------------------------------------- |
		> | `200`     | `application/json` | `JSON object`                                                  |
		> | `400`     | `application/json` | `{error: "Invalid zipcode"}`                                   |
		> | `400`     | `application/json` | `{"error": "No sensors found within the range of "x" miles."}` |
		> | `400`     | `application/json` | `{"error": "No read key or zipcode provided."}`                |
		
		### Example response
		
		> ```py
		>    {
		>        "color": "0xFF00FF",
		>        "zipcode": 11101
		>    }
		> ```"
    
    """
    url = f"https://coolcorridors.p.rapidapi.com/color"
    querystring = {'zipcode': zipcode, 'read_key': read_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "coolcorridors.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

