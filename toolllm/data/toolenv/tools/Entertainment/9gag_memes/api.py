import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_section_of_memes(limit: int=20, filter: str='Animal', offset: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This api will return section (category) of the memes"
    
    """
    url = f"https://9gag-memes.p.rapidapi.com/v1/fetch-sections"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if filter:
        querystring['filter'] = filter
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "9gag-memes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_20_random_memes(post_section: str='get this value from fetch-sections api response', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Endpoint will return 20 memes"
    
    """
    url = f"https://9gag-memes.p.rapidapi.com/v1/fetch-memes"
    querystring = {}
    if post_section:
        querystring['post_section'] = post_section
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "9gag-memes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

