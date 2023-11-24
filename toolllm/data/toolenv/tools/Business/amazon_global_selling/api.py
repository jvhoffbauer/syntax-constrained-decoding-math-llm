import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def amazon(amazon: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Harmonized System (HS) code is a standardized numerical method to classify export trade products by customs authorities around the world."
    
    """
    url = f"https://amazon-global-selling.p.rapidapi.com/"
    querystring = {}
    if amazon:
        querystring['amazon'] = amazon
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "amazon-global-selling.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

