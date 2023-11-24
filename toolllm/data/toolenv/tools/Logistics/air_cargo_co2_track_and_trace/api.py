import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def pull_track(awb: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "By providing a valid AWB, you can get tracking information for the shipment."
    awb: provide valid AWB number
        
    """
    url = f"https://air-cargo-co2-track-and-trace.p.rapidapi.com/track"
    querystring = {'awb': awb, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "air-cargo-co2-track-and-trace.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

