import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def languages(api_version: str, scope: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Gets the set of languages currently supported by other operations of the Translator Text API."
    api_version: Version of the API requested by the client. Value must be **3.0**.
        scope: A comma-separated list of names defining the group of languages to return. Allowed group names are- `translation`, `transliteration` and `dictionary`. If no scope is given, then all groups are returned, which is equivalent to passing `scope=translation,transliteration,dictionary`. To decide which set of supported languages is appropriate for your scenario, see the description of the response object.
        
    """
    url = f"https://microsoft-translator-text.p.rapidapi.com/languages"
    querystring = {'api-version': api_version, }
    if scope:
        querystring['scope'] = scope
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

