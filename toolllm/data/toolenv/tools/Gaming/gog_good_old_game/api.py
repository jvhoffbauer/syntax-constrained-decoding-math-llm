import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def mac_games(systems: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all game available for mac !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'systems': systems, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def linux_game(systems: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all games available for linux !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'systems': systems, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def windows_games(systems: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all games available for windows !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'systems': systems, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def strategy_games(genres: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all strategy games !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'genres': genres, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def sports_games(genres: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all sports games !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'genres': genres, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def simulation_games(genres: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all simulation games !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'genres': genres, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def shooter_games(genres: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all shooter game !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'genres': genres, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def rpg_games(genres: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all rpg games !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'genres': genres, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def racing_games(genres: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all racing games !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'genres': genres, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def adventure_game(genres: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get all adventure game !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'genres': genres, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def action_games(genres: str, folio: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get action games !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game"
    querystring = {'genres': genres, }
    if folio:
        querystring['folio'] = folio
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def page_no(no: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**there are around 701+ page and each page include 48 games !**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game/pageno/{no}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def single_game(game_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**get single game response by id which include system requirement for all  platform if it is available**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game/{game_id}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_game(sugg: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "**search like search bar**"
    
    """
    url = f"https://gog-good-old-game.p.rapidapi.com/game/search/{sugg}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "gog-good-old-game.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

