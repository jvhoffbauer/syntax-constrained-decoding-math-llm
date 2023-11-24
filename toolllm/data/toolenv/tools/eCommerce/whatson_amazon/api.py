import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def list_shops(page: int=0, size: int=30, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List supported shops"
    page: Start from 0
        size: Size of the page, min : 30 - max : 50
        
    """
    url = f"https://whatson-amazon.p.rapidapi.com/shop/_list"
    querystring = {}
    if page:
        querystring['page'] = page
    if size:
        querystring['size'] = size
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "whatson-amazon.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_product(keyword: str, shopnameid: str, cache: str=None, extrameta: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Crawl live data from the webpage"
    keyword: Search key string
        shopnameid: NameId of the target shop
        cache: speed up response time by activating cache
        extrameta: a flag used to add extrameta in the response
        
    """
    url = f"https://whatson-amazon.p.rapidapi.com/item/_search"
    querystring = {'keyword': keyword, 'shopNameId': shopnameid, }
    if cache:
        querystring['cache'] = cache
    if extrameta:
        querystring['extrameta'] = extrameta
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "whatson-amazon.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

