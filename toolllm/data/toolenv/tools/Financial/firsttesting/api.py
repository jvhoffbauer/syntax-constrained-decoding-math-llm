import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def api_ep_one(param_one: str=None, param_four: str=None, param_three: int=None, param_two: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "No description is required as of now"
    
    """
    url = f"https://firsttesting.p.rapidapi.com/"
    querystring = {}
    if param_one:
        querystring['Param-One'] = param_one
    if param_four:
        querystring['Param-Four'] = param_four
    if param_three:
        querystring['Param-Three'] = param_three
    if param_two:
        querystring['Param-Two'] = param_two
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "firsttesting.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

