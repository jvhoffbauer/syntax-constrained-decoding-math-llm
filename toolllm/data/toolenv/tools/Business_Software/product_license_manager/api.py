import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def api_license_status_generate(api: str, key: str, func: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint will show you the status of an api or license. if it is active you can pass more STRING to it like: func
		
		'func' stands for FUNCTION, it basically tells api what function user has requested to access. accessable functions are: gl,ac,st.
		gl: Generate license
		ac: Activate license
		st: Status"
    
    """
    url = f"https://product-license-manager.p.rapidapi.com/webhook"
    querystring = {'api': api, 'key': key, }
    if func:
        querystring['func'] = func
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "product-license-manager.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def activate_license_ac(lic: str, key: str, func: str, api: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This will activate the license which you generated using other endpoint, this license will be ready to use after activation.
		
		'func' stands for FUNCTION, it basically tells api what function user has requested to access. accessable functions are: gl,ac,st.
		gl: Generate license
		ac: Activate license
		st: Status
		
		'lic' stands for LICENSE, you need to givge an license which you want it to activate."
    
    """
    url = f"https://product-license-manager.p.rapidapi.com/webhook"
    querystring = {'lic': lic, 'key': key, 'func': func, 'api': api, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "product-license-manager.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

