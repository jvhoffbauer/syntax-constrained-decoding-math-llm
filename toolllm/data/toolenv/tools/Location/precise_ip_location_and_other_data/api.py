import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_location_and_other_data_for_ip_address(ip: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This end point takes a 'GET' request with IP address as parameter and returns json file with data"
    
    """
    url = f"https://precise-ip-location-and-other-data.p.rapidapi.com/location"
    querystring = {'ip': ip, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "precise-ip-location-and-other-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

