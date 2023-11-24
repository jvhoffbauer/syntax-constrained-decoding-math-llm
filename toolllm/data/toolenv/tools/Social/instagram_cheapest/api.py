import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def userinfo(username: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get userinfo by username"
    
    """
    url = f"https://instagram-cheapest.p.rapidapi.com/api/v1/instagram/user/{username}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-cheapest.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_medias(user_id: str, next_max_id: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get user_medias by user_id"
    
    """
    url = f"https://instagram-cheapest.p.rapidapi.com/api/v1/instagram/user_media"
    querystring = {'user_id': user_id, }
    if next_max_id:
        querystring['next_max_id'] = next_max_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-cheapest.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

