import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def cup_players(team: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the players for a team"
    team: Team name
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/players"
    querystring = {'team': team, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def teams_statistic_table(stat: str, team: str=None, mode: str=None, avg: str=None, to: str=None, is_from: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Teams table for a specified statistic"
    stat: Statistic name
        team: Team name
        mode: Set with top to get the top 5, with bottom to get the worse 5 teams (default top)
        avg: Set to true if you want average statistic value, that is the table computed as (total value statistic/played games). Default false.
        to: Match day number till which compute the table
        is_from: Match day number from which to compute the table
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/table/teamstat"
    querystring = {'stat': stat, }
    if team:
        querystring['team'] = team
    if mode:
        querystring['mode'] = mode
    if avg:
        querystring['avg'] = avg
    if to:
        querystring['to'] = to
    if is_from:
        querystring['from'] = is_from
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_events(team1: str, team2: str, matchday: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all the events for a match"
    team1: Team1 name
        team2: Team2 name
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/match/events"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def players_statistic_table(stat: str, team: str=None, player: str=None, is_from: str=None, to: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the players table for a specified statistic"
    stat: Statistic name
        team: Team name
        player: Player name
        is_from: Match day number from which compute the table
        to: Match day number till which compute the table
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/table/playerstat"
    querystring = {'stat': stat, }
    if team:
        querystring['team'] = team
    if player:
        querystring['player'] = player
    if is_from:
        querystring['from'] = is_from
    if to:
        querystring['to'] = to
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def matches_results(matchday: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all matches for a specified match day number"
    matchday: Match day number
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup"
    querystring = {'matchday': matchday, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def group_table(group: str, time: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the table for a group"
    group: Group name (ex.A)
        time: Let to compute the table considering only the first half (FH) or the second time (SH) results. Default is full time (FT).
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/table"
    querystring = {'group': group, }
    if time:
        querystring['time'] = time
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def missing_players_for_a_match(team1: str, team2: str, matchday: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the players who will miss the match and the reason"
    team1: Team1 name
        team2: Team2 name
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/match/missing"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_scorers(team: str=None, player: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns top scorers for the Cup or the number of goals scored by a player"
    team: Team name
        player: Player name
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/table/scorers"
    querystring = {}
    if team:
        querystring['team'] = team
    if player:
        querystring['player'] = player
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def lineups_and_substitutes_for_a_match(team1: str, team2: str, matchday: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns lineups, substitutes and coaches for a game (only after the game is finished)."
    team1: Team1 name
        team2: Team2 name
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/formations"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def player_stats_for_a_match(player: str, team1: str, team2: str, matchday: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the player's statistics for a match"
    player: Player name
        team1: Team1 name
        team2: Team2 name
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/match/player"
    querystring = {'player': player, 'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_statistics(team1: str, team2: str, matchday: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns statistics for a match"
    team1: Team1 name
        team2: Team2 name
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/match/stats"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_scorers(team1: str, team2: str, matchday: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns when and how the scorers scored in a match"
    team1: Team1 name
        team2: Team2 name
        matchday: Match day number for the match
        
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/scorers"
    querystring = {'team1': team1, 'team2': team2, }
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_of_teams(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the list of all the teams of the tournament"
    
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/teams"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def team_data(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns info about the team name"
    
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/team"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def venue_data(name: str='Olimpico di Roma', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return venue data"
    
    """
    url = f"https://heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com/api/eurocup/venue"
    querystring = {}
    if name:
        querystring['name'] = name
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-euro-cup-2016-live-score-results-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

