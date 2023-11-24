import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def send_message_to_multiple_numbers(to: str, key: str, mask: str, email: str, message: str, status: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API is useful to send a branded sms to multiple numbers"
    to: Destination Number (Default Format) 923151231016
        key: Account API Key
        mask: Masking (Branded Name)
        email: Account Email Address
        message: Message Limited to 640 characters
        status: Return Message ID
        
    """
    url = f"https://branded-sms-pakistan.p.rapidapi.com/send"
    querystring = {'to': to, 'key': key, 'mask': mask, 'email': email, 'message': message, }
    if status:
        querystring['status'] = status
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "branded-sms-pakistan.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def send_single_message(message: str, mask: str, to: int, email: str, key: str, status: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API is useful to send a branded sms to single number"
    message: Message Limited to 640 characters
        mask: Masking (Branded Name)
        to: Destination Number (Default Format) 923151231016
        email: Account Email Address
        key: Account API Key
        status: Return Message ID
        
    """
    url = f"https://branded-sms-pakistan.p.rapidapi.com/send"
    querystring = {'message': message, 'mask': mask, 'to': to, 'email': email, 'key': key, }
    if status:
        querystring['status'] = status
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "branded-sms-pakistan.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

