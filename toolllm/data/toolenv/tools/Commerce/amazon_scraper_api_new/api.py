import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_amazon_search_results(searchquery: str, api_key: str='11a8d8c8d681a5d9902659a72db4a590', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The SearchItems operation searches for items on Amazon based on a search query. The Amazon Product Advertising API returns up to ten items per search request.
		
		A SearchItems request requires a search category, which, if not specified, defaults to "All" and value for at least one of the Keywords, Actor, Artist, Author, Brand, or Title for searching items on Amazon.
		
		 However, note that it is mandatory to provide at least one of the above-mentioned parameters."
    
    """
    url = f"https://amazon-scraper-api-new.p.rapidapi.com/search/{searchquery}"
    querystring = {}
    if api_key:
        querystring['api_key'] = api_key
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "amazon-scraper-api-new.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

