import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def single_lookup(ip_address: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "## Single Lookup
		
		This is the primary IpForensics endpoint. It is used to look up any given IPv4 or IPv6 addresses. 
		
		To call this endpoint, simply attach an IP address to the API's base URL (HTTP GET method):
		
		**Each request to the single IP lookup endpoint consumes 1 token.**"
    apikey: Your API Key - Obtain the API key from your dashboard
        
    """
    url = f"https://ip-forensics-ip-geolocation-currency-exchange-and-threat-intelligence-api.p.rapidapi.com/single"
    querystring = {'ip_address': ip_address, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ip-forensics-ip-geolocation-currency-exchange-and-threat-intelligence-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

