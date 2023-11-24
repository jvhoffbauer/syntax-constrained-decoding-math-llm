import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def step01_epcorps(zip_cd: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get energy power company list."
    zip_cd: your living place zip code. ex) 1000001
        
    """
    url = f"https://enegaeruapi-pv-v3.p.rapidapi.com/epcorps"
    querystring = {'zip_cd': zip_cd, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "enegaeruapi-pv-v3.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def step02_eplans(epcorp_cd: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get energy power company's plan list."
    epcorp_cd: epcorp_cd value you can get after calling /epcorps. ex) 4
        
    """
    url = f"https://enegaeruapi-pv-v3.p.rapidapi.com/eplans"
    querystring = {'epcorp_cd': epcorp_cd, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "enegaeruapi-pv-v3.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def step06_cells(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "check existing storage batteries information."
    
    """
    url = f"https://enegaeruapi-pv-v3.p.rapidapi.com/cells"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "enegaeruapi-pv-v3.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def step9_calcprogress(family_id: int, process_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "check the status of energy usage optimizing simulation."
    family_id: family_id value that you can get after calling /family ex) 1234567890
        process_id: process_id value that you can get after calling /pvloadcalc. ex) "a35b1b11569e7e340a4350c6aeb42573"
        
    """
    url = f"https://enegaeruapi-pv-v3.p.rapidapi.com/calcprogress"
    querystring = {'family_id': family_id, 'process_id': process_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "enegaeruapi-pv-v3.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def step10_pvcalcsmplrpt(calc_date: str, family_id: int, process_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get energy usage optimizing simulation result."
    calc_date: calc_date value when you executed YYYY-MM-DD date. ex) 2018-01-01
        family_id: family_id value that you can get after calling /family ex) 1234567890
        process_id: process_id value that you can get after calling /pvloadcalc. ex) "a35b1b11569e7e340a4350c6aeb42573"
        
    """
    url = f"https://enegaeruapi-pv-v3.p.rapidapi.com/pvcalcsmplrpt"
    querystring = {'calc_date': calc_date, 'family_id': family_id, 'process_id': process_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "enegaeruapi-pv-v3.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

