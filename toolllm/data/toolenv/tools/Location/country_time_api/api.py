import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def time_api(country: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Time API is a simple and convenient web service that allows you to retrieve the current time for different countries around the world. By providing the country name as a parameter, you can obtain the accurate and up-to-date local time for that specific location."
    
    """
    url = f"https://country-time-api.p.rapidapi.com/time"
    querystring = {'country': country, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "country-time-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

