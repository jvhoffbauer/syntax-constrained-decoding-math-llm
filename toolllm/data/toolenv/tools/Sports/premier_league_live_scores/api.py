import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def team(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns info about the team"
    
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/team"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/venue"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/referee"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def prediction(team2: str, team1: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns match result perdiction (use an AI deep learning engine)"
    team2: Away team name (case sensitiva)
        team1: Home team name (case sensitive)
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/predict"
    querystring = {'team2': team2, 'team1': team1, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def season_matches_results(matchday: str='1', season: str=None, date: str=None, live: bool=None, team1: str=None, team2: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return season matches results for a match day"
    matchday: Return all matches results for the specified match day
        season: Season code (default 2017-18)
        date: Returns all match in the date (format mmddyyyy)
        live: Returns results for playing matches (live) (default false, overwrite others parameters)
        team1: Returns all matches with team1
        team2: Returns all matches with team2
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague"
    querystring = {}
    if matchday:
        querystring['matchday'] = matchday
    if season:
        querystring['season'] = season
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
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bookmakers_list(team1: str, team2: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the list of the available bookmakers for a match. Not available for BASIC plan."
    team1: Home team
        team2: Away team
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/listbookmakers"
    querystring = {'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_scorers(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return scorers for a match. Not available for BASIC plan."
    team1: Home team name
        team2: Away team name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/scorers"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def lineups_and_substitutes_for_a_game(team1: str, team2: str, live: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return lineups, substitutes and coaches for a game (only after the game is finished). Not available for BASIC plan."
    team1: Home team name
        team2: Away team name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/formations"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_events(team2: str, team1: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the events for a match (yellow and red cards, substitutions, shots on post and formations module). Not available for BASIC plan."
    team2: Amat team name
        team1: Home tema name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/match/events"
    querystring = {'team2': team2, 'team1': team1, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def player_stats_for_a_match(team1: str, team2: str, player: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the player's statistics for a match. Not available for BASIC plan."
    team1: Home team name
        team2: Away team name
        player: Player name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/match/player"
    querystring = {'team1': team1, 'team2': team2, 'player': player, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_scorers(todate: str=None, page: int=None, is_from: int=None, player: str=None, team: str=None, to: int=None, mode: str=None, fromdate: str=None, how: str='head', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns top scorers for the league"
    todate: Compute the table only with matches played todate (format mmddyyyy)
        page: Page result to return. Default is 1 that are results from 1 to 5 (max. value is 20).
        is_from: Optional parameter to specify the first match number to use to compute the result (default 1)
        player: Optional parameter to get goals number only for the player name specified
        team: Team name
        to: Optional parameter to specify the last match number to consider to compute the result (default last match number played registered on system)
        mode: Optional parameter to restrict the table compute on home or away games (possible values are home, away or all, that is the default)
        fromdate: Compute the table only with matches played fromdate (forma mmddyyyy)
        how: Return only goals scored according the how parameter. Its value can be: left, right, head or any, that is the default.
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/scorers"
    querystring = {}
    if todate:
        querystring['todate'] = todate
    if page:
        querystring['page'] = page
    if is_from:
        querystring['from'] = is_from
    if player:
        querystring['player'] = player
    if team:
        querystring['team'] = team
    if to:
        querystring['to'] = to
    if mode:
        querystring['mode'] = mode
    if fromdate:
        querystring['fromdate'] = fromdate
    if how:
        querystring['how'] = how
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def match_statistics(team1: str, team2: str, live: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return statistics for a match after a while it is finished or live. Not available for BASIC plan."
    team1: Home team name
        team2: Away team name
        live: Returns data for a playing match (default false)
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/match/stats"
    querystring = {'team1': team1, 'team2': team2, }
    if live:
        querystring['live'] = live
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def league_players(team: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns all players for a team. Not available for BASIC plan."
    team: Team name
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/players"
    querystring = {'team': team, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def missing_players_for_a_match(team1: str, team2: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return missing players for a match. Not available for BASIC plan."
    team1: Home team name
        team2: Away team name
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/match/missing"
    querystring = {'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def players_statistic_table(stat: str, is_from: str=None, player: str=None, to: str=None, team: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return the players table for a specified statistic. Not available for BASIC plan."
    stat: Statistic name
        is_from: Match day number from which compute the table
        player: Player name
        to: Match day number till which compute the table
        team: Team name
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/playerstat"
    querystring = {'stat': stat, }
    if is_from:
        querystring['from'] = is_from
    if player:
        querystring['player'] = player
    if to:
        querystring['to'] = to
    if team:
        querystring['team'] = team
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def teams_statistic_table(stat: str, avg: str=None, is_from: str=None, mode: str=None, team: str=None, to: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Teams table for a specified statistic. Not available for BASIC plan."
    stat: Statistic name
        avg: Set to true if you want average statistic value, that is the table computed as (total value statistic/played games). Default false.
        is_from: Match day number from which to compute the table
        mode: Set with top to get the top 5, with bottom to get the worse 5 teams (default top)
        team: Team name
        to: Match day number till which compute the table
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/teamstat"
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
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def odds_list(team1: str, bookmaker: str, team2: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the available odds for a match and a bookmaker. Not available for BASIC plan."
    team1: Home team
        bookmaker: Bookmaker name
        team2: Away team
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/listodds"
    querystring = {'team1': team1, 'bookmaker': bookmaker, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bet_stats(bet: str, team: str=None, time: str=None, fromdate: str=None, todate: str=None, over: int=None, mode: str=None, handicap: int=None, when: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns aggregate data about results, goal-nogoal, underover, 1x2 and totalgoals to support your bet activities. Not available for BASIC plan."
    bet: Type of data required, result, totalgoals,underover,1x2,goalnogoal
        team: Team name
        time: Let you to select only first half (FH) result, second half (SH) or full time (FT) default
        fromdate: Only matches fromdate (format mmddyyyy)
        todate: Only matches todate (format mmddyyyy)
        over: Over values, mandatory for underover bet
        mode: Together with team parameter, let you to select only games where team has played home, away or all (default)
        handicap: Handicap values (only for 1x2 bet)
        when: Let you to select only games with win, loss, draw or all (default)
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table/betting"
    querystring = {'bet': bet, }
    if team:
        querystring['team'] = team
    if time:
        querystring['time'] = time
    if fromdate:
        querystring['fromdate'] = fromdate
    if todate:
        querystring['todate'] = todate
    if over:
        querystring['over'] = over
    if mode:
        querystring['mode'] = mode
    if handicap:
        querystring['handicap'] = handicap
    if when:
        querystring['when'] = when
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def odd_quotas(bookmaker: str, odd: str, team1: str, team2: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return quotas for an odd a match and a bookmaker. Not available for BASIC plan."
    bookmaker: Bookmaker name
        odd: Odd name
        team1: Home team
        team2: Away team
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/odds"
    querystring = {'bookmaker': bookmaker, 'odd': odd, 'team1': team1, 'team2': team2, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/push/list"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
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
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/playerdetails"
    querystring = {'player': player, 'team': team, }
    if honours:
        querystring['honours'] = honours
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def league_table(is_from: int=None, mode: str=None, season: str=None, time: str=None, to: int=None, fromdate: str=None, todate: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the table for the league"
    is_from: Optional parameter to specify the first match number to use to compute the table (default 1)
        mode: Optional parameter to restrict the table compute on home or away games (default all)
        season: Season code (default 2017-18)
        time: Let to compute the table considering only the first half (FH) or the second time (SH) results. Default is full time (FT).
        to: Optional parameter to specify the last match number to consider to compute the table (default last match number played registered on system)
        fromdate: Compute the table only with matches played fromdate (format mmddyyyy)
        todate: Compute the table only with matches played todate (format mmddyyyy)
        
    """
    url = f"https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/table"
    querystring = {}
    if is_from:
        querystring['from'] = is_from
    if mode:
        querystring['mode'] = mode
    if season:
        querystring['season'] = season
    if time:
        querystring['time'] = time
    if to:
        querystring['to'] = to
    if fromdate:
        querystring['fromdate'] = fromdate
    if todate:
        querystring['todate'] = todate
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

