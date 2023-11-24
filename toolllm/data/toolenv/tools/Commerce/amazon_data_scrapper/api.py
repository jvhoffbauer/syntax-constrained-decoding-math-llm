import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_amazon_product_details(productid: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get the details of an amazon product by providing the product id which we can get from the amazon website."
    apikey: you can get this at : [https://www.scraperapi.com/](url)
        
    """
    url = f"https://amazon-data-scrapper5.p.rapidapi.com/product/{productid}"
    querystring = {'apiKey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "amazon-data-scrapper5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_amazon_search_results(searchquery: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "it gives us search results of a given search query on Amazon."
    apikey: you can get this at : [https://www.scraperapi.com/](url)
        
    """
    url = f"https://amazon-data-scrapper5.p.rapidapi.com/search/{searchquery}"
    querystring = {'apiKey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "amazon-data-scrapper5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_amazon_bestsellers(bestsellersquery: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "it gives results of amazon best sellers based on the given best sellers query."
    apikey: you can get this at:[https://www.scraperapi.com/](url)
        
    """
    url = f"https://amazon-data-scrapper5.p.rapidapi.com/bestsellers/{bestsellersquery}"
    querystring = {'apiKey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "amazon-data-scrapper5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_amazon_product_reviews(productid: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "it gives data regarding customers ratings and reviews for the particular product we want taking input of productId."
    apikey: you can get this at : [https://www.scraperapi.com/](url)
        
    """
    url = f"https://amazon-data-scrapper5.p.rapidapi.com/product/{productid}/reviews"
    querystring = {'apiKey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "amazon-data-scrapper5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

