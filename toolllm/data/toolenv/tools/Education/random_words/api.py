import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_multiple_random_words(count: int, maxlength: int=None, endswith: str=None, wordlength: int=None, includes: str=None, beginswith: str=None, minlength: int=None, excludes: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get multiple random words (i.e. min 2 and max 20) from a list of 5500+ words
		
		Important Notes:
		1. *count* must be a valid number between 2 and 20 (both 2 and 20 included)
		2. *wordLength* must not be used with minLength and/or maxLength"
    count: The word count must be between 2 and 20
        
    """
    url = f"https://random-words5.p.rapidapi.com/getMultipleRandom"
    querystring = {'count': count, }
    if maxlength:
        querystring['maxLength'] = maxlength
    if endswith:
        querystring['endsWith'] = endswith
    if wordlength:
        querystring['wordLength'] = wordlength
    if includes:
        querystring['includes'] = includes
    if beginswith:
        querystring['beginsWith'] = beginswith
    if minlength:
        querystring['minLength'] = minlength
    if excludes:
        querystring['excludes'] = excludes
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "random-words5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_a_random_word(wordlength: int=None, excludes: str=None, beginswith: str=None, endswith: str=None, includes: str=None, maxlength: int=None, minlength: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a random words from a list of more than 5500+ words
		
		Important Note: 
		1. *wordLength* must not be used with minLength and/or maxLength"
    
    """
    url = f"https://random-words5.p.rapidapi.com/getRandom"
    querystring = {}
    if wordlength:
        querystring['wordLength'] = wordlength
    if excludes:
        querystring['excludes'] = excludes
    if beginswith:
        querystring['beginsWith'] = beginswith
    if endswith:
        querystring['endsWith'] = endswith
    if includes:
        querystring['includes'] = includes
    if maxlength:
        querystring['maxLength'] = maxlength
    if minlength:
        querystring['minLength'] = minlength
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "random-words5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

