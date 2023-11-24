import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def download(is_id: str, version: str, type: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Download an extension"
    type: Either ZIP or CRX
        
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/download"
    querystring = {'id': is_id, 'version': version, 'type': type, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ranking_extensions(namespace: str, page: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return a list of extensions, sorted by their ranking in the given namespace.
		
		A namespace can be the overall-rank, or the type of item in Chrome Web Store (extension, app, or theme), or a category."
    namespace: Should be one of the namespaces in /api/metastats
        page: Page number (starting from 0)
        
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/ranking"
    querystring = {'namespace': namespace, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ranking_publishers(namespace: str, page: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the list of publishers in a given namespace. Namespace should be one of the fields in Metastats - Publishers API response."
    namespace: Should be the inform of \"authors-*<key>*-rank\" where *<key>* is obtained from the /api/authors-metastats API response
        page: Page number (starting from 0)
        
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/authors-ranking"
    querystring = {'namespace': namespace, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def metastats_publishers(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve overall stats about Chrome extension publishers in Chrome Web Store"
    
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/authors-metastats"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_versions(is_id: str='bmnlcjabgnpnenekpadlanbbkooimhnj', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a list of downloadable versions for an extension"
    
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/list-versions"
    querystring = {}
    if is_id:
        querystring['id'] = is_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def manifest(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the Chrome manifest file"
    
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/manifest"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(q: str, page: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Chrome extensions by name or ID"
    
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/search"
    querystring = {'q': q, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def detail(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve details of a Chrome extension"
    
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/detail"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def trends(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get historical data trends"
    
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/trends"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def reviews(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve user reviews"
    
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/reviews"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def metastats_extensions(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the overall extension stats in Chrome Web Store"
    
    """
    url = f"https://chrome-stats.p.rapidapi.com/api/metastats"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrome-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

