import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def venue(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns venue data"
    
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/venue"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def team(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns info about the team"
    
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/team"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def events_subscribed(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all the events subscribed. Not available for BASIC plan."
    
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/push/list"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/listbookmakers"
    querystring = {'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def odds_list(team2: str, team1: str, bookmaker: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the available odds for a match and a bookmaker"
    team2: Away team
        team1: Home team
        bookmaker: Bookmaker name
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/listodds"
    querystring = {'team2': team2, 'team1': team1, 'bookmaker': bookmaker, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_scorers(how: str=None, fromdate: str=None, todate: str=None, page: int=None, to: int=None, is_from: int=None, mode: str=None, player: str=None, team: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns top scorers for the league"
    how: Return only goals scored according the how parameter. Its value can be: left, right, head or any, that is the default.
        fromdate: Compute the table only with matches played fromdate (format mmddyyyy)
        todate: Compute the table only with matches played todate (format mmddyyyy)
        page: Page result to return. Default is 1 that are results from 1 to 5 (max. value is 20).
        to: Optional parameter to specify the last match number to consider to compute the result (default last match number played registered on system)
        is_from: Optional parameter to specify the first match number to use to compute the result (default 1)
        mode: Optional parameter to restrict the table compute on home or away games (default all)
        player: Optional parameter to get goals number only for the player name specified
        team: Team name
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/table/scorers"
    querystring = {}
    if how:
        querystring['how'] = how
    if fromdate:
        querystring['fromdate'] = fromdate
    if todate:
        querystring['todate'] = todate
    if page:
        querystring['page'] = page
    if to:
        querystring['to'] = to
    if is_from:
        querystring['from'] = is_from
    if mode:
        querystring['mode'] = mode
    if player:
        querystring['player'] = player
    if team:
        querystring['team'] = team
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def player_stats_for_a_match(player: str, team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the player's statistics for a match"
    player: Player name
        team1: Home team name
        team2: Away team name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/match/player"
    querystring = {'player': player, 'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def player_details(player: str, team: str, honours: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all data about a player. Available only with ULTRA and MEGA plans!"
    player: Player name
        team: Team name
        honours: Return only the honours for the player (default false)
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/playerdetails"
    querystring = {'player': player, 'team': team, }
    if honours:
        querystring['honours'] = honours
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def league_table(fromdate: str=None, todate: str=None, is_from: int=None, to: int=None, mode: str=None, time: str=None, season: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Current league table"
    fromdate: Compute the table only with matches played fromdate (format mmddyyyy)
        todate: Compute the table only with matches played todate (format mmddyyyy)
        is_from: Optional parameter to specify the first match number to use to compute the table (default 1)
        to: Optional parameter to specify the last match number to consider to compute the table (default last match number played registered on system)
        mode: Optional parameter to restrict the table compute on home or away games (default all)
        time: Let to compute the table considering only the first half (FH) or the second time (SH) results. Default is full time (FT).
        season: Season code (default 2016-17)
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/table"
    querystring = {}
    if fromdate:
        querystring['fromdate'] = fromdate
    if todate:
        querystring['todate'] = todate
    if is_from:
        querystring['from'] = is_from
    if to:
        querystring['to'] = to
    if mode:
        querystring['mode'] = mode
    if time:
        querystring['time'] = time
    if season:
        querystring['season'] = season
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
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
    team1: Home team name
        team2: Away team name
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/match/missing"
    querystring = {'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def league_players(team: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all the players for a team"
    team: Team name
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/players"
    querystring = {'team': team, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_scorers(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return who scored and how for a match"
    team1: Home team name
        team2: Away team name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/scorers"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def lineups_and_substitutes_for_a_match(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return lineups, substitutes and coaches for a game after a while the game is finished."
    team1: Home team name
        team2: Away team name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/formations"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_statistics(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return statistics for a match after a while it is finished."
    team1: Home team name
        team2: Away team name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/match/stats"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def odd_quotas(team2: str, team1: str, odd: str, bookmaker: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns quotas for an odd a match and a bookmaker"
    team2: Away team
        team1: Home team
        odd: Odd name
        bookmaker: Bokkmaker name
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/odds"
    querystring = {'team2': team2, 'team1': team1, 'odd': odd, 'bookmaker': bookmaker, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_events(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the events for a match (yellow and red cards, substitutions, shots on post and formations module)"
    team1: Home team name
        team2: Away team name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/match/events"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bet_stats(bet: str, fromdate: str=None, mode: str=None, over: int=None, team: str=None, time: str=None, todate: str=None, when: str=None, handicap: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns aggregate data about results, goal-nogoal, underover, 1x2 and totalgoals to support your bet activities"
    bet: Type of data required, result, totalgoals,underover,1x2,goalnogoal
        fromdate: Only matches fromdate (format mmddyyyy)
        mode: Together with team parameter, let you to select only games where team has played home, away or all (default)
        over: Over values limit, mandatory for underover bet
        team: Team name
        time: Let you to select only first half (FH) result, second half (SH) or full time (FT) default
        todate: Only matches todate (format mmddyyyy)
        when: Let you to select only games with win, loss, draw or all (default)
        handicap: Handicap values (only for 1x2 bet)
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1/table/betting"
    querystring = {'bet': bet, }
    if fromdate:
        querystring['fromdate'] = fromdate
    if mode:
        querystring['mode'] = mode
    if over:
        querystring['over'] = over
    if team:
        querystring['team'] = team
    if time:
        querystring['time'] = time
    if todate:
        querystring['todate'] = todate
    if when:
        querystring['when'] = when
    if handicap:
        querystring['handicap'] = handicap
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def season_matches_results(season: str=None, team1: str=None, matchday: str='1', date: str=None, team2: str=None, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns season matches results for a match day"
    season: Season code (default 2016-17)
        team1: Returns all matches with team1
        matchday: Returns all matches results for the match day specified
        date: Returns all matches for the date (format mmddyyyy)
        team2: Returns all matches with team2
        live: Returns only playing matches with live updates (default false)
        
    """
    url = f"https://heisenbug-ligue-1-live-scores-v1.p.rapidapi.com/api/ligue1"
    querystring = {}
    if season:
        querystring['season'] = season
    if team1:
        querystring['team1'] = team1
    if matchday:
        querystring['matchday'] = matchday
    if date:
        querystring['date'] = date
    if team2:
        querystring['team2'] = team2
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-ligue-1-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

