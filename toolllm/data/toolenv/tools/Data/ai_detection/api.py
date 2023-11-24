import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def check_text(term: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint allows you to easily submit text for analysis and determine if it was generated by a machine or a human. Just please **do not use any special characters** - it wont work :) . 
		Note: **The results start to get reliable after around 50 tokens.**"
    
    """
    url = f"https://ai-detection.p.rapidapi.com/check/{term}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ai-detection.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

