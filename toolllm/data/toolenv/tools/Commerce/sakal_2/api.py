import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def step14(name: bool, query_param: str='2', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "step14"
    name: string
        query_param: 2
        
    """
    url = f"https://sakal_2.p.rapidapi.com/posts/{name}"
    querystring = {}
    if query_param:
        querystring['Query_param'] = query_param
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sakal_2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

