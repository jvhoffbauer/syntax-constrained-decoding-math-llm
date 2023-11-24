import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def options(ticker: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Stock and Options Data"
    ticker: A ticker for U.S. Trading Stocks and ETF
        
    """
    url = f"https://stock-and-options-trading-data-provider.p.rapidapi.com/options/{ticker}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "stock-and-options-trading-data-provider.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def straddle(ticker: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Straddle Format"
    ticker: Ticker for Intel Stock
        
    """
    url = f"https://stock-and-options-trading-data-provider.p.rapidapi.com/straddle/{ticker}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "stock-and-options-trading-data-provider.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

