import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def flask_app(text: str, is_from: str, to: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "flask application"
    
    """
    url = f"https://flask11.p.rapidapi.com/nlp-translation.p.rapidapi.com/v1/translate"
    querystring = {'text': text, 'from': is_from, 'to': to, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "flask11.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

