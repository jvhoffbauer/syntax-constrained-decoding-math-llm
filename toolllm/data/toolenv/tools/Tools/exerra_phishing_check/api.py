import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_stats(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get statistics about the Exerra Phishing API"
    
    """
    url = f"https://exerra-phishing-check.p.rapidapi.com/stats"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "exerra-phishing-check.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def check_a_url(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Check if a URL is a known phishing attempt"
    url: This is the URL that the API will check.
Must be a valid HTTP(s) URL or it will throw a 400
        
    """
    url = f"https://exerra-phishing-check.p.rapidapi.com/"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "exerra-phishing-check.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all(type: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all domains (or links) associated with phishing attempts. The response is very large (>≈13MB), so it is preferred to use "Check a link". 
		
		Due to the large response size (and processing) this endpoint is paid."
    
    """
    url = f"https://exerra-phishing-check.p.rapidapi.com/all/{type}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "exerra-phishing-check.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

