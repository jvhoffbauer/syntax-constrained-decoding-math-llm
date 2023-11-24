import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def seasons(limit: str='50', offset: str='0', is_id: str='eq.982', league_id: str='eq.979', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all seasons.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated every 1 month.<br />**Recommended Calls**: 1 call per month.
		
		### Use Cases
		Get all seasons<br />`https://beach-volleyball.sportdetect.com/seasons`<br /><br />Get the seasons from the `id`<br />`https://beach-volleyball.sportdetect.com/seasons?id=eq.{id}`<br /><br />Get the seasons from the `league_id`<br />`https://beach-volleyball.sportdetect.com/seasons?league_id=eq.{league_id}`"
    limit: Limiting and Pagination
        offset: Limiting and Pagination
        is_id: The id of the season. example:`eq.{id}`
        league_id: The id of the league. example:`eq.{league_id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/seasons"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    if is_id:
        querystring['id'] = is_id
    if league_id:
        querystring['league_id'] = league_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def cuptrees(is_id: str='eq.13915', season_id: str='eq.1990', offset: str='0', league_id: str='eq.1547', limit: str='50', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all cup knock outs.
		You can use `id` from the `seasons` or `leagues` endpoint to get the wanted cup knock out tree.
		
		Fields in rounds:
		
		Field | Explanation
		--- | ---
		`order` | The order of the round
		`description` | The description of the round
		`blocks` | The blocks of the round
		`finished` | If the event is finished
		`order` | The order of the block
		`home_team_score` | The score of the home team
		`away_team_score` | The score of the away team
		`has_next_round_link` | If the event has next round
		`event_in_progress` | If the event is in play
		`series_start_date_timestamp` | The start date of the event
		`automatic_progression` | If the event has automatic progression
		`participants` | The participants of the block (event)
		`team_id` | The id of the team
		`winner` | If the team is winner of the block
		`order` | The order of the participants
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated after every finished match.<br />**Recommended Calls**: 1 call after finished match.
		
		### Use Cases
		Get one cup knock out from the `id`<br />`https://beach-volleyball.sportdetect.com/cuptrees?id=eq.{id}`<br /><br />Get cups from the `season_id`<br />`https://beach-volleyball.sportdetect.com/cuptrees?season_id=eq.{season_id}`<br /><br />Get cups from the `league_id`<br />`https://beach-volleyball.sportdetect.com/cuptrees?league_id=eq.{league_id}`"
    is_id: The id of the cup tree. example:`eq.{id}`
        season_id: The id of the season. example:`eq.{season_id}`
        offset: Limiting and Pagination
        league_id: The id of the league. example:`eq.{league_id}`
        limit: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/cuptrees"
    querystring = {}
    if is_id:
        querystring['id'] = is_id
    if season_id:
        querystring['season_id'] = season_id
    if offset:
        querystring['offset'] = offset
    if league_id:
        querystring['league_id'] = league_id
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def countries(alpha: str='eq.NX', is_id: str='eq.1', limit: str='50', offset: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all countries.
		You can use the `alpha` field to get the country
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated every hour.<br />**Recommended Calls**: 1 call per hour.
		
		You can get the image of the country by calling the following url: `https://images.sportdetect.com/{hash_image}.png`
		
		### Use Cases
		Get all countries<br />`https://beach-volleyball.sportdetect.com/countries`<br /><br />Get the country from the `id`<br />`https://beach-volleyball.sportdetect.com/countries?id=eq.{id}`<br /><br />Get all countries from the `alpha`<br />`https://beach-volleyball.sportdetect.com/countries?alpha=eq.{alpha}`"
    alpha: The alpha2 name of the country. example:`eq.{alpha}`
        is_id: The id of the country. example:`eq.{id}`
        limit: Limiting and Pagination
        offset: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/countries"
    querystring = {}
    if alpha:
        querystring['alpha'] = alpha
    if is_id:
        querystring['id'] = is_id
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def seasons_info(offset: str='0', limit: str='50', season_id: str='eq.982', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all season's info.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated every 1 hour.<br />**Recommended Calls**: 1 call per hour.
		
		### Use Cases
		Get the info from the `season_id`<br />`https://beach-volleyball.sportdetect.com/seasons-info?season_id=eq.{season_id}`"
    offset: Limiting and Pagination
        limit: Limiting and Pagination
        season_id: The id of the season. example:`eq.{season_id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/seasons-info"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if limit:
        querystring['limit'] = limit
    if season_id:
        querystring['season_id'] = season_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def seasons_rounds(offset: str='0', limit: str='50', season_id: str='eq.5032', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all season's rounds.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated every 1 hour.<br />**Recommended Calls**: 1 call per hour.
		
		### Use Cases
		Get the rounds from the `season_id`<br />`https://beach-volleyball.sportdetect.com/seasons-rounds?season_id=eq.{season_id}`"
    offset: Limiting and Pagination
        limit: Limiting and Pagination
        season_id: The id of the season. example:`eq.{season_id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/seasons-rounds"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if limit:
        querystring['limit'] = limit
    if season_id:
        querystring['season_id'] = season_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def tournaments(offset: str='0', league_id: str='eq.11346', limit: str='50', is_id: str='eq.59012', category_id: str='eq.233', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all tournaments.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a week.<br />**Recommended Calls**: Several times a week.
		
		### Use Cases
		Get all tournaments<br />`https://beach-volleyball.sportdetect.com/tournaments`<br /><br />Get the tournaments from the `id`<br />`https://beach-volleyball.sportdetect.com/tournaments?id=eq.{id}`<br /><br />Get the tournaments from the `league_id`<br />`https://beach-volleyball.sportdetect.com/tournaments?league_id=eq.{league_id}`<br /><br />Get the tournaments from the `category_id`<br />`https://beach-volleyball.sportdetect.com/tournaments?category_id=eq.{category_id}`"
    offset: Limiting and Pagination
        league_id: The id of the league. example:`eq.{league_id}`
        limit: Limiting and Pagination
        is_id: The id of the tournament. example:`eq.{id}`
        category_id: The id of the category. example:`eq.{category_id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/tournaments"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if league_id:
        querystring['league_id'] = league_id
    if limit:
        querystring['limit'] = limit
    if is_id:
        querystring['id'] = is_id
    if category_id:
        querystring['category_id'] = category_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def categories(offset: str='0', limit: str='50', alpha: str='eq.AR', is_id: str='eq.235', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all categories.
		You can use the `alpha` field to get the specific category as a country.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated every hour.<br />**Recommended Calls**: 1 call per hour.
		
		You can get the image of the category by calling the following url: `https://images.sportdetect.com/{hash_image}.png`
		
		### Use Cases
		Get all categories<br />`https://beach-volleyball.sportdetect.com/categories`<br /><br />Get one category from the `id`<br />`https://beach-volleyball.sportdetect.com/categories?id=eq.{id}`<br /><br />Get all categories from the `alpha`<br />`https://beach-volleyball.sportdetect.com/categories?alpha=eq.{alpha}`"
    offset: Limiting and Pagination
        limit: Limiting and Pagination
        alpha: The alpha2 name of the category (_country_). example:`eq.{alpha}`
        is_id: The id of the category. example:`eq.{id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/categories"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if limit:
        querystring['limit'] = limit
    if alpha:
        querystring['alpha'] = alpha
    if is_id:
        querystring['id'] = is_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def standings(offset: str='0', is_id: str='eq.73881', league_id: str='eq.977', limit: str='50', season_id: str='eq.1126', type: str='eq.total', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all standings.
		For the type argument you can search by: **home**, **away** and **total**.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated after every finished match.<br />**Recommended Calls**: 1 call per finished match.
		
		### Use Cases
		Get all standings<br />`https://beach-volleyball.sportdetect.com/standings`<br /><br />Get the standing from the `id`<br />`https://beach-volleyball.sportdetect.com/standings?id=eq.{id}`<br /><br />Get the standing from the `league_id`<br />`https://beach-volleyball.sportdetect.com/standings?league_id=eq.{league_id}`<br /><br />Get the standing from the `league_id` and `season_id`<br />`https://beach-volleyball.sportdetect.com/standings?league_id=eq.{league_id}&season_id=eq.{season_id}`<br /><br />Get the standing from the `league_id`, `season_id` and `type`<br />`https://beach-volleyball.sportdetect.com/standings?league_id=eq.{league_id}&season_id=eq.{season_id}&type=eq.{type}`"
    offset: Limiting and Pagination
        is_id: The id of the standing. example:`eq.{id}`
        league_id: The id of the league. example:`eq.{league_id}`
        limit: Limiting and Pagination
        season_id: The id of the season. example:`eq.{season_id}`
        type: The type of the standing. example:`eq.{type}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/standings"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if is_id:
        querystring['id'] = is_id
    if league_id:
        querystring['league_id'] = league_id
    if limit:
        querystring['limit'] = limit
    if season_id:
        querystring['season_id'] = season_id
    if type:
        querystring['type'] = type
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def money(limit: str='50', is_id: str='eq.85', offset: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all money values.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		### Use Cases
		Get the money from the `id`<br />`https://beach-volleyball.sportdetect.com/money?id=eq.{id}`"
    limit: Limiting and Pagination
        is_id: The id. example:`eq.{id}`
        offset: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/money"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if is_id:
        querystring['id'] = is_id
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def news_teams(team_id: str='eq.5046', offset: str='0', limit: str='50', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all news of the teams.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated every 15 minutes.<br />**Recommended Calls**: 1 call every 15 minutes.
		
		### Use Cases
		Get the news from the `team_id`<br />`https://beach-volleyball.sportdetect.com/news-teams?team_id=eq.{team_id}`"
    team_id: The id of the team. example:`eq.{team_id}`
        offset: Limiting and Pagination
        limit: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/news-teams"
    querystring = {}
    if team_id:
        querystring['team_id'] = team_id
    if offset:
        querystring['offset'] = offset
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def news_leagues(offset: str='0', limit: str='50', league_id: str='eq.1246', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all news of the leagues.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated every 15 minutes.<br />**Recommended Calls**: 1 call every 15 minutes.
		
		### Use Cases
		Get the news from the `league_id`<br />`https://beach-volleyball.sportdetect.com/news-leagues?league_id=eq.{league_id}`"
    offset: Limiting and Pagination
        limit: Limiting and Pagination
        league_id: The id of the league. example:`eq.{league_id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/news-leagues"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if limit:
        querystring['limit'] = limit
    if league_id:
        querystring['league_id'] = league_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def venues(offset: str='0', is_id: str='eq.1', limit: str='50', country_id: str='eq.3', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all venues.
		With geolocation attribute from `geolocations` endpoint we can see latitude and longitute of the venue.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a week.<br />**Recommended Calls**: Several times a week.
		
		You can get the image of the venue by calling the following url: `https://images.sportdetect.com/{hash_image}.png`
		
		### Use Cases
		Get all venues<br />`https://beach-volleyball.sportdetect.com/venues`<br /><br />Get the venues from the `id`<br />`https://beach-volleyball.sportdetect.com/venues?id=eq.{id}`<br /><br />Get the venues from the `country_id`<br />`https://beach-volleyball.sportdetect.com/venues?country_id=eq.{country_id}`"
    offset: Limiting and Pagination
        is_id: The id of the venue. example:`eq.{id}`
        limit: Limiting and Pagination
        country_id: The id of the country. example:`eq.{country_id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/venues"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if is_id:
        querystring['id'] = is_id
    if limit:
        querystring['limit'] = limit
    if country_id:
        querystring['country_id'] = country_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def geolocations(limit: str='50', offset: str='0', is_id: str='eq.1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return the geolocation of the venues.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated according to the venues.<br />**Recommended Calls**: 1 call per every venue.
		
		### Use Cases
		Get the geolocation from the `id`<br />`https://beach-volleyball.sportdetect.com/geolocations?id=eq.{id}`"
    limit: Limiting and Pagination
        offset: Limiting and Pagination
        is_id: The id of the location. example:`eq.{id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/geolocations"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    if is_id:
        querystring['id'] = is_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def events_live(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all live events from the sport.
		
		It has the same results as the Events endpoint."
    
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/events-live"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def teams(limit: str='50', tournament_id: str='eq.9465', country_id: str=None, category_id: str='eq.233', primary_league_id: str=None, is_id: str='eq.32024', offset: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    limit: Limiting and Pagination
        tournament_id: The id of the tournament. example:`eq.{tournament_id}`
        country_id: The id of the country. example:`eq.{country_id}`
        category_id: The id of the category. example:`eq.{category_id}`
        primary_league_id: The id of the primary league
        is_id: The id of the team. example:`eq.{id}`
        offset: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/teams"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if tournament_id:
        querystring['tournament_id'] = tournament_id
    if country_id:
        querystring['country_id'] = country_id
    if category_id:
        querystring['category_id'] = category_id
    if primary_league_id:
        querystring['primary_league_id'] = primary_league_id
    if is_id:
        querystring['id'] = is_id
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def events(limit: str='50', home_team_id: str='eq.47776', venue_id: str='eq.5313', season_id: str=None, tournament_id: str='eq.9465', is_id: str='eq.1', offset: str='0', referee_id: str=None, away_team_id: str='eq.30785', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all events.
		You can use `id` from the `seasons`, `tournaments`, `rounds`, `venues`, `referees` and `teams` endpoint to get the events.
		Events status codes:
		
		`type` | `description`
		--- | ---
		canceled | Canceled
		canceled | Abandoned
		delayed | Start delayed
		finished | Removed
		finished | Coverage canceled
		finished | Walkover
		finished | Retired
		finished | Ended
		interrupted | Interrupted
		notstarted | Not started
		postponed | Postponed
		
		For **scores** we have fields for covering that: `current`, `display`, `period1`, `period2`, `period3`, `period4`, `period5`, `normaltime`.
		
		For **time extras or injuries** we have fields for covering that: **current_period_start_timestamp**.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated every 10 seconds.<br />**Recommended Calls**: 1 call every 10 seconds.
		
		### Use Cases
		Get all events<br />`https://beach-volleyball.sportdetect.com/events`<br /><br />Get event from the `id`<br />`https://beach-volleyball.sportdetect.com/events?id=eq.{id}`<br /><br />Get events from the `season_id`<br />`https://beach-volleyball.sportdetect.com/events?season_id=eq.{season_id}`<br /><br />Get events from the `tournament_id`<br />`https://beach-volleyball.sportdetect.com/events?tournament_id=eq.{tournament_id}`<br /><br />Get events from the `round_id`<br />`https://beach-volleyball.sportdetect.com/events?round_id=eq.{round_id}`<br /><br />Get events from the `venue_id`<br />`https://beach-volleyball.sportdetect.com/events?venue_id=eq.{venue_id}`<br /><br />Get events from the `referee_id`<br />`https://beach-volleyball.sportdetect.com/events?referee_id=eq.{referee_id}`<br /><br />**H2H** - Get head to head events with teams ex.(home_team_id, away_team_id)<br />`https://beach-volleyball.sportdetect.com/events?or=(home_team_id.eq.{home_team_id}, away_team_id.eq.{home_team_id}, home_team_id.eq.{away_team_id}, away_team_id.eq.{away_team_id})`<br /><br />Get home team events from the `home_team_id`<br />`https://beach-volleyball.sportdetect.com/events?home_team_id=eq.{home_team_id}`<br /><br />Get away team events from the `away_team_id`<br />`https://beach-volleyball.sportdetect.com/events?away_team_id=eq.{away_team_id}`"
    limit: Limiting and Pagination
        home_team_id: The id of the home team. example:`eq.{home_team_id}`
        venue_id: The id of the venue. example:`eq.{venue_id}`
        season_id: The id of the season. example:`eq.{season_id}`
        tournament_id: The id of the tournament. example:`eq.{tournament_id}`
        is_id: The id of the event. example:`eq.{id}`
        offset: Limiting and Pagination
        referee_id: The id of the referee. example:`eq.{referee_id}`
        away_team_id: The id of the away team. example:`eq.{away_team_id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/events"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if home_team_id:
        querystring['home_team_id'] = home_team_id
    if venue_id:
        querystring['venue_id'] = venue_id
    if season_id:
        querystring['season_id'] = season_id
    if tournament_id:
        querystring['tournament_id'] = tournament_id
    if is_id:
        querystring['id'] = is_id
    if offset:
        querystring['offset'] = offset
    if referee_id:
        querystring['referee_id'] = referee_id
    if away_team_id:
        querystring['away_team_id'] = away_team_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def events_coverage(limit: str='50', event_id: str='eq.1', offset: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all event's coverages.
		With this endpoint you can see what data does your event has.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated after every hour.<br />**Recommended Calls**: 1 call after every match.
		
		### Use Cases
		Get the event coverage from the `event_id`<br />`https://beach-volleyball.sportdetect.com/events-coverage?event_id=eq.{event_id}`"
    limit: Limiting and Pagination
        event_id: The id of the event. example:`eq.{event_id}`
        offset: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/events-coverage"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if event_id:
        querystring['event_id'] = event_id
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def teams_seasons(offset: str='0', team_id: str='eq.4651', limit: str='50', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all team's seasons.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a day.<br />**Recommended Calls**: Several times a day.
		
		### Use Cases
		Get the seasons from the `team_id`<br />`https://beach-volleyball.sportdetect.com/teams-seasons?team_id=eq.{team_id}`"
    offset: Limiting and Pagination
        team_id: The id of the team. example:`eq.{team_id}`
        limit: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/teams-seasons"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if team_id:
        querystring['team_id'] = team_id
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def leagues_info_official_organisation(limit: str='50', league_id: str='eq.1', offset: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return official organisations of the leagues and the cups.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a day.<br />**Recommended Calls**: 1 call per day.
		
		### Use Cases
		Get the official organisation from the `league_id`<br />`https://beach-volleyball.sportdetect.com/leagues-info-official-organisation?league_id=eq.{league_id}`"
    limit: Limiting and Pagination
        league_id: The id of the league. example:`eq.{league_id}`
        offset: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/leagues-info-official-organisation"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if league_id:
        querystring['league_id'] = league_id
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def leagues_info_tv_partners(limit: str='50', league_id: str='eq.1', offset: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all tv partners of the leagues and the cups.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a day.<br />**Recommended Calls**: 1 call per day.
		
		### Use Cases
		Get the tv partners from the `league_id`<br />`https://beach-volleyball.sportdetect.com/leagues-info-tv-partners?league_id=eq.{league_id}`"
    limit: Limiting and Pagination
        league_id: The id of the league. example:`eq.{league_id}`
        offset: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/leagues-info-tv-partners"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if league_id:
        querystring['league_id'] = league_id
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def leagues_info_promotions(offset: str='0', league_id: str='eq.1', limit: str='50', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all promotions of the leagues and the cups.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a day.<br />**Recommended Calls**: 1 call per day.
		
		### Use Cases
		Get the promotions from the `league_id`<br />`https://beach-volleyball.sportdetect.com/leagues-info-promotions?league_id=eq.{league_id}`"
    offset: Limiting and Pagination
        league_id: The id of the league. example:`eq.{league_id}`
        limit: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/leagues-info-promotions"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if league_id:
        querystring['league_id'] = league_id
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def leagues_info_largest_stadium(offset: str='0', league_id: str='eq.1', limit: str='50', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all largest stadiums of of the leagues and the cups.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a day.<br />**Recommended Calls**: 1 call per month.
		
		### Use Cases
		Get the largest stadium from the `league_id`<br />`https://beach-volleyball.sportdetect.com/leagues-info-largest-stadium?league_id=eq.{league_id}`"
    offset: Limiting and Pagination
        league_id: The id of the league. example:`eq.{league_id}`
        limit: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/leagues-info-largest-stadium"
    querystring = {}
    if offset:
        querystring['offset'] = offset
    if league_id:
        querystring['league_id'] = league_id
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def leagues(limit: str='50', category_id: str='eq.233', offset: str='0', is_id: str='eq.1245', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all leagues and cups.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a day.<br />**Recommended Calls**: 1 call per hour.
		
		You can get the image of the league by calling the following url: `https://images.sportdetect.com/{hash_image}.png`
		
		### Use Cases
		Get all leagues<br />`https://beach-volleyball.sportdetect.com/leagues`<br /><br />Search the leagues by the `name`<br />`https://beach-volleyball.sportdetect.com/leagues?name=like.*Championship*`<br /><br />Get the leagues from the `id`<br />`https://beach-volleyball.sportdetect.com/leagues?id=eq.{id}`<br /><br />Get the leagues from the `category_id`<br />`https://beach-volleyball.sportdetect.com/leagues?category_id=eq.{category_id}`"
    limit: Limiting and Pagination
        category_id: The id of the category. example:`eq.{category_id}`
        offset: Limiting and Pagination
        is_id: The id of the league. example:`eq.{id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/leagues"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if category_id:
        querystring['category_id'] = category_id
    if offset:
        querystring['offset'] = offset
    if is_id:
        querystring['id'] = is_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def leagues_info_last_season_attendance(league_id: str='eq.1', limit: str='50', offset: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all last season attendance of the leagues and the cups.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a day.<br />**Recommended Calls**: 1 call after every finished season.
		
		### Use Cases
		Get the last season attendance from the `league_id`<br />`https://beach-volleyball.sportdetect.com/leagues-info-last-season-attendance?league_id=eq.{league_id}`"
    league_id: The id of the league. example:`eq.{league_id}`
        limit: Limiting and Pagination
        offset: Limiting and Pagination
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/leagues-info-last-season-attendance"
    querystring = {}
    if league_id:
        querystring['league_id'] = league_id
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def leagues_info_last_season_top_scorers(limit: str='50', offset: str='0', league_id: str='eq.1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this endpoint you can return all last top scorers of the leagues and the cups.
		
		This endpoint uses a pagination system and the page argument allows you to switch between the various pages.
		
		To switch pages you should use `/{endpoint}?limit={limit}&offset={offset}` ex.(`/{endpoint}?limit=15&offset=30}`) as parameters in endpoint.
		
		> **Pagination**: 50 results per page. Enter offset and limit number to get the next results.
		
		**Update Period**: The endpoint is updated several times a day.<br />**Recommended Calls**: 1 call after every finished season.
		
		### Use Cases
		Get the top scorers from the `league_id`<br />`https://beach-volleyball.sportdetect.com/leagues-info-last-season-top-scorers?league_id=eq.{league_id}`"
    limit: Limiting and Pagination
        offset: Limiting and Pagination
        league_id: The id of the league. example:`eq.{league_id}`
        
    """
    url = f"https://beach-volleyball-detect.p.rapidapi.com/leagues-info-last-season-top-scorers"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    if league_id:
        querystring['league_id'] = league_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "beach-volleyball-detect.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

