import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def send_individual_sms(password: str, message: str, username: str, mask: str, to: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Sending SMS from the API"
    
    """
    url = f"https://notify92-sms-service.p.rapidapi.com/api/quick/message"
    querystring = {'password': password, 'message': message, 'username': username, 'mask': mask, 'to': to, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "notify92-sms-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

