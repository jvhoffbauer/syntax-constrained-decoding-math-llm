import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_a_provider(is_id: str, secret_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data for a single Provider record"
    
    """
    url = f"https://onepost1.p.rapidapi.com/api/v1/providers/{is_id}"
    querystring = {'secret_key': secret_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "onepost1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_a_social_post(is_id: str, secret_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data for a single SocialPost owned by the API user"
    
    """
    url = f"https://onepost1.p.rapidapi.com/api/v1/social_posts/{is_id}"
    querystring = {'secret_key': secret_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "onepost1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_an_authorized_page(is_id: str, secret_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Gets data for a single AuthorizedPage record"
    
    """
    url = f"https://onepost1.p.rapidapi.com/api/v1/authorized_pages/{is_id}"
    querystring = {'secret_key': secret_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "onepost1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_an_event(is_id: str, secret_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return data for a single Event record owned by the API user"
    
    """
    url = f"https://onepost1.p.rapidapi.com/api/v1/events/{is_id}"
    querystring = {'secret_key': secret_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "onepost1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_an_image(is_id: str, secret_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get data for a single Image record"
    
    """
    url = f"https://onepost1.p.rapidapi.com/api/v1/images/{is_id}"
    querystring = {'secret_key': secret_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "onepost1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

