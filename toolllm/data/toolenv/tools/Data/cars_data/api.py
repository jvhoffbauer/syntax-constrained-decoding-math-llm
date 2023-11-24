import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def getmakes(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all cars make"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/get/getMakes"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getecu(engine: str, make: str, generation: str, model: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all ECUs from a specified make,  model , generation and engine
		(You can use query parameters or body parameters example : 
		getModels/Audi 
		getModels?make=Audi
		)"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/get/getECU/{make}/{model}/{generation}/{engine}"
    querystring = {}
    if make:
        querystring['make'] = make
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getcarsbymake(make: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all cars by a specified make"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/search/getCarsByMake/{make}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getcarsbyengine(engine: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all cars by specified engine (or similar)"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/search/getCarsByEngine/{engine}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getcarsbyecu(ecu: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get cars by specified ECU (or similar)"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/search/getCarsByEcu/{ecu}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getcarsbymodel(model: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all cars by specified model"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/search/getCarsByModel/{model}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getcarlogo(make: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get car logo by its make"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/search/getCarLogo/{make}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getcardetails(make: str, ecu: str, engine: str, generation: str, model: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all car details from a specified make,  model , generation, engine and ecu
		(You can use query parameters or body parameters example : 
		getModels/Audi 
		getModels?make=Audi
		)"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/get/getCarDetails/{make}/{model}/{generation}/{engine}/{ecu}"
    querystring = {}
    if generation:
        querystring['generation'] = generation
    if engine:
        querystring['engine'] = engine
    if ecu:
        querystring['ecu'] = ecu
    if model:
        querystring['model'] = model
    if make:
        querystring['make'] = make
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getengine(make: str, generation: str, model: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all Engines from a specified make,  model and generation
		(You can use query parameters or body parameters example : 
		getModels/Audi 
		getModels?make=Audi
		)"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/get/getEngine/{make}/{model}/{generation}"
    querystring = {}
    if make:
        querystring['make'] = make
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getgeneration(model: str, make: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all generations from a specified make and  model
		(You can use query parameters or body parameters example : 
		getModels/Audi 
		getModels?make=Audi
		)"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/get/getGeneration/{make}/{model}"
    querystring = {}
    if make:
        querystring['make'] = make
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getmodels(make: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all models from a specified Make
		(You can use query parameters or body parameters example : 
		getModels/Audi 
		getModels?make=Audi
		)"
    
    """
    url = f"https://cars-data2.p.rapidapi.com/get/getModels/{make}"
    querystring = {}
    if make:
        querystring['make'] = make
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cars-data2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

