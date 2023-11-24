import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def unscramble(l: str, l2: str='spa', length: str='7', containing: str='pop', letters: str='populars', starting: str='p', all: str='po', ending: str='r', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Various word games"
    
    """
    url = f"https://words36.p.rapidapi.com/unscrambler-api.php"
    querystring = {'l': l, }
    if l2:
        querystring['l2'] = l2
    if length:
        querystring['length'] = length
    if containing:
        querystring['containing'] = containing
    if letters:
        querystring['letters'] = letters
    if starting:
        querystring['starting'] = starting
    if all:
        querystring['all'] = all
    if ending:
        querystring['ending'] = ending
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "words36.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

