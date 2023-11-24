import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def quotes(author: str='[]', category: str='[]', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get inspired by the words of history's greatest thinkers. Get your daily dose of motivation"
    author: Filter quotes by author
        category: Filter quotes by category
        
    """
    url = f"https://words-of-wisdom-the-famous-quotes-api2.p.rapidapi.com/quotes"
    querystring = {}
    if author:
        querystring['author'] = author
    if category:
        querystring['category'] = category
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "words-of-wisdom-the-famous-quotes-api2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def authors(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a list of authors"
    
    """
    url = f"https://words-of-wisdom-the-famous-quotes-api2.p.rapidapi.com/authors"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "words-of-wisdom-the-famous-quotes-api2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def categories(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a list of categories"
    
    """
    url = f"https://words-of-wisdom-the-famous-quotes-api2.p.rapidapi.com/categories"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "words-of-wisdom-the-famous-quotes-api2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

