import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def ruby_versions(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Ruby Versions"
    
    """
    url = f"https://ruby-code-compiler.p.rapidapi.com/versions/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ruby-code-compiler.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

