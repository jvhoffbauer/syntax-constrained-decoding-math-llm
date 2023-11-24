import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def top_paid_apps(language: str='en', region: str='us', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Top paid apps chart."
    language: The language to use, specified as a 2-letter language code - see [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
**Default**: `en`.
        region: The country code of country/region to use, specified as a 2-letter country code - see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
**Default**: `us`.
        
    """
    url = f"https://store-apps.p.rapidapi.com/top-paid-apps"
    querystring = {}
    if language:
        querystring['language'] = language
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "store-apps.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def app_details(language: str='en', region: str='us', app_id: str='com.google.android.apps.subscriptions.red', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get full app details."
    language: The language to use, specified as a 2-letter language code - see [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
**Default**: `en`.
        region: The country code of country/region to use, specified as a 2-letter country code - see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
**Default**: `us`.
        app_id: App Id. Batching of up to 100 App Ids is supported by separating multiple ids by comma (e.g. com.snapchat.android,com.microsoft.teams).
        
    """
    url = f"https://store-apps.p.rapidapi.com/app-details"
    querystring = {}
    if language:
        querystring['language'] = language
    if region:
        querystring['region'] = region
    if app_id:
        querystring['app_id'] = app_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "store-apps.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(q: str, language: str='en', cursor: str=None, region: str='us', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for apps on the Store."
    q: Search query.
        language: The language to use, specified as a 2-letter language code - see [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
**Default**: `en`.
        cursor: Specify a cursor from the previous request to get the next set of results.
        region: The country code of country/region to use, specified as a 2-letter country code - see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
**Default**: `us`.
        
    """
    url = f"https://store-apps.p.rapidapi.com/search"
    querystring = {'q': q, }
    if language:
        querystring['language'] = language
    if cursor:
        querystring['cursor'] = cursor
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "store-apps.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_free_apps(region: str='us', language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Top free apps chart."
    region: The country code of country/region to use, specified as a 2-letter country code - see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
**Default**: `us`.
        language: The language to use, specified as a 2-letter language code - see [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
**Default**: `en`.
        
    """
    url = f"https://store-apps.p.rapidapi.com/top-free-apps"
    querystring = {}
    if region:
        querystring['region'] = region
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "store-apps.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_grossing_games(language: str='en', region: str='us', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Top grossing games chart."
    language: The language to use, specified as a 2-letter language code - see [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
**Default**: `en`.
        region: The country code of country/region to use, specified as a 2-letter country code - see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
**Default**: `us`.
        
    """
    url = f"https://store-apps.p.rapidapi.com/top-grossing-games"
    querystring = {}
    if language:
        querystring['language'] = language
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "store-apps.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_free_games(language: str='en', region: str='us', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Top free games chart."
    language: The language to use, specified as a 2-letter language code - see [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
**Default**: `en`.
        region: The country code of country/region to use, specified as a 2-letter country code - see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
**Default**: `us`.
        
    """
    url = f"https://store-apps.p.rapidapi.com/top-free-games"
    querystring = {}
    if language:
        querystring['language'] = language
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "store-apps.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def app_reviews(app_id: str, limit: int=10, cursor: str=None, region: str='us', language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all app reviews."
    app_id: App Id of the app for which to get reviews.
        limit: Maximum number of reviews in the results.
        cursor: Specify a cursor from the previous request to get the next set of results.
        region: The country code of country/region to use, specified as a 2-letter country code - see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
**Default**: `us`.
        language: The language to use, specified as a 2-letter language code - see [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
**Default**: `en`.
        
    """
    url = f"https://store-apps.p.rapidapi.com/app-reviews"
    querystring = {'app_id': app_id, }
    if limit:
        querystring['limit'] = limit
    if cursor:
        querystring['cursor'] = cursor
    if region:
        querystring['region'] = region
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "store-apps.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_grossing_apps(language: str='en', region: str='us', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Top grossing apps chart."
    language: The language to use, specified as a 2-letter language code - see [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
**Default**: `en`.
        region: The country code of country/region to use, specified as a 2-letter country code - see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
**Default**: `us`.
        
    """
    url = f"https://store-apps.p.rapidapi.com/top-grossing-apps"
    querystring = {}
    if language:
        querystring['language'] = language
    if region:
        querystring['region'] = region
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "store-apps.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_paid_games(region: str='us', language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Top paid games chart."
    region: The country code of country/region to use, specified as a 2-letter country code - see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
**Default**: `us`.
        language: The language to use, specified as a 2-letter language code - see [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
**Default**: `en`.
        
    """
    url = f"https://store-apps.p.rapidapi.com/top-paid-games"
    querystring = {}
    if region:
        querystring['region'] = region
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "store-apps.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

