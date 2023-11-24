import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def amberwaves_retrieve_paged_collection(alias: str, start: int, api_key: str, size: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieves a paged collection of amber waves content nodes filtered by a particular section alias, ordered by descending release date."
    alias: A string parameter that specifies a series alias used for filtering. (FromUri)
        start: A zero-index integer parameter that specifies the desired starting index (0 for page 1, 100 for page 2, etc...) (FromUri)
        api_key: api key
        size: An integer parameter that specifies the desired page size. (FromUri)
        
    """
    url = f"https://t14ha70d-usda-v1.p.rapidapi.com/content/Amber Waves"
    querystring = {'alias': alias, 'start': start, 'api_key': api_key, 'size': size, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "t14ha70d-usda-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

