import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def string_comparison_algorithm_get(string2: str, string1: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "String Comparison Algorithm
		Send params as string1 and string2"
    
    """
    url = f"https://string-similarity-comparison.p.rapidapi.com/comparison"
    querystring = {'string2': string2, 'string1': string1, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "string-similarity-comparison.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

