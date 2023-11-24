import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def weather_data(start: str, lat: int, param: str, lon: int, end: str, freq: str='D', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Hourly historical and forecast weather parameters in time-series format, from 1950 to 16 days ahead for any location."
    
    """
    url = f"https://oikoweather.p.rapidapi.com/weather"
    querystring = {'start': start, 'lat': lat, 'param': param, 'lon': lon, 'end': end, }
    if freq:
        querystring['freq'] = freq
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "oikoweather.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

