import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def group_table(group: str, time: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the table for a group"
    group: Group code (A..K)
        time: Let to compute the table considering only the first half (FH) or the second time (SH) results. Default is full time (FT).
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/table"
    querystring = {'group': group, }
    if time:
        querystring['time'] = time
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bookmakers_list(team1: str, team2: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the list of the available bookmakers for a match"
    team1: Home team
        team2: Away team
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/listbookmakers"
    querystring = {'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_statistics(team1: str, team2: str, live: bool=None, matchday: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns statistics for a match"
    team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/match/stats"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def matches_results(live: bool=None, date: str=None, group: str='A', matchday: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all matches for a specified match day number"
    live: Returns matches and results with live updates (default false)
        date: Return matches in the date (format mmddyyyy).
        group: Group code (A..K). Mandatory for 1<=matchday<=6
        matchday: Match day number
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague"
    querystring = {}
    if live:
        querystring['live'] = live
    if date:
        querystring['date'] = date
    if group:
        querystring['group'] = group
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def player_stats_for_a_match(player: str, team1: str, team2: str, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the player's statistics for a match"
    player: Player name
        team1: Home team
        team2: Away team
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/match/player"
    querystring = {'player': player, 'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def lineups_and_substitutes_for_a_match(team1: str, team2: str, live: str=None, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns lineups, substitutes and coaches for a game (only after the game is finished)."
    team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/formations"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def missing_players_for_a_match(team1: str, team2: str, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the players who will miss the match and the reason"
    team1: Home team
        team2: Away team
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/match/missing"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def odds_list(bookmaker: str, team1: str, team2: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the available odds for a match and a bookmaker"
    bookmaker: Bookmaker name
        team1: Home team
        team2: Away team
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/listodds"
    querystring = {'bookmaker': bookmaker, 'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_scorers(team1: str, team2: str, live: bool=None, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns when and how the scorers scored in a match"
    team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/scorers"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_scorers(fromdate: str=None, todate: str=None, page: str=None, player: str=None, team: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns top scorers for the Cup or the number of goals scored by a player"
    fromdate: Compute the table only with matches played format (format mmddyyyy)
        todate: Compute the table only with matches played todate (format mmddyyyy)
        page: Page result to return. Default is 1 that are results from 1 to 5 (max. value is 20).
        player: Player name
        team: Team name
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/table/scorers"
    querystring = {}
    if fromdate:
        querystring['fromdate'] = fromdate
    if todate:
        querystring['todate'] = todate
    if page:
        querystring['page'] = page
    if player:
        querystring['player'] = player
    if team:
        querystring['team'] = team
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_events(team1: str, team2: str, live: bool=None, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all the events for a match"
    team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/match/events"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def odd_quotas(bookmaker: str, odd: str, team1: str, team2: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns quotas for an odd a match and a bookmaker"
    bookmaker: Bookmaker name
        odd: Odd name
        team1: Home team
        team2: Away team
        
    """
    url = f"https://heisenbug-europa-league-live-scores-v1.p.rapidapi.com/api/europaleague/odds"
    querystring = {'bookmaker': bookmaker, 'odd': odd, 'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-europa-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

