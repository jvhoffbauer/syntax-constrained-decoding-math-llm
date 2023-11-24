import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def verifyemailaddresswithtoken(email: str, cca: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Verifies email address using authorization token"
    email: Email address to be verified
        cca: Signals API whether or not to check if server has \"catch all\" address (1- check, 0-do not check)
        
    """
    url = f"https://emalidate1.p.rapidapi.com/verify"
    querystring = {'email': email, }
    if cca:
        querystring['cca'] = cca
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emalidate1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def validateemailaddresswithtoken(email: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Email syntax validation using authorization token"
    email: Email address to be validated
        
    """
    url = f"https://emalidate1.p.rapidapi.com/validate"
    querystring = {'email': email, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emalidate1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

