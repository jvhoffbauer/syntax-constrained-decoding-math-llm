import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_news_by_id(newspaperid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get specific news resource"
    
    """
    url = f"https://climate-change-news86.p.rapidapi.com/news/{newspaperid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "climate-change-news86.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_news(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return back all climate change news"
    
    """
    url = f"https://climate-change-news86.p.rapidapi.com/news"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "climate-change-news86.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

