import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def login(username: str, password: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Login using username and password."
    
    """
    url = f"https://instagram-unofficial.p.rapidapi.com/login"
    querystring = {'username': username, 'password': password, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-unofficial.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_igtv(query: str, session_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search IGTV."
    session_key: Use our login api to get the session_key
        
    """
    url = f"https://instagram-unofficial.p.rapidapi.com/search-igtv"
    querystring = {'query': query, 'session_key': session_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-unofficial.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_tags(query: str, session_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search tags."
    session_key: Use our login api to get the session_key
        
    """
    url = f"https://instagram-unofficial.p.rapidapi.com/search-tags"
    querystring = {'query': query, 'session_key': session_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-unofficial.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_users(query: str, session_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search users."
    session_key: Use our login api to get the session_key
        
    """
    url = f"https://instagram-unofficial.p.rapidapi.com/search-users"
    querystring = {'query': query, 'session_key': session_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-unofficial.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_search(query: str, session_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Top Search (hashtags, places, users)."
    session_key: Use our login api to get the session_key
        
    """
    url = f"https://instagram-unofficial.p.rapidapi.com/search"
    querystring = {'query': query, 'session_key': session_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-unofficial.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_a_tag(tag: str, session_key: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a tag."
    
    """
    url = f"https://instagram-unofficial.p.rapidapi.com/get-tag"
    querystring = {'tag': tag, }
    if session_key:
        querystring['session_key'] = session_key
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-unofficial.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def unlike_a_post(media_id: str, session_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Unlike a post by id."
    session_key: Use our login api to get the session_key
        
    """
    url = f"https://instagram-unofficial.p.rapidapi.com/unlike-post"
    querystring = {'media_id': media_id, 'session_key': session_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-unofficial.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

