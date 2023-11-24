import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def listing_detail(countrycode: str, asin: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get product detail based on an ASIN."
    
    """
    url = f"https://datamz.p.rapidapi.com/{countrycode}/product/{asin}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "datamz.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_results(countrycode: str, keyword: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get products informations matching a search.
		Results are ordered like they are in the real page."
    
    """
    url = f"https://datamz.p.rapidapi.com/{countrycode}/keywords/{keyword}/results"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "datamz.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_keyword_ranking(countrycode: str, keyword: str, asin: str, page: int=2, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Provide a keyword and a list of ASIN and get the ranking of each one.
		The results includes ranking type (sponsored or organic) and came from the specified country and page."
    countrycode: Amazon marketplace country code.
Available countries are:

    US : United State
    CA : Canada
    MX : Mexico
    BR : Brazil
    DE : Germany
    UK or GB : United Kingdom
    FR : France
    IT : Italy
    ES : Spain
    NL : Netherlands
    IN : India
    AE : United Arab Emirates
    TR : Turkey
    EG : Egypt
    SE : Sweden
    PL : Poland
    SA : Saudi Arabia
    SG : Singapore
    JP : Japan
    AU : Australia
        keyword: The keywords you want to check.
Can contain multiple words.
Eg. \"rubber yoga mat\"
        
    """
    url = f"https://datamz.p.rapidapi.com/{countrycode}/keywords/{keyword}/ranking"
    querystring = {'asin': asin, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "datamz.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

