import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def privacy_permissions_by_id(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get privacy permissions for an app by ID"
    
    """
    url = f"https://app-store2.p.rapidapi.com/privacy/{is_id}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def categories(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get App Store categories and their matching category codes"
    
    """
    url = f"https://app-store2.p.rapidapi.com/categories"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def similar_apps_by_id(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a list of apps similar to the provided app"
    
    """
    url = f"https://app-store2.p.rapidapi.com/similar/{is_id}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def similar_apps_by_bundle_id(appid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a list of apps similar to the provided app by app bundle ID"
    
    """
    url = f"https://app-store2.p.rapidapi.com/similar/bundle/{appid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def applications_by_developer(is_id: str, lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a list of apps published by a chosen developer"
    
    """
    url = f"https://app-store2.p.rapidapi.com/developer/{is_id}"
    querystring = {}
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(q: str, lang: str='en', country: str='us', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for apps on the App Store"
    
    """
    url = f"https://app-store2.p.rapidapi.com/search"
    querystring = {'q': q, }
    if lang:
        querystring['lang'] = lang
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def reviews_by_bundle_id(appid: str, country: str='us', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get reviews for a chosen app by app bundle id"
    
    """
    url = f"https://app-store2.p.rapidapi.com/reviews/bundle/{appid}"
    querystring = {}
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def reviews_by_id(is_id: str, country: str='us', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get reviews for a chosen app by app id"
    
    """
    url = f"https://app-store2.p.rapidapi.com/reviews/{is_id}"
    querystring = {}
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def application_details_by_bundle_id(appid: str, country: str='us', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Application information by app bundle id."
    
    """
    url = f"https://app-store2.p.rapidapi.com/app/bundle/{appid}"
    querystring = {}
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def application_details_by_id(is_id: str, country: str='us', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Application information by app id."
    
    """
    url = f"https://app-store2.p.rapidapi.com/app/{is_id}"
    querystring = {}
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def new_paid_ios_apps(category: str='6016', country: str='us', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of new paid ios apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/ios/new/paid"
    querystring = {}
    if category:
        querystring['category'] = category
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def new_free_ios_apps(category: str='6016', country: str='us', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of new free ios apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/ios/new/free"
    querystring = {}
    if category:
        querystring['category'] = category
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def new_ios_apps(country: str='us', category: str='6016', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of new ios apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/ios/new"
    querystring = {}
    if country:
        querystring['country'] = country
    if category:
        querystring['category'] = category
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_grossing_mac_apps(category: str='6016', country: str='us', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of the top grossing mac apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/mac/top/grossing"
    querystring = {}
    if category:
        querystring['category'] = category
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_grossing_ipad_apps(country: str='us', lang: str='en', category: str='6016', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of the top grossing ipad apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/ipad/top/grossing"
    querystring = {}
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    if category:
        querystring['category'] = category
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_grossing_ios_apps(country: str='us', category: str='6016', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of the top grossing ios apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/ios/top/grossing"
    querystring = {}
    if country:
        querystring['country'] = country
    if category:
        querystring['category'] = category
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_paid_mac_apps(category: str='6016', country: str='us', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of the top paid mac apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/mac/top/paid"
    querystring = {}
    if category:
        querystring['category'] = category
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_paid_ipad_apps(category: str='6016', country: str='us', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of the top paid ipad apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/ipad/top/paid"
    querystring = {}
    if category:
        querystring['category'] = category
    if country:
        querystring['country'] = country
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_paid_ios_apps(lang: str='en', category: str='6016', country: str='us', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of the top paid ios apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/ios/top/paid"
    querystring = {}
    if lang:
        querystring['lang'] = lang
    if category:
        querystring['category'] = category
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_free_mac_apps(lang: str='en', category: str='6016', country: str='us', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of the top free mac apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/mac/top/free"
    querystring = {}
    if lang:
        querystring['lang'] = lang
    if category:
        querystring['category'] = category
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_free_ipad_apps(country: str='us', category: str='6016', lang: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of the top free Ipad apps"
    
    """
    url = f"https://app-store2.p.rapidapi.com/ipad/top/free"
    querystring = {}
    if country:
        querystring['country'] = country
    if category:
        querystring['category'] = category
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_free_ios_apps(lang: str='en', country: str='us', category: str='6016', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get list of the top free apps on IOS"
    
    """
    url = f"https://app-store2.p.rapidapi.com/ios/top/free"
    querystring = {}
    if lang:
        querystring['lang'] = lang
    if country:
        querystring['country'] = country
    if category:
        querystring['category'] = category
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "app-store2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

