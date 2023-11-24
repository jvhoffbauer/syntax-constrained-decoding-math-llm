import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def searchbyaddress(address: str='1600 Pennsylvania Ave. NW Washington, DC 20500', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search local walk scores and regional bike and transit data by address. NWI score range from 0-20."
    
    """
    url = f"https://opennwi.p.rapidapi.com/scores"
    querystring = {}
    if address:
        querystring['address'] = address
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opennwi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

