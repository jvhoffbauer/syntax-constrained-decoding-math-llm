import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def convert(to: str, api_key: str, amount: int, is_from: str, date: str='2021-03-10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint is used to convert any amount from one currency to another."
    
    """
    url = f"https://metalpriceapi.p.rapidapi.com/v1/convert"
    querystring = {'to': to, 'api_key': api_key, 'amount': amount, 'from': is_from, }
    if date:
        querystring['date'] = date
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "metalpriceapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

