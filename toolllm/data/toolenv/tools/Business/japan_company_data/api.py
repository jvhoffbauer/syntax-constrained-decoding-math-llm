import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_company_patents(corporateid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API endpoint allows you to determine which patents have been filed by a Japanese company via their corporate ID"
    
    """
    url = f"https://japan-company-data.p.rapidapi.com/hojin/v1/hojin/{corporateid}/patent"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "japan-company-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_by_name(name: str, limit: int, page: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint allows you to search for a Japanese company by name, such as "間宮""
    
    """
    url = f"https://japan-company-data.p.rapidapi.com/hojin/v1/hojin"
    querystring = {'name': name, 'limit': limit, 'page': page, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "japan-company-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_by_corporate_id(corporateid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint allows you to search by Corporate ID, i.e. 4030001044808"
    
    """
    url = f"https://japan-company-data.p.rapidapi.com/hojin/v1/hojin/{corporateid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "japan-company-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

