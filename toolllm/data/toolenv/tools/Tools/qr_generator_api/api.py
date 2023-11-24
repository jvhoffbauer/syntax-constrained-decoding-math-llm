import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def generate(text: str, backcolor: str='#ffffff', forecolor: str='#000000', pixel: int=10, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Generate HTML image-tag with base64-image-string as QR code of input text (Query Parameter)"
    text: QR Code Text Content
        backcolor: (Optional) Background color in hexadecimal value (Default: White = #ffffff). Note: Should start with # prefix, and each basic-color (red, green, blue) should has two hex-digits.
        forecolor: (Optional) Foreground color in hexadecimal value (Default: Black = #000000). Note: Should start with # prefix, and each basic-color (red, green, blue) should has two hex-digits.
        pixel: (Optional) QR Code pixel (Default: 10)
        
    """
    url = f"https://qr-generator-api.p.rapidapi.com/api/qrcode/generate"
    querystring = {'text': text, }
    if backcolor:
        querystring['backColor'] = backcolor
    if forecolor:
        querystring['foreColor'] = forecolor
    if pixel:
        querystring['pixel'] = pixel
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "qr-generator-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

