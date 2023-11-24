import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def domain_availability(domain: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Domain availability endpoint"
    domain: The domain you want to test
        
    """
    url = f"https://domain-availability-domain-checker-pay-per-use.p.rapidapi.com/domain-availability"
    querystring = {'domain': domain, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "domain-availability-domain-checker-pay-per-use.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

