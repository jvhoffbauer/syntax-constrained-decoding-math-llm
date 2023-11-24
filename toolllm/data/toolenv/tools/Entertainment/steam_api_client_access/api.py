import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_user_owned_game(steamid: str, steamkey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve owned game for a specific steam ID"
    
    """
    url = f"https://steam-api-client-access.p.rapidapi.com/getOwnedGames"
    querystring = {'steamId': steamid, 'steamKey': steamkey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "steam-api-client-access.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_player_achievements(appid: str, steamkey: str, steamid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all player achievements from his steam profile."
    
    """
    url = f"https://steam-api-client-access.p.rapidapi.com/getPlayerAchievements"
    querystring = {'appid': appid, 'steamKey': steamkey, 'steamId': steamid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "steam-api-client-access.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_game_information_by_app_id(appid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve a complete game information object simply by passing an app id (you can find app id with the /getOwnedGames or /getRecentlyPlayedGames endpoints of this api"
    
    """
    url = f"https://steam-api-client-access.p.rapidapi.com/gameDetails/{appid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "steam-api-client-access.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

