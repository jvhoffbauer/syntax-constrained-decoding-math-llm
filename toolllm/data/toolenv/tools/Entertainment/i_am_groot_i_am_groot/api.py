import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def listen_to_groot(number: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Listen to Groot"
    number: The number of sentences you want to listen to Groot for
        
    """
    url = f"https://rapidalex-i-am-groot-v1.p.rapidapi.com/listenToGroot"
    querystring = {}
    if number:
        querystring['number'] = number
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "rapidalex-i-am-groot-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def speak_like_groot(sentence: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    ""
    sentence: The sentence you want converted to Groot Speak. If left empty, this endpoint will return a random number of sentences
        
    """
    url = f"https://rapidalex-i-am-groot-v1.p.rapidapi.com/grootSpeak"
    querystring = {}
    if sentence:
        querystring['sentence'] = sentence
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "rapidalex-i-am-groot-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

