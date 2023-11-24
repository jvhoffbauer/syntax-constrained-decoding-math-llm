import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def team(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns info about the team"
    name: Team name
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/team"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def venue(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns venue data"
    
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/venue"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def players_statistic_table(stat: str, is_from: int=None, player: str=None, team: str=None, to: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the players table for a specified statistic. Not available for BASIC plan."
    stat: Statistic name
        is_from: Match day number from which compute the table
        player: Player name
        team: Team name
        to: Match day number till which compute the table
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/table/playerstat"
    querystring = {'stat': stat, }
    if is_from:
        querystring['from'] = is_from
    if player:
        querystring['player'] = player
    if team:
        querystring['team'] = team
    if to:
        querystring['to'] = to
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def teams_statistic_table(stat: str, avg: str=None, frmo: int=None, mode: str=None, team: str=None, to: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Teams table for a specified statistic. Not available for BASIC plan."
    stat: Statistic name
        avg: Set to true if you want average statistic value, that is the table computed as (total value statistic/played games). Default false.
        frmo: Match day number from which to compute the table
        mode: Set with top to get the top 5, with bottom to get the worse 5 teams (default top)
        team: Team name
        to: Match day number till which compute the table
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/table/teamstat"
    querystring = {'stat': stat, }
    if avg:
        querystring['avg'] = avg
    if frmo:
        querystring['frmo'] = frmo
    if mode:
        querystring['mode'] = mode
    if team:
        querystring['team'] = team
    if to:
        querystring['to'] = to
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def referees_statistics(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Referees statistics"
    
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/table/referee"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/playerdetails"
    querystring = {'player': player, 'team': team, }
    if honours:
        querystring['honours'] = honours
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def season_matches_results(team1: str=None, team2: str=None, live: bool=None, date: str=None, matchday: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns season matches results"
    team1: Returns all matches with team1
        team2: Returns all matches with team2
        live: Return only playing matches with live updates (default false)
        date: Returns all matches for the date (format mmddyyyy)
        matchday: Returns all the game for the match day specified
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a"
    querystring = {}
    if team1:
        querystring['team1'] = team1
    if team2:
        querystring['team2'] = team2
    if live:
        querystring['live'] = live
    if date:
        querystring['date'] = date
    if matchday:
        querystring['matchday'] = matchday
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/listodds"
    querystring = {'bookmaker': bookmaker, 'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def league_table(fromdate: str=None, todate: str=None, mode: str=None, time: str=None, is_from: str=None, to: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the table for the league"
    fromdate: Compute the table only with matches played fromdate (format mmddyyyy)
        todate: Compute the table only with matches played fromdate (format mmddyyyy)
        mode: Optional parameter to restrict the table compute on home or away games (default all)
        time: Let to compute the table considering only the first half (FH) or the second time (SH) results. Default is full time (FT).
        is_from: Optional parameter to specify the first match number to use to compute the table (default 1)
        to: Optional parameter to specify the last match number to consider to compute the table (default last match number played registered on system)
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/table"
    querystring = {}
    if fromdate:
        querystring['fromdate'] = fromdate
    if todate:
        querystring['todate'] = todate
    if mode:
        querystring['mode'] = mode
    if time:
        querystring['time'] = time
    if is_from:
        querystring['from'] = is_from
    if to:
        querystring['to'] = to
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/match/stats"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/match/player"
    querystring = {'player': player, 'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/formations"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
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
        bookmaker: Bookmaker name
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/odds"
    querystring = {'team2': team2, 'team1': team1, 'odd': odd, 'bookmaker': bookmaker, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/match/missing"
    querystring = {'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/match/events"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bet_stats(bet: str, fromdate: str=None, handicap: int=None, mode: str=None, over: int=None, team: str=None, time: str=None, todate: str=None, when: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns aggregate data about results, goal-nogoal, underover, 1x2 and totalgoals to support your bet activities"
    bet: Type of data required, result, totalgoals,underover,1x2,goalnogoal
        fromdate: Only matches fromdate (format mmddyyyy)
        handicap: Handicap values (only for 1x2 bet)
        mode: Together with team parameter, let you to select only games where team has played home, away or all (default)
        over: Over values limit, mandatory for underover bet
        team: Team name
        time: Let you to select only first half (FH) result, second half (SH) or full time (FT) default
        todate: Only matches todate (format mmddyyyy)
        when: Let you to select only games with win, loss, draw or all (default)
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/table/betting"
    querystring = {'bet': bet, }
    if fromdate:
        querystring['fromdate'] = fromdate
    if handicap:
        querystring['handicap'] = handicap
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
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/scorers"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bookmakers_list(team2: str, team1: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the list of the available bookmakers for a match"
    team2: Away team
        team1: Home team
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/listbookmakers"
    querystring = {'team2': team2, 'team1': team1, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def league_players(team: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return all players for a team"
    team: Team name
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/players"
    querystring = {'team': team, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_scorers(how: str=None, fromdate: str=None, todate: str=None, page: int=None, is_from: str=None, mode: str=None, player: str=None, team: str=None, to: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns top scorers for the league"
    how: Return only goals scored according the how parameter. Its value can be: left, right, head or any, that is the default.
        fromdate: Compute the table only with matches played fromdate (format mmddyyyy)
        todate: Compute the table only with matches played todate (format mmddyyyy)
        page: Page result to return. Default is 1 that are results from 1 to 5 (max. value is 20).
        is_from: Optional parameter to specify the first match number to use to compute the result (default 1)
        mode: Optional parameter to restrict the table compute on home or away games (default all)
        player: Optional parameter to get goals number only for the player name specified
        team: Team name
        to: Optional parameter to specify the last match number to consider to compute the result (default last match number played registered on system)
        
    """
    url = f"https://heisenbug-seriea-live-scores-v1.p.rapidapi.com/api/serie-a/table/scorers"
    querystring = {}
    if how:
        querystring['how'] = how
    if fromdate:
        querystring['fromdate'] = fromdate
    if todate:
        querystring['todate'] = todate
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
            "X-RapidAPI-Host": "heisenbug-seriea-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

