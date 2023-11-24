import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_quotes(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Quote List"
    
    """
    url = f"https://quotes56.p.rapidapi.com/quotes"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "quotes56.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

