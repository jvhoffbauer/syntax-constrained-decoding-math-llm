import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_data_safety_attributes_by_app_id(appid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the data safety attributes of a single application by its ID"
    appid: Application ID
        
    """
    url = f"https://google-play9.p.rapidapi.com/apps/{appid}/datasafety"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "google-play9.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_list_of_apps_with_pagination(country: str=None, collection: str=None, category: str=None, fulldetail: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a list of apps and a pagination token"
    country: Country for the Google Play
        collection: Collection for the Google Play
        category: Category for the Google Play
        fulldetail: Include full detail of the applications
        
    """
    url = f"https://google-play9.p.rapidapi.com/apps"
    querystring = {}
    if country:
        querystring['country'] = country
    if collection:
        querystring['collection'] = collection
    if category:
        querystring['category'] = category
    if fulldetail:
        querystring['fullDetail'] = fulldetail
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "google-play9.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_permissions_by_app_id(appid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the permissions of a single application by its ID"
    appid: Application ID
        
    """
    url = f"https://google-play9.p.rapidapi.com/apps/{appid}/permissions"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "google-play9.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_applications_by_developer_id(developerid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the list of applications of a single developer by its ID"
    developerid: Developer ID
        
    """
    url = f"https://google-play9.p.rapidapi.com/developers/{developerid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "google-play9.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_app_by_id(appid: str, lang: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a single application by its ID"
    appid: Application ID
        lang: Language for the application
        
    """
    url = f"https://google-play9.p.rapidapi.com/apps/{appid}"
    querystring = {}
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "google-play9.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_similar_apps_by_id(appid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns list of applications that is similar to a single application by its ID"
    appid: Application ID
        
    """
    url = f"https://google-play9.p.rapidapi.com/apps/{appid}/similar"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "google-play9.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_reviews_by_app_id(appid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the reviews of a single application by its ID"
    appid: Application ID
        
    """
    url = f"https://google-play9.p.rapidapi.com/apps/{appid}/reviews"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "google-play9.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

