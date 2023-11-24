import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def rapid_api_of_dung_bui_end_point(livecommentsquery: str='STRING', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "lưu webhook call"
    livecommentsquery: livecommentsQuery
        
    """
    url = f"https://dung-bui.p.rapidapi.comhttps://dung-bui.p.rapidapi.com"
    querystring = {}
    if livecommentsquery:
        querystring['livecommentsQuery'] = livecommentsquery
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "dung-bui.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

