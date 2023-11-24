import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def customer(is_id: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Request customer information"
    
    """
    url = f"https://perfex-crm-mekong-mmo.p.rapidapi.com/client.mmomekong.com/api/"
    querystring = {}
    if is_id:
        querystring['id'] = is_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "perfex-crm-mekong-mmo.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

