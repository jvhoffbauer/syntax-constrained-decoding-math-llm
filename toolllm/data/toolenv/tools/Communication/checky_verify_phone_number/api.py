import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_verify(phone: str, country: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "To use this endpoint, you need to make an HTTP GET request to the API with the phone and country parameters in the query string."
    phone: The phone number to verify. It should be provided without any spaces or special characters.
        country: The two-letter country code of the phone number.  eg **US**, **CA**, **FR** etc.
        
    """
    url = f"https://checky-verify-phone-number.p.rapidapi.com/verify"
    querystring = {'phone': phone, 'country': country, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "checky-verify-phone-number.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

