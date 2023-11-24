import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def tickets(count: int=2, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API endpoint to generate tickets. Pass `count` in case more than 1 tickets need to be created. Max 10 per request.
		
		Refer to example response (on the right) to see how tickets are generated. Each ticket has `3` rows and `9` columns. Empty columns are returns with an `X` and non-empty columns contain the number."
    
    """
    url = f"https://tambola-fun.p.rapidapi.com/tickets"
    querystring = {}
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tambola-fun.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

