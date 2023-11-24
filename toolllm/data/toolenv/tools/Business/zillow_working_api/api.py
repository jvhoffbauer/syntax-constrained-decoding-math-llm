import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def by_zillow_url(url: str='https://www.zillow.com/homes/3071%20IMPERIAL%20ST%20JACKSONVILLE,%20FL-%2032254/44466838_zpid/', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "put any property url from zillow: 
		ex. https://www.zillow.com/homes/3071%20IMPERIAL%20ST%20JACKSONVILLE,%20FL-%2032254/44466838_zpid/"
    
    """
    url = f"https://zillow-working-api.p.rapidapi.com/byurl"
    querystring = {}
    if url:
        querystring['url'] = url
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-working-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def by_property_address(propertyaddress: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "(More Advanced) The API will find it's ZPID at backend then get you the property details."
    
    """
    url = f"https://zillow-working-api.p.rapidapi.com/byaddress"
    querystring = {'propertyaddress': propertyaddress, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-working-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def by_zpid(zpid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Property Details By ZPID( you can see the zpid in the zillow url)"
    
    """
    url = f"https://zillow-working-api.p.rapidapi.com/byzpid"
    querystring = {'zpid': zpid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-working-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

