import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def team_php(team_a: str, limit: int=None, venue: str=None, tournament: str=None, orderby: str=None, pagenumber: int=None, pagesize: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return scores for matches between a home team and all away teams."
    team_a: Home Team
        limit: Default = 100, Max = 1000
        venue: Home, Away, Neutral
        tournament: Inter-Cities Fairs Cup, UEFA Champions League, UEFA Cup, UEFA Cupwinners Cup, UEFA Europa League, UEFA European Champions Cup, UEFA Intertoto Cup, UEFA Super Cup
        orderby: TOURNAMENT, COUNTRY_A, TEAM_A, COUNTRY_B, TEAM_B, DATE, VENUE, OUTCOME, GOALS_FOR, GOALS_AGAINST, PHASE
        pagenumber: If pageSize is not empty then default = 1
        pagesize: Possible values from 5 to 1000, if pageNumber is not empty then default = 25
        
    """
    url = f"https://sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com/team.php"
    querystring = {'team_a': team_a, }
    if limit:
        querystring['limit'] = limit
    if venue:
        querystring['VENUE'] = venue
    if tournament:
        querystring['TOURNAMENT'] = tournament
    if orderby:
        querystring['orderBy'] = orderby
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if pagesize:
        querystring['pageSize'] = pagesize
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def country_php(country_a: str, limit: int=None, venue: str=None, tournament: str=None, orderby: str=None, pagenumber: int=None, pagesize: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return scores for matches between all home country teams and all away teams."
    country_a: Home Country
        limit: Default = 100, Max = 1000
        venue: Home, Away, Neutral
        tournament: Inter-Cities Fairs Cup, UEFA Champions League, UEFA Cup, UEFA Cupwinners Cup, UEFA Europa League, UEFA European Champions Cup, UEFA Intertoto Cup, UEFA Super Cup
        orderby: TOURNAMENT, COUNTRY_A, TEAM_A, COUNTRY_B, TEAM_B, DATE, VENUE, OUTCOME, GOALS_FOR, GOALS_AGAINST, PHASE
        pagenumber: If pageSize is not empty then default = 1
        pagesize: Possible values from 5 to 1000, if pageNumber is not empty then default = 25
        
    """
    url = f"https://sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com/country.php"
    querystring = {'country_a': country_a, }
    if limit:
        querystring['limit'] = limit
    if venue:
        querystring['VENUE'] = venue
    if tournament:
        querystring['TOURNAMENT'] = tournament
    if orderby:
        querystring['orderBy'] = orderby
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if pagesize:
        querystring['pageSize'] = pagesize
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def country_vs_country_php(country_a: str, country_b: str, limit: int=None, orderby: str=None, venue: str=None, tournament: str=None, pagenumber: int=None, pagesize: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return scores for matches between all home country teams and all away country teams."
    country_a: Home Country
        country_b: Away Country
        limit: Default = 100, Max = 1000
        orderby: TOURNAMENT, COUNTRY_A, TEAM_A, COUNTRY_B, TEAM_B, DATE, VENUE, OUTCOME, GOALS_FOR, GOALS_AGAINST, PHASE
        venue: Home, Away, Neutral
        tournament: Inter-Cities Fairs Cup, UEFA Champions League, UEFA Cup, UEFA Cupwinners Cup, UEFA Europa League, UEFA European Champions Cup, UEFA Intertoto Cup, UEFA Super Cup
        pagenumber: If pageSize is not empty then default = 1
        pagesize: Possible values from 5 to 1000, if pageNumber is not empty then default = 25
        
    """
    url = f"https://sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com/country-vs-country.php"
    querystring = {'country_a': country_a, 'country_b': country_b, }
    if limit:
        querystring['limit'] = limit
    if orderby:
        querystring['orderBy'] = orderby
    if venue:
        querystring['VENUE'] = venue
    if tournament:
        querystring['TOURNAMENT'] = tournament
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if pagesize:
        querystring['pageSize'] = pagesize
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def countries_php(limit: int=None, pagenumber: int=None, pagesize: int=None, orderby: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a list of all countries names."
    limit: Default = 100, Max = 1000
        pagenumber: If pageSize is not empty then default = 1
        pagesize: Possible values from 5 to 1000, if pageNumber is not empty then default = 25
        orderby: COUNTRY_A
        
    """
    url = f"https://sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com/countries.php"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if pagesize:
        querystring['pageSize'] = pagesize
    if orderby:
        querystring['orderby'] = orderby
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def country_vs_team_php(team_b: str, country_a: str, limit: int=None, venue: str=None, tournament: str=None, orderby: str=None, pagenumber: int=None, pagesize: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return scores for matches between all home country teams and an away team."
    team_b: Away Team
        country_a: Home Country
        limit: Default = 100, Max = 1000
        venue: Home, Away, Neutral
        tournament: Inter-Cities Fairs Cup, UEFA Champions League, UEFA Cup, UEFA Cupwinners Cup, UEFA Europa League, UEFA European Champions Cup, UEFA Intertoto Cup, UEFA Super Cup
        orderby: TOURNAMENT, COUNTRY_A, TEAM_A, COUNTRY_B, TEAM_B, DATE, VENUE, OUTCOME, GOALS_FOR, GOALS_AGAINST, PHASE
        pagenumber: If pageSize is not empty then default = 1
        pagesize: Possible values from 5 to 1000, if pageNumber is not empty then default = 25
        
    """
    url = f"https://sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com/country-vs-team.php"
    querystring = {'team_b': team_b, 'country_a': country_a, }
    if limit:
        querystring['limit'] = limit
    if venue:
        querystring['VENUE'] = venue
    if tournament:
        querystring['TOURNAMENT'] = tournament
    if orderby:
        querystring['orderBy'] = orderby
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if pagesize:
        querystring['pageSize'] = pagesize
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def team_vs_country_php(team_a: str, country_b: str, limit: int=None, venue: str=None, tournament: str=None, orderby: str=None, pagenumber: int=None, pagesize: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return scores for matches between a home team and all away country teams."
    team_a: Home Team
        country_b: Away Country
        limit: Default = 100, Max = 1000
        venue: Home, Away, Neutral
        tournament: Inter-Cities Fairs Cup, UEFA Champions League, UEFA Cup, UEFA Cupwinners Cup, UEFA Europa League, UEFA European Champions Cup, UEFA Intertoto Cup, UEFA Super Cup
        orderby: TOURNAMENT, COUNTRY_A, TEAM_A, COUNTRY_B, TEAM_B, DATE, VENUE, OUTCOME, GOALS_FOR, GOALS_AGAINST, PHASE
        pagenumber: If pageSize is not empty then default = 1
        pagesize: Possible values from 5 to 1000, if pageNumber is not empty then default = 25
        
    """
    url = f"https://sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com/team-vs-country.php"
    querystring = {'team_a': team_a, 'country_b': country_b, }
    if limit:
        querystring['limit'] = limit
    if venue:
        querystring['VENUE'] = venue
    if tournament:
        querystring['TOURNAMENT'] = tournament
    if orderby:
        querystring['orderBy'] = orderby
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if pagesize:
        querystring['pageSize'] = pagesize
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def teams_php(limit: int=None, pagenumber: int=None, pagesize: int=None, orderby: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a list of all teams names."
    limit: Default = 100, Max = 1000
        pagenumber: If pageSize is not empty then default = 1
        pagesize: Possible values from 5 to 1000, if pageNumber is not empty then default = 25
        orderby: COUNTRY_A, TEAM_A
        
    """
    url = f"https://sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com/teams.php"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if pagesize:
        querystring['pageSize'] = pagesize
    if orderby:
        querystring['orderby'] = orderby
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def team_vs_team_php(team_a: str, team_b: str, pagenumber: int=None, limit: int=None, orderby: str=None, pagesize: int=None, venue: str=None, tournament: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return scores for matches between a home teams and an away team."
    team_a: Home Team
        team_b: Away Team
        pagenumber: If pageSize is not empty then default = 1
        limit: Default = 100, Max = 1000
        orderby: TOURNAMENT, COUNTRY_A, TEAM_A, COUNTRY_B, TEAM_B, DATE, VENUE, OUTCOME, GOALS_FOR, GOALS_AGAINST, PHASE
        pagesize: Possible values from 5 to 1000, if pageNumber is not empty then default = 25
        venue: Home, Away, Neutral
        tournament: Inter-Cities Fairs Cup, UEFA Champions League, UEFA Cup, UEFA Cupwinners Cup, UEFA Europa League, UEFA European Champions Cup, UEFA Intertoto Cup, UEFA Super Cup
        
    """
    url = f"https://sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com/team-vs-team.php"
    querystring = {'team_a': team_a, 'team_b': team_b, }
    if pagenumber:
        querystring['pagenumber'] = pagenumber
    if limit:
        querystring['limit'] = limit
    if orderby:
        querystring['orderBy'] = orderby
    if pagesize:
        querystring['pageSize'] = pagesize
    if venue:
        querystring['VENUE'] = venue
    if tournament:
        querystring['TOURNAMENT'] = tournament
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sportstatsguru-ssg-football-clubs-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

