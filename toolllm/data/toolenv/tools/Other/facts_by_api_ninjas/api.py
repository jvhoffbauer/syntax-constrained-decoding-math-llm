import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def v1_facts(limit: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API Ninjas Facts API endpoint"
    limit: How many results to return. Must be between **1** and **30**. Default is **1**.
        
    """
    url = f"https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "facts-by-api-ninjas.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

