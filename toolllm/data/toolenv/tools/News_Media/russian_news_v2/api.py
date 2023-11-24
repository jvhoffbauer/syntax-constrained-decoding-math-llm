import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_articles_from_individual_newspapers(newspaperid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "containing Russia keyword Russia"
    
    """
    url = f"https://russian-news1.p.rapidapi.com/news/{newspaperid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "russian-news1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_russian_news(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns russian news from all over the world."
    
    """
    url = f"https://russian-news1.p.rapidapi.com/news"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "russian-news1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

