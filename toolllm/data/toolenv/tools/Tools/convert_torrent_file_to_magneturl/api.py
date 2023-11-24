import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def api(urltorrnet: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Torrent"
    
    """
    url = f"https://convert-torrent-file-to-magneturl.p.rapidapi.com/TorrentToMagnet"
    querystring = {'urlTorrnet': urltorrnet, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "convert-torrent-file-to-magneturl.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

