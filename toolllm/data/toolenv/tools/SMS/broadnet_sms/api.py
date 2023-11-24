import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def send_sms(text: str, accesskey: str, sid: str, mno: int, type: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Message Submission"
    
    """
    url = f"https://broadnet-sms1.p.rapidapi.com/websmpp/websms"
    querystring = {'text': text, 'accesskey': accesskey, 'sid': sid, 'mno': mno, 'type': type, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "broadnet-sms1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

