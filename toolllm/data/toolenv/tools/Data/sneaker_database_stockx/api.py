import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_products(limit: str, keywords: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a collection of products.
		
		**Parameters ** (All the parameters must be string to work, even the limit| Don't worry about the data conversion!)
		-> keyword
		-> limit ( Max 20 per call)"
    limit: max. 20 per call
        
    """
    url = f"https://sneaker-database-stockx.p.rapidapi.com/getproducts"
    querystring = {'limit': limit, 'keywords': keywords, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sneaker-database-stockx.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_most_popular(limit: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns the most popular sneakers from StockX, FlightClub, Goat, and Stadium Goods.
		
		**Parameters:**
		limit"
    limit: max. 20 per call
        
    """
    url = f"https://sneaker-database-stockx.p.rapidapi.com/mostpopular"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sneaker-database-stockx.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_products_prices(styleid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns Prices of Sneakers:
		
		**Parameters:**
		styleId"
    
    """
    url = f"https://sneaker-database-stockx.p.rapidapi.com/productprice"
    querystring = {'styleId': styleid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sneaker-database-stockx.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

