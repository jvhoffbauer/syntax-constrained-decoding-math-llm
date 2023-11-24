import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def qr_code_generator_get(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This end point takes a 'GET' request with url as string parameter and returns a qr code image"
    
    """
    url = f"https://qrcodegenapi.p.rapidapi.com/qr"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "qrcodegenapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

