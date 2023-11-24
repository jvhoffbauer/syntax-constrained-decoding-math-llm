import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_amazon_product_offer(productid: str, api_key: str='1db21d9fecb9ecb37b7d45aeff4a0e42', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Amazon Product Offer"
    
    """
    url = f"https://zh-amazon-data-scraper.p.rapidapi.com/products/{productid}/offers"
    querystring = {}
    if api_key:
        querystring['api_key'] = api_key
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zh-amazon-data-scraper.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_amazon_product_review(productid: str, api_key: str='1db21d9fecb9ecb37b7d45aeff4a0e42', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Amazon Product Review"
    
    """
    url = f"https://zh-amazon-data-scraper.p.rapidapi.com/products/{productid}/reviews"
    querystring = {}
    if api_key:
        querystring['api_key'] = api_key
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zh-amazon-data-scraper.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

