import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def qr_code_image_copy(url: str='www.google.com', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This end point 'GET' request with url or string as a parameter. The API will return an image of the QR code, which can be downloaded by the client."
    
    """
    url = f"https://qr27.p.rapidapi.com/qr"
    querystring = {}
    if url:
        querystring['url'] = url
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "qr27.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

