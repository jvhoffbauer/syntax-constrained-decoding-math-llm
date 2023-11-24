import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def address(cidade: str, uf: str, key: str, logradouro: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retuns the address from the state, city and street"
    cidade: City's name
        uf: Acronym of federative unit.Ex .: sp
        key: access key
        logradouro: Address you want to find
        
    """
    url = f"https://ipage_cep.p.rapidapi.com/ws/cep/v1/application/views/endereco/"
    querystring = {'cidade': cidade, 'uf': uf, 'key': key, 'logradouro': logradouro, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ipage_cep.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def zip_code(cep: str, key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the address from the entered zip code"
    cep: Brazilian zip code
        key: access key
        
    """
    url = f"https://ipage_cep.p.rapidapi.com/ws/cep/v1/application/views/cep/"
    querystring = {'cep': cep, 'key': key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ipage_cep.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

