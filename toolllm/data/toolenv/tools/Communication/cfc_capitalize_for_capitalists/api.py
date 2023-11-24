import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def capitalize_it(text: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "CAPITALIZE YOUR TEXT, USE THIS ENDPOINT!!!"
    
    """
    url = f"https://cfc-capitalize-for-capitalists.p.rapidapi.com/"
    querystring = {'text': text, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cfc-capitalize-for-capitalists.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

