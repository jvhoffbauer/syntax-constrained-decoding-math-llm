import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def api_data(access_token: str='access_token', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns ref to be used for future api calls"
    
    """
    url = f"https://wellbeing-express.p.rapidapi.com/api"
    querystring = {}
    if access_token:
        querystring['access_token'] = access_token
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wellbeing-express.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def base_api(ref: str, q: str, format: str, page: int, pagesize: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "All endpoints can be queried by changing the q parameter. The ref parameter value can be found by querying the api data endpoint"
    ref: This parameter is used to define the ref of the master branch, this can be found by querying the API data endpoint. All access tokens on rapidapi only have access to master branch
        q: Query for api, should be used exactly as given to get entire list of documents
        
    """
    url = f"https://wellbeing-express.p.rapidapi.com/api/v2/documents/search"
    querystring = {'ref': ref, 'q': q, 'format': format, 'page': page, 'pageSize': pagesize, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wellbeing-express.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

