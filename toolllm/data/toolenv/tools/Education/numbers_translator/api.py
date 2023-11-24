import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def numbers_translator(text: str='23879908709817834', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Numbers Translator"
    text: Numerical value of the number
        
    """
    url = f"https://numbers-spell.p.rapidapi.com/numbers"
    querystring = {}
    if text:
        querystring['text'] = text
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "numbers-spell.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

