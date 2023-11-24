import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def price(index: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get price of index over a period"
    
    """
    url = f"https://global-market-indices-data.p.rapidapi.com/v1/price"
    querystring = {'index': index, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-market-indices-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def forecast(index: str='DAX', symbol: str='BAYN.DE', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Predics stock price for the next ^ months"
    
    """
    url = f"https://global-market-indices-data.p.rapidapi.com/v1/forecast"
    querystring = {}
    if index:
        querystring['index'] = index
    if symbol:
        querystring['symbol'] = symbol
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-market-indices-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def change(period: str='7DAYS', symbol: str='AAPL', index: str='SPX', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the symbol change over the period of time(1DAY, 7DAYS, 1MONTH, 3MONTHS, 6MONTHS, 1YEAR )"
    
    """
    url = f"https://global-market-indices-data.p.rapidapi.com/v1/change"
    querystring = {}
    if period:
        querystring['period'] = period
    if symbol:
        querystring['symbol'] = symbol
    if index:
        querystring['index'] = index
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-market-indices-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top5(symbol: str, index: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get best/worst performers for a symbol over a period"
    
    """
    url = f"https://global-market-indices-data.p.rapidapi.com/v1/top5"
    querystring = {'symbol': symbol, 'index': index, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-market-indices-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def index(index: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get an Index constituents"
    
    """
    url = f"https://global-market-indices-data.p.rapidapi.com/v1/index"
    querystring = {'index': index, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-market-indices-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def indices(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Listed Indices"
    
    """
    url = f"https://global-market-indices-data.p.rapidapi.com/v1/indices"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "global-market-indices-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

