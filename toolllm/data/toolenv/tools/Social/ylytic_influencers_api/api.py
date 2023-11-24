import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_instagram_and_youtube_influencer(skip: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Instagram and YouTube Influencer"
    
    """
    url = f"https://ylytic-influencers-api.p.rapidapi.com/ylytic/admin/api/v1/search"
    querystring = {'skip': skip, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ylytic-influencers-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

