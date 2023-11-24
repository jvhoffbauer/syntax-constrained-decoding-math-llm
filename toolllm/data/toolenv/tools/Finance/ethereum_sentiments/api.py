import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def crypto_sentiments_ethereum_tokens(ethsentiments: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API queries Uniswap for new  tokens and are ready to gain momentum."
    
    """
    url = f"https://ethereum-sentiments.p.rapidapi.com/ethSentiments"
    querystring = {}
    if ethsentiments:
        querystring['ethSentiments'] = ethsentiments
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ethereum-sentiments.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

