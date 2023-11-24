import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_seasons(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Seasons"
    
    """
    url = f"https://tms5.p.rapidapi.com/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tms5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_episodes(tv_id: int, season_number: int, append_to_response: str='external_ids', api_key: str='05902896074695709d7763505bb88b4d', language: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Episodes"
    
    """
    url = f"https://tms5.p.rapidapi.com/tv/{tv_id}/season/{season_number}"
    querystring = {}
    if append_to_response:
        querystring['append_to_response'] = append_to_response
    if api_key:
        querystring['api_key'] = api_key
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tms5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def trending_movie_day(api_key: str='05902896074695709d7763505bb88b4d', language: str='en-US', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "trending movie day"
    
    """
    url = f"https://tms5.p.rapidapi.com/trending/movie/day"
    querystring = {}
    if api_key:
        querystring['api_key'] = api_key
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tms5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tv_with_ext_id(tv_id: int, api_key: str, language: str='en-US', append_to_response: str='external_ids', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Tv with ext id"
    
    """
    url = f"https://tms5.p.rapidapi.com/tv/{tv_id}"
    querystring = {'api_key': api_key, }
    if language:
        querystring['language'] = language
    if append_to_response:
        querystring['append_to_response'] = append_to_response
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tms5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_movie_ext_id(movie_id: str, language: str='en-US', append_to_response: str='external_ids', api_key: str='05902896074695709d7763505bb88b4d', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get movie ext id"
    
    """
    url = f"https://tms5.p.rapidapi.com/movie/{movie_id}"
    querystring = {}
    if language:
        querystring['language'] = language
    if append_to_response:
        querystring['append_to_response'] = append_to_response
    if api_key:
        querystring['api_key'] = api_key
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tms5.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

