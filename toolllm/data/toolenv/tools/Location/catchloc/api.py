import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def group_management_api_access_for_registered_group_list(api_key: str=None, cert_key: str=None, timestamp: str=None, api: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API access for group information.
		
		required parameter : api (api.common.group.get.list)"
    
    """
    url = f"https://catchloc.p.rapidapi.com/api.partner.common.php"
    querystring = {}
    if api_key:
        querystring['api_key'] = api_key
    if cert_key:
        querystring['cert_key'] = cert_key
    if timestamp:
        querystring['timestamp'] = timestamp
    if api:
        querystring['api'] = api
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "catchloc.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def group_management_api_access_for_device_s_group_list(cert_key: str=None, member_key: str=None, api: str=None, timestamp: str=None, api_key: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API access for location object's group list.
		
		required parameter : api (api.common.group.get.object.group.list)"
    
    """
    url = f"https://catchloc.p.rapidapi.com/api.partner.common.php"
    querystring = {}
    if cert_key:
        querystring['cert_key'] = cert_key
    if member_key:
        querystring['member_key'] = member_key
    if api:
        querystring['api'] = api
    if timestamp:
        querystring['timestamp'] = timestamp
    if api_key:
        querystring['api_key'] = api_key
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "catchloc.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def group_management_api_access_for_group_s_device_list(group_key: str=None, timestamp: str=None, api_key: str=None, api: str=None, cert_key: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API access for location object group's device list.
		
		required parameter : api(api.common.group.get.group.object.list)"
    
    """
    url = f"https://catchloc.p.rapidapi.com/api.partner.common.php"
    querystring = {}
    if group_key:
        querystring['group_key'] = group_key
    if timestamp:
        querystring['timestamp'] = timestamp
    if api_key:
        querystring['api_key'] = api_key
    if api:
        querystring['api'] = api
    if cert_key:
        querystring['cert_key'] = cert_key
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "catchloc.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def group_management_api_access_for_creating_group(cert_key: str=None, api_key: str=None, group_name: str=None, timestamp: str=None, api: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API access for location object's group designation and creation.
		
		required parameter : api (api.common.group.set.add)"
    
    """
    url = f"https://catchloc.p.rapidapi.com/api.partner.common.php"
    querystring = {}
    if cert_key:
        querystring['cert_key'] = cert_key
    if api_key:
        querystring['api_key'] = api_key
    if group_name:
        querystring['group_name'] = group_name
    if timestamp:
        querystring['timestamp'] = timestamp
    if api:
        querystring['api'] = api
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "catchloc.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def group_management_api_access_for_modifying_group_information(timestamp: str, api_key: str, group_name: str, api: str, cert_key: str, group_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API access to modifying location object's group information
		
		required parameter : api (api.common.group.set.modify)"
    
    """
    url = f"https://catchloc.p.rapidapi.com/api.partner.common.php"
    querystring = {'timestamp': timestamp, 'api_key': api_key, 'group_name': group_name, 'api': api, 'cert_key': cert_key, 'group_key': group_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "catchloc.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def group_management_api_access_for_removing_group_information(api: str, api_key: str, cert_key: str, group_key: str, timestamp: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API access to remove location object's group information.
		
		required parameter : api (api.common.group.set.delete)"
    
    """
    url = f"https://catchloc.p.rapidapi.com/api.partner.common.php"
    querystring = {'api': api, 'api_key': api_key, 'cert_key': cert_key, 'group_key': group_key, 'timestamp': timestamp, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "catchloc.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

