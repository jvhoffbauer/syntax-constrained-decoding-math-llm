import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_pin_data(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint will return back all information about a specific pin on Pinterest."
    url: use pin url: https://pin.it/1JyKAWz
or https://www.pinterest.com/pin/898608931881203244/
or 898608931881203244
        
    """
    url = f"https://pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com/api/data"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

