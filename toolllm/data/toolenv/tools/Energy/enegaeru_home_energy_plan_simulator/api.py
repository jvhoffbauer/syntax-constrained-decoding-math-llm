import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def step02_eplans(epcorp_cd: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get energy power company's plan list."
    epcorp_cd: epcorp_cd value you can get after calling /epcorps. ex) 4
        
    """
    url = f"https://enegaeruapi-ep-v3.p.rapidapi.com/eplans"
    querystring = {'epcorp_cd': epcorp_cd, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "enegaeruapi-ep-v3.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def step01_epcorps(zip_cd: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get energy power company list."
    zip_cd: your living place zip code. ex) 1000001
        
    """
    url = f"https://enegaeruapi-ep-v3.p.rapidapi.com/epcorps"
    querystring = {'zip_cd': zip_cd, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "enegaeruapi-ep-v3.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def step6_calcprogress(family_id: int, process_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "check the status of energy plan simulation."
    family_id: family_id value that you can get after calling /family ex) 1234567890
        process_id: process_id value that you can get after calling /eploadcalc. ex) "a35b1b11569e7e340a4350c6aeb42573"
        
    """
    url = f"https://enegaeruapi-ep-v3.p.rapidapi.com/calcprogress"
    querystring = {'family_id': family_id, 'process_id': process_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "enegaeruapi-ep-v3.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def step07_epcalcsmplrpt(calc_date: str, process_id: str, family_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get energy plan simulation result."
    calc_date: calc_date value when you executed YYYY-MM-DD date. ex) 2018-01-01
        process_id: process_id value that you can get after calling /eploadcalc. ex) "a35b1b11569e7e340a4350c6aeb42573"
        family_id: family_id value that you can get after calling /family ex) 1234567890
        
    """
    url = f"https://enegaeruapi-ep-v3.p.rapidapi.com/epcalcsmplrpt"
    querystring = {'calc_date': calc_date, 'process_id': process_id, 'family_id': family_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "enegaeruapi-ep-v3.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

