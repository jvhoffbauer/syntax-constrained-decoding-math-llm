import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def group_table(group: str, time: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the table for a group"
    group: Group name
        time: Let to compute the table considering only the first half (FH) or the second time (SH) results. Default is full time (FT).
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/table"
    querystring = {'group': group, }
    if time:
        querystring['time'] = time
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_scorers(player: str=None, team: str=None, is_from: int=None, fromdate: str=None, how: str=None, mode: str=None, page: str=None, to: str=None, todate: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns top scorers for the Cup or the number of goals scored by a player"
    player: Player name
        team: Team name
        is_from: Optional parameter to specify the first match number to use to compute the result (default 1)
        fromdate: Compute the table only with matches played fromdate (forma mmddyyyy)
        how: Return only goals scored according the how parameter. Its value can be: left, right, head or any, that is the default.
        mode: Optional parameter to restrict the table compute on home or away games (possible values are home, away or all, that is the default)
        page: Page result to return. Default is 1 that are results from 1 to 5 (max. value for page is 20).
        to: Optional parameter to specify the last match number to consider to compute the result (default last match number played registered on system)
        todate: Compute the table only with matches played todate (format mmddyyyy)
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/table/scorers"
    querystring = {}
    if player:
        querystring['player'] = player
    if team:
        querystring['team'] = team
    if is_from:
        querystring['from'] = is_from
    if fromdate:
        querystring['fromdate'] = fromdate
    if how:
        querystring['how'] = how
    if mode:
        querystring['mode'] = mode
    if page:
        querystring['page'] = page
    if to:
        querystring['to'] = to
    if todate:
        querystring['todate'] = todate
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def cup_players(team: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the players for a team. Not available for BASIC plan."
    team: Team name
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/players"
    querystring = {'team': team, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def teams_statistic_table(stat: str, avg: bool=None, is_from: int=None, mode: str=None, team: str=None, to: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Teams table for a specified statistic. Not available for BASIC plan."
    stat: Statistic name
        avg: Set to true if you want average statistic value, that is the table computed as (total value statistic/played games). Default false.
        is_from: Match day number from which to compute the table
        mode: Set with top to get the top 5, with bottom to get the worse 5 teams (default top)
        team: Team name
        to: Match day number till which compute the table
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/table/teamstat"
    querystring = {'stat': stat, }
    if avg:
        querystring['avg'] = avg
    if is_from:
        querystring['from'] = is_from
    if mode:
        querystring['mode'] = mode
    if team:
        querystring['team'] = team
    if to:
        querystring['to'] = to
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def events_subscribed(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the events subscribed. Not available for BASIC plan."
    
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/push/list"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def matches_result(matchday: str, group: str='A', date: str=None, live: bool=None, team1: str=None, team2: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all matches for a specified match day number."
    matchday: Match day number
        group: Group name (only for group stages)
        date: Returns all match in the date (format mmddyyyy)
        live: Returns results for playing matches (live) (default false, overwrite others parameters)
        team1: Returns all matches with team1 as home team
        team2: Returns all matches with team2 as away team
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup"
    querystring = {'matchday': matchday, }
    if group:
        querystring['group'] = group
    if date:
        querystring['date'] = date
    if live:
        querystring['live'] = live
    if team1:
        querystring['team1'] = team1
    if team2:
        querystring['team2'] = team2
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def odd_quotas(bookmaker: str, odd: str, team1: str, team2: str, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns quotas for an odd a match and a bookmaker. Not available for BASIC plan."
    bookmaker: Bookmaker name
        odd: Odd name
        team1: Home team
        team2: Away team
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/odds"
    querystring = {'bookmaker': bookmaker, 'odd': odd, 'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def lineups_and_substitutes_for_a_match(team1: str, team2: str, matchday: str=None, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns lineups, substitutes and coaches for a game (only after the game is finished). Not available for BASIC plan."
    team1: Home team
        team2: Away team
        matchday: Match day number for the match
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/formations"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def odds_list(team1: str, team2: str, bookmaker: str, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the available odds for a match and a bookmaker. Not available for BASIC plan."
    team1: Home team
        team2: Away team
        bookmaker: Bookmaker name
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/listodds"
    querystring = {'team1': team1, 'team2': team2, 'bookmaker': bookmaker, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_statistics(team1: str, team2: str, matchday: int=None, live: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns statistics for a match. Not available for BASIC plan."
    team1: Home team
        team2: Away team
        matchday: Match day number for the match
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/match/stats"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def missing_players_for_a_match(team1: str, team2: str, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the players who will miss the match and the reason. Not available for BASIC plan."
    team1: Home team
        team2: Away team
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/match/missing"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bookmakers_list(team1: str, team2: str, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the list of the available bookmakers for a match. Not available for BASIC plan."
    team1: Home team
        team2: Away team
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/listbookmakers"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def players_statistic_table(stat: str, player: str=None, team: str=None, is_from: int=None, to: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the players table for a specified statistic. Not available for BASIC plan."
    stat: Statistic name
        player: Player name
        team: Team name
        is_from: Match day number from which compute the table
        to: Match day number till which compute the table
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/table/playerstat"
    querystring = {'stat': stat, }
    if player:
        querystring['player'] = player
    if team:
        querystring['team'] = team
    if is_from:
        querystring['from'] = is_from
    if to:
        querystring['to'] = to
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def player_stats_for_a_match(player: str, team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the player's statistics for a match. Not available for BASIC plan."
    player: Player name
        team1: Home team name
        team2: Away team name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/match/player"
    querystring = {'player': player, 'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_events(team1: str, team2: str, matchday: int=None, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all the events for a match. Not available for BASIC plan."
    team1: Home team
        team2: Away team
        matchday: Match day number for the match
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/match/events"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_scorers(team1: str, team2: str, live: bool=None, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns when and how the scorers scored in a match. Not available for BASIC plan."
    team1: Home team
        team2: Away team
        live: Returns data for a playing match (default false)
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com/api/worldcup/scorers"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-world-cup-2018-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

