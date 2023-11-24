import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def scrape_playstore(appid: str, country: str='us', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Scrape AppStore app listing details like descriptions, and reviews"
    appid: Enter the app ID that you want to retrieve, for example **com.twitter.android**
        country: Enter the two letter country code to search in. Default is **us**. Examples include:

- us
- ca
- gb
- de
etc
        
    """
    url = f"https://android-playstore-scraper.p.rapidapi.com/v1/playstore"
    querystring = {'appid': appid, }
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "android-playstore-scraper.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

