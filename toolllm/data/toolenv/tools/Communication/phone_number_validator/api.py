import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def validate_phone_number(number: str, response_type: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Easily and quickly looks up details about a phone number"
    number: Enter a valid phone number. You can also include the country code **(e.g +19843323454)** and dashes are also valid **(e.g  984-332-3454)** 
        
    """
    url = f"https://phone-number-validator1.p.rapidapi.com/v1/validatephone"
    querystring = {'number': number, }
    if response_type:
        querystring['response_type'] = response_type
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "phone-number-validator1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

