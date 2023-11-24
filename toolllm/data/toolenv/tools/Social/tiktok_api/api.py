import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def getdatawithfullvideoid(video_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "complete video id is needed eg:
		
		if url is = https://www.tiktok.com/@leemayy_/video/7151736605152234779
		then video id is = 7151736605152234779"
    
    """
    url = f"https://tiktok-api10.p.rapidapi.com/aweme/v1/feed/"
    querystring = {'video_id': video_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-api10.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getdatawithurl(url: str, minimal: str, is_from_webapp: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://tiktok-api10.p.rapidapi.com/api"
    querystring = {'url': url, 'minimal': minimal, 'is_from_webapp': is_from_webapp, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-api10.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

