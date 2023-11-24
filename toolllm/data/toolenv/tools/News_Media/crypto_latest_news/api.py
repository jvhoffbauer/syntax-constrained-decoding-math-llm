import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def latest_crypto_news(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Find the latest cryptocurrency news, updates, values, prices, and more related to Bitcoin, Ethereum, Dogecoin, DeFi and NFTs from several newspapers and websites"
    
    """
    url = f"https://crypto-latest-news.p.rapidapi.com/cryptonews"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-latest-news.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

