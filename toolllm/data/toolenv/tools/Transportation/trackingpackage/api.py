import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def trackingpackage(trackingnumber: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Track UPS, USPS and FedEx packages."
    
    """
    url = f"https://trackingpackage.p.rapidapi.com/TrackingPackage"
    querystring = {'trackingNumber': trackingnumber, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "trackingpackage.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

