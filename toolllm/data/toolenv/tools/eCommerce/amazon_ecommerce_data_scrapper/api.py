import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_product_offers(productid: str, api_key: str, offers: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GET Product Offers"
    
    """
    url = f"https://amazon-ecommerce-data-scrapper.p.rapidapi.com/products/{productid}/{offers}"
    querystring = {'api_key': api_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "amazon-ecommerce-data-scrapper.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_product_reviews(reviews: str, productid: str, api_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GET Product Reviews"
    
    """
    url = f"https://amazon-ecommerce-data-scrapper.p.rapidapi.com/products/{productid}/{reviews}"
    querystring = {'api_key': api_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "amazon-ecommerce-data-scrapper.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

