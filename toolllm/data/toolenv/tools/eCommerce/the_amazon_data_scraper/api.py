import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_amazon_product_reviews(productid: str, api_key: str='034a629dc2291c164b9de760eecd0482', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Endpoint can be accessed with /products/{productId}/reviews gives you all the review info for a certain amazon product"
    
    """
    url = f"https://the-amazon-data-scraper.p.rapidapi.com/products/{productid}/reviews"
    querystring = {}
    if api_key:
        querystring['api_key'] = api_key
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-amazon-data-scraper.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

