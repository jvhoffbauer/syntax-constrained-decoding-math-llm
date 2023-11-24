import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def validate_email_with_ip_v1(ipaddress: str, email: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Email Validation Endpoint with IP for Geolocation"
    ipaddress: The IP Address the email signed up from (Can be blank, but parameter required)
        email: The email address you want to validate

        apikey: Your API Key, found in your account

        
    """
    url = f"https://zerobounce1.p.rapidapi.com/v1/validatewithip"
    querystring = {'ipaddress': ipaddress, 'email': email, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zerobounce1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def validate_v1(email: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Email Validation Endpoint"
    email: The email address you want to validate
        apikey: Your API Key, found in your account.
        
    """
    url = f"https://zerobounce1.p.rapidapi.com/v1/validate"
    querystring = {'email': email, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zerobounce1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

