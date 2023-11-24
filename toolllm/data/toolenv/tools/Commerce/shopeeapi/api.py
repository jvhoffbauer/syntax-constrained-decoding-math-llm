import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_products(region: str, q: str, p: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search product & Paginate"
    region: The region must one of [\\\"en\\\", \\\"sg\\\", \\\"my\\\", \\\"id\\\", \\\"th\\\", \\\"vn\\\", \\\"ph\\\", \\\"tw\\\", \\\"br\\\", \\\"cl\\\", \\\"mx\\\", \\\"co\\\"]
        q: A product search query
        p: Page number
        
    """
    url = f"https://shopeeapi2.p.rapidapi.com/{region}/search"
    querystring = {'q': q, }
    if p:
        querystring['p'] = p
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shopeeapi2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def product_details(region: str, path: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get shopee product details"
    region: The region. must be one of [\\\"en\\\", \\\"sg\\\", \\\"my\\\", \\\"id\\\", \\\"th\\\", \\\"vn\\\", \\\"ph\\\", \\\"tw\\\", \\\"br\\\", \\\"cl\\\", \\\"mx\\\", \\\"co\\\"]
        path: Path parameters
        
    """
    url = f"https://shopeeapi2.p.rapidapi.com/{region}/{path}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shopeeapi2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

