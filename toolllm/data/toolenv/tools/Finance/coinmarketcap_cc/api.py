import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_cryptocurrency_metadata(is_id: str, api_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all static metadata available for one or more cryptocurrencies. This information includes details like logo, description, official website URL, social links, and links to a cryptocurrency's technical documentation.
		
		One or more comma-separated CoinMarketCap cryptocurrency IDs. Example: "1,2""
    
    """
    url = f"https://coinmarketcap-cc.p.rapidapi.com/cryptocurrency/info/{is_id}"
    querystring = {'api_key': api_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "coinmarketcap-cc.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

