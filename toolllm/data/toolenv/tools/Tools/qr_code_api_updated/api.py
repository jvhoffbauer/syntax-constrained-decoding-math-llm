import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def qr_endpoint(url: str='www.google.com', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "qr endpoint to  surf to any website"
    
    """
    url = f"https://qr-code-api-updated.p.rapidapi.com/qr-code"
    querystring = {}
    if url:
        querystring['url'] = url
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "qr-code-api-updated.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

