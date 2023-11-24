import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def player_details(player: str, team: str, honours: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all data about a player. Available only with ULTRA and MEGA plans!"
    player: Player name
        team: Team name
        honours: Return only the honours for the player (default false)
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/playerdetails"
    querystring = {'player': player, 'team': team, }
    if honours:
        querystring['honours'] = honours
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def player_stats_for_a_match(player: str, team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the player's statistics for a match"
    player: Player name
        team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/match/player"
    querystring = {'player': player, 'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def missing_players_for_a_match(team1: str, team2: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns missing players for a match"
    team1: Home team
        team2: Away team
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/match/missing"
    querystring = {'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_events(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the events for a match (yellow and red cards, substitutions, shots on post and formations module)"
    team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/match/events"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def season_matches_results(team1: str=None, team2: str=None, date: str=None, matchday: int=1, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns season matches results"
    team1: Returns all matches with team1
        team2: Return all matches with team2
        date: Returns all matches for the date (format mmddyyyy)
        matchday: Returns all the game for the match day specified [1-34]
        live: Returns only playing matches with live updates (default false)
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos"
    querystring = {}
    if team1:
        querystring['team1'] = team1
    if team2:
        querystring['team2'] = team2
    if date:
        querystring['date'] = date
    if matchday:
        querystring['matchday'] = matchday
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_scorers(how: str=None, page: int=None, is_from: int=None, mode: str=None, player: str=None, team: str=None, to: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns top scorers for the league"
    how: Return only goals scored according the how parameter. Its value can be: left, right, head or any, that is the default.
        page: Page result to return. Default is 1 that are results from 1 to 5 (max. value is 20).
        is_from: Optional parameter to specify the first match number to use to compute the result (default 1)
        mode: Optional parameter to restrict the table compute on home or away games (default all)
        player: Optional parameter to get goals number only for the player name specified
        team: Team name
        to: Optional parameter to specify the last match number to consider to compute the result (default last match number played registered on system)
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/table/scorers"
    querystring = {}
    if how:
        querystring['how'] = how
    if page:
        querystring['page'] = page
    if is_from:
        querystring['from'] = is_from
    if mode:
        querystring['mode'] = mode
    if player:
        querystring['player'] = player
    if team:
        querystring['team'] = team
    if to:
        querystring['to'] = to
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_scorers(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns who scored and how for a match"
    team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/scorers"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def league_players(team: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all player for a team"
    team: Team name
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/players"
    querystring = {'team': team, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def lineups_and_substitutes_for_a_game(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns lineups, substitutes and coaches for a game after a while the game is finished."
    team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/formations"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def league_table(is_from: int=None, mode: str=None, time: str=None, to: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the table for the league"
    is_from: Optional parameter to specify the first match number to use to compute the table (default 1)
        mode: Optional parameter to restrict the table compute on home or away games (default all)
        time: Let to compute the table considering only the first half (FH) or the second time (SH) results. Default is full time (FT).
        to: Optional parameter to specify the last match number to consider to compute the table (default last match number played registered on system)
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/table"
    querystring = {}
    if is_from:
        querystring['from'] = is_from
    if mode:
        querystring['mode'] = mode
    if time:
        querystring['time'] = time
    if to:
        querystring['to'] = to
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_statistics(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns match statistics"
    team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-liga-nos-live-scores-v1.p.rapidapi.com/api/liganos/match/stats"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-liga-nos-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

