import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search(plate: str='100TA49', function: str='getktypefornumplatefrance', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://french-vehicle-license-plate-api.p.rapidapi.com/default/BVSLambda"
    querystring = {}
    if plate:
        querystring['plate'] = plate
    if function:
        querystring['function'] = function
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "french-vehicle-license-plate-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

