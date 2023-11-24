import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def devices_getasingledeviceinfofromaccount(is_id: str, key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    id: ID of the device
        key: TrumpetBox Cloud API KEY
        
    """
    url = f"https://trumpetbox-cloud.p.rapidapi.com/device"
    querystring = {'id': is_id, 'key': key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "trumpetbox-cloud.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def messages_getpendingmessagesfromaccount(device: str, key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    device: ID of the specific device you want to get pending messages (Optional)


        key: TrumpetBox Cloud API KEY
        
    """
    url = f"https://trumpetbox-cloud.p.rapidapi.com/pending"
    querystring = {'device': device, 'key': key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "trumpetbox-cloud.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

