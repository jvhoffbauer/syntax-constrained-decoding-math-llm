import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def ufc_fight_night_vettori_vs_cannonier_june_17_2023(limit: int=None, offset: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**UFC Fight Night: Vettori vs. Cannonier**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/June_17_2023"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_fight_night_emmett_vs_topuriar_june_24_2023(offset: int=None, limit: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**UFC Fight Night: Emmett vs. Topuria**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/June_24_2023"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_289_nunes_vs_aldana_june_10_2023(limit: int=None, offset: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**Get details to  UFC 289: Nunes vs. Aldana**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/June_10_2023"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_fight_night_holloway_vs_allen_april_15_2023(offset: int=None, limit: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**Get details to UFC Fight Night: Holloway vs. Allen**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/April_15_2023"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_fight_night_song_vs_simon_april_28_2023(limit: int=None, offset: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**Get details to UFC Fight Night: Song vs. Simon**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/April_28_2023"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_fight_night_pavlovich_vs_blaydes_april_22_2023(limit: int=None, offset: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**Get details to UFC Fight Night: Pavlovich vs. Blaydes**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/April_22_2023"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_fight_night_dern_vs_hill_may_20_2023(limit: int=None, offset: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**Get details to UFC Fight Night: Dern vs. Hill**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/May_20_2023"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_288_sterling_vs_cejudo_may_06_2023(limit: int=None, offset: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**Get details to  UFC 288: Sterling vs. Cejudo**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/May_06_2023"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_fight_night_rozenstruik_vs_almeida_may_13_2023(limit: int=None, offset: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**Get details to UFC Fight Night: Rozenstruik vs. Almeida**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/May_13_2023"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_fight_night_kara_france_vs_albazi_june_03_2023(limit: int=None, offset: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**Get details to UUFC Fight Night: Kara-France vs. Albazi**.                                                          
		 Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/June_03_2023"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_fighter_stats_by_age(age: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The search functionality provided helps you find fighter statistics and UFC/MMA history based on their age. It compares your search criteria with the fighters' information and returns a list of fighters that match all the specified criteria, including their statistics, averages, titles, wins, losses, and more."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/search"
    querystring = {'age': age, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_fighter_stats(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The search functionality provided helps you find fighter statistics and UFC/MMA history based on their names. It compares your search criteria with the fighters' information and returns a list of fighters that match all the specified criteria, including their statistics, averages, titles, wins, losses, and more."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/search"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_event_details(q: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This lets you search for specific fights by the names of the fighters involved. The response returned by the API endpoint includes details such as the date of the fight, the name of the fighters involved, and the outcome of the fight."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/search"
    querystring = {'q': q, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ufc_287_pereira_vs_adesanya_2_april_08_2023(offset: int=None, limit: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**Get details to UFC 287: Pereira vs. Adesanya 2.**.    
		  .Access a range of information about each fighter, including their win-loss record, height, weight, reach, and age. results of a particular fight or a fighter's win-loss record."
    
    """
    url = f"https://mma-stats.p.rapidapi.com/April_08_2023"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

