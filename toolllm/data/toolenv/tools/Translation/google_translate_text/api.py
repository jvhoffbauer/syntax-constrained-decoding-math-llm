import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def translatetext(tolanguage: str, text: str, fromlanguage: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Enter the text to be translated."
    tolanguage: Enter the language you want to translate the text to. (Use the language codes in About/Read Me)
        text: Enter the text to be translated
        fromlanguage: Enter the original language of text. (Use the language codes in About/Read Me)
        
    """
    url = f"https://google-translate-text.p.rapidapi.com/"
    querystring = {'toLanguage': tolanguage, 'text': text, 'fromLanguage': fromlanguage, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "google-translate-text.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

