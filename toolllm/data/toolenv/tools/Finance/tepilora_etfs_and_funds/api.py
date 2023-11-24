import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_security_description(isinorfundname: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "It allows to get a very detailed description for a selected Fund or ETF. You must provide IsinCode or FundName. A full matching name or isin code is required"
    
    """
    url = f"https://tepilora-etfs-and-funds.p.rapidapi.com/D/{isinorfundname}/Json"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tepilora-etfs-and-funds.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

