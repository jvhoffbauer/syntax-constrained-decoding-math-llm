import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def game(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the game details for the given game id."
    id: Game id String
        
    """
    url = f"https://chess.p.rapidapi.com/game"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chess.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(yearop: str='=', year: str=None, result: str=None, player1_color: str=None, player1_name: str=None, player2_name: str=None, player2_color: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search the chess.gallery game database."
    yearop: "=" or ">=" or "<=". Used as the operator while filtering based on year
        year: Year value to search for.
        result: Get the games with this result. e.g. 1-0 for white win, 0-1 for black win 1/2-1/2 for a draw
        player1_color: The color of the piece the first player is playing.  black or white
        player1_name: Name of the first player
        player2_name: Name of the second player.
        player2_color: The color of the piece the second player is playing. black or white
        
    """
    url = f"https://chess.p.rapidapi.com/search"
    querystring = {}
    if yearop:
        querystring['yearop'] = yearop
    if year:
        querystring['year'] = year
    if result:
        querystring['result'] = result
    if player1_color:
        querystring['player1_color'] = player1_color
    if player1_name:
        querystring['player1_name'] = player1_name
    if player2_name:
        querystring['player2_name'] = player2_name
    if player2_color:
        querystring['player2_color'] = player2_color
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chess.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def random(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a random game from the chess.gallery database."
    
    """
    url = f"https://chess.p.rapidapi.com/random"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chess.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def player_search(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search player names"
    name: Name of the player. Partial names are allowed.
        
    """
    url = f"https://chess.p.rapidapi.com/player/search"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chess.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def pgn(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the PGN (Portable Game Notation) for the given game id."
    id: Game id string
        
    """
    url = f"https://chess.p.rapidapi.com/pgn"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chess.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

