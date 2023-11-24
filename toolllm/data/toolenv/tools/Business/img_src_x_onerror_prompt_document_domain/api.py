import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def test(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "+++++++++++++++++++++++++++++++++++++++'"/>><img/onanimationstart=prompt`${document.domain}>"
    
    """
    url = f"https://img-src-x-onerror-prompt-document-domain.p.rapidapi.comhttps://provider.rapidapi.com/defenition/api_9eb5d2ac-481f-4de3-abe3-19ca0223b575/endpoints/add"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "img-src-x-onerror-prompt-document-domain.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

