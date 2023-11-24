import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def camera_key_list(country: str, district: str=None, region: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Refer to [Camera Key List](https://core-api.net/traffic/guide.html)"
    
    """
    url = f"https://live-traffic-images.p.rapidapi.com/get_camera_list"
    querystring = {'country': country, }
    if district:
        querystring['district'] = district
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "live-traffic-images.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

