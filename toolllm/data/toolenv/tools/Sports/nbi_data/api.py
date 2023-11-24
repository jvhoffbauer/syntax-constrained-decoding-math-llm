import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_game(seasons: str='[2020]', end_date: str='2022-01-01', postseason: bool=None, limit: int=25, start_date: str='2020-01-01', page: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Game Data"
    seasons: An array of year.  i.e. putting 2019 will return all games that are in season 2019-2020.
        end_date: Should be in `YYYY-MM-DD` format. Will query all games that occur on or before this date.
        postseason: Will return all games the occur in postseason
        start_date: Should be in `YYYY-MM-DD` format. Will query all games that occur on or after this date.
        
    """
    url = f"https://nbi-data.p.rapidapi.com/game"
    querystring = {}
    if seasons:
        querystring['seasons'] = seasons
    if end_date:
        querystring['end_date'] = end_date
    if postseason:
        querystring['postseason'] = postseason
    if limit:
        querystring['limit'] = limit
    if start_date:
        querystring['start_date'] = start_date
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nbi-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_season_average(season: int=2019, players: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Season Average"
    season: The season year. i.e. putting 2019, will return the data of season 2019-2020.
        players: Array of player ids. The player ids can be retrieve from /player api.
        
    """
    url = f"https://nbi-data.p.rapidapi.com/average"
    querystring = {}
    if season:
        querystring['season'] = season
    if players:
        querystring['players'] = players
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nbi-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_stats(page: int=1, postseason: bool=None, games: str=None, limit: int=25, players: str=None, end_date: str=None, start_date: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Game Stats or Player Stats"
    page: The current page, used in navigating thru the list.
        postseason: Retrieve the stats in postseason
        games: Array of game ids. The game ids can be retrieve from /game api.
        limit: The maximum of items to return per page, a max of 100
        players: Array of player ids. The player ids can be retrieve from /player api.
        end_date: Should be in `YYYY-MM-DD` format. This is used to retrieve data the occur on or before this date.
        start_date: Should be in `YYYY-MM-DD` format. This is used to retrieve data the occur on or after this date.
        
    """
    url = f"https://nbi-data.p.rapidapi.com/stat"
    querystring = {}
    if page:
        querystring['page'] = page
    if postseason:
        querystring['postseason'] = postseason
    if games:
        querystring['games'] = games
    if limit:
        querystring['limit'] = limit
    if players:
        querystring['players'] = players
    if end_date:
        querystring['end_date'] = end_date
    if start_date:
        querystring['start_date'] = start_date
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nbi-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_specific_team(page: int=1, q: str='Golden State Warriors', limit: int=25, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the specific team data"
    page: The current page, used for navigating thru the list
        q: The team name. Can be a keyword. i.e. Golden (will return all teams with `golden` in their name)
        limit: The maximum of items to return per page, a max of 100
        
    """
    url = f"https://nbi-data.p.rapidapi.com/team/search"
    querystring = {}
    if page:
        querystring['page'] = page
    if q:
        querystring['q'] = q
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nbi-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_teams(page: int=1, limit: int=25, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all the teams"
    page: The current page, used for navigating thru the list
        limit: The maximum of items to return per page, a max of 100
        
    """
    url = f"https://nbi-data.p.rapidapi.com/team"
    querystring = {}
    if page:
        querystring['page'] = page
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nbi-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_player(q: str='Stephen Curry', page: int=1, limit: int=25, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get player data"
    q: The player name to search. OPTIONAL. Leave blank to get all players.
        page: The current page, used for navigating thru the list.
        limit: The maximum of items to return per page, a maximum of 100
        
    """
    url = f"https://nbi-data.p.rapidapi.com/player"
    querystring = {}
    if q:
        querystring['q'] = q
    if page:
        querystring['page'] = page
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "nbi-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

