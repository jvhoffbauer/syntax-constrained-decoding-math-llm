import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search(limit: str, query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Insert the search query and retrieve the most relevant results from Google Search in JSON format."
    limit: The number of results you want to retrieve
        query: The search string of your choice.
        
    """
    url = f"https://google-search-api4.p.rapidapi.com/search"
    querystring = {'limit': limit, 'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "google-search-api4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

