import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def posts_previousreleasess(sort: str='vote_average', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Sort the results by IMDB rating/date released
		Query parameters:
		Sorting: sort = date_released/vote_average
		
		These parameters can be applied to all requests"
    
    """
    url = f"https://ott-release-updates.p.rapidapi.com/posts/previousreleasess"
    querystring = {}
    if sort:
        querystring['sort'] = sort
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ott-release-updates.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def posts_633c599d546dda989d90b2ff(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get speicifc movie information by Movie Id"
    
    """
    url = f"https://ott-release-updates.p.rapidapi.com/posts/633c599d546dda989d90b2ff"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ott-release-updates.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def posts_nextweeks(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all Movies Which are going to stream in the coming weeks
		in all major OTT platform"
    
    """
    url = f"https://ott-release-updates.p.rapidapi.com/posts/nextweeks"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ott-release-updates.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def posts_search(moviename: str='bi', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search from the movie list by movie name / some characters in the movie name
		Query parameters:
		Search: movieName = 'bim'"
    
    """
    url = f"https://ott-release-updates.p.rapidapi.com/posts/search"
    querystring = {}
    if moviename:
        querystring['movieName'] = moviename
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ott-release-updates.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def posts(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all Movies"
    
    """
    url = f"https://ott-release-updates.p.rapidapi.com/posts"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ott-release-updates.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def posts_previousreleases(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all Movies Which are streaming currently in all major OTT platform"
    
    """
    url = f"https://ott-release-updates.p.rapidapi.com/posts/previousreleases"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ott-release-updates.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

