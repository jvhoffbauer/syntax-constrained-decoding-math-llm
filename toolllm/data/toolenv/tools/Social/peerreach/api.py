import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def user_lookup(screen_name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a detailed overview of available PeerReach data for the user"
    screen_name: Twitter handle
        
    """
    url = f"https://peerreach.p.rapidapi.com/user/lookup.json"
    querystring = {'screen_name': screen_name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "peerreach.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

