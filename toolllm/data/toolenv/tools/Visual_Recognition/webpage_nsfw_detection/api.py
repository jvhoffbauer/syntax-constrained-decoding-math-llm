import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def visual_detection(url: str, width: int=1920, height: int=1080, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Detect NSFW Content based on Screenshot of the Webpage Only"
    url: Complete URL of the webpage you want to check for NSFW Content
        
    """
    url = f"https://webpage-nsfw-detection.p.rapidapi.com/api/visual"
    querystring = {'url': url, }
    if width:
        querystring['width'] = width
    if height:
        querystring['height'] = height
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webpage-nsfw-detection.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

