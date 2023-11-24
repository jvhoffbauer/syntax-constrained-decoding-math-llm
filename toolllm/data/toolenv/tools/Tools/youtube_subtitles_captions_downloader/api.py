import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_subtitles_plain_text(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Give the link of any YouTube video which has captions. It will return the subtitles in plain text- no formatting."
    
    """
    url = f"https://youtube-subtitles-captions-downloader.p.rapidapi.com/ytmp3/ytmp3/subtitles/"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "youtube-subtitles-captions-downloader.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

