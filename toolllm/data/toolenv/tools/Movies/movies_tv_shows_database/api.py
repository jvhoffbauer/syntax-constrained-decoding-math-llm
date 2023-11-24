import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_tv_series_by_year(year: str, page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return tv series results with title, year, id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'year': year, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tv_schedule_by_country(country: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return TV Series Name, Season Number, Episode number, Episode name, Air date, air time, runtime, Network, series  id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'country': country, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tv_series_episodes_by_series_id_season_number(season: str, seriesid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A valid TV Series ID (e.g. tt2741602)
		return Episode number, episode name, episode air date, vote average, vote count"
    seriesid: A valid Series ID (e.g. tt2741602)
        
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'season': season, 'seriesid': seriesid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_airing_today_tv_shows(page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return tv series results with title, id, year"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {}
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_trending_tv_shows(page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return tv series results with title, id, year"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {}
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tv_on_the_air(page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return tv series results with title, id, year"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {}
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_popular_tv_shows_by_year(year: str, page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return tv series results with title, id, year"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'year': year, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_recently_added_tv_series_by_release_date(page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return tv series results with title, id, year"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {}
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tv_series_aliases_by_id(seriesid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A valid TV Series ID (e.g. tt2741602)
		return tv series aliases"
    seriesid: A valid Series ID (e.g. tt2741602)
        
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'seriesid': seriesid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tv_series_images_by_id(seriesid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A valid TV Series ID (e.g. tt2741602)
		return poster, fanart"
    seriesid: A valid Series ID (e.g. tt2741602)
        
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'seriesid': seriesid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tv_series_by_title(title: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search by TV Series Title
		return title, id, release_date"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'title': title, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_by_tv_series_by_id(seriesid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A valid TV Series ID (e.g. tt2741602)
		
		return title, description, release_date, id, irating, vote_count, meta, popularity, youtube_trailer_key"
    seriesid: A valid Series ID (e.g. tt2741602)
        
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'seriesid': seriesid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_movies_by_year(year: str, page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return movie results with title, year , id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'year': year, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_similar_movies(movieid: str, page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return movie results with title , release date , id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'movieid': movieid, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_box_office_movies(page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return movie results with title , year , id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {}
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_trending_movies(page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return movie results with title , year , id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {}
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_now_playing_movies(page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return movie results with title, year, id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {}
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_popular_movies_by_year(year: str, page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return movie results with title , year , id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'year': year, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_movie_aliases_by_id(movieid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A valid Movie ID (e.g. tt1375666)
		return movie aliases"
    movieid: A valid Movie ID (e.g. tt1375666)
        
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'movieid': movieid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_movie_images_by_id(movieid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A valid Movie ID (e.g. tt1375666)
		return title, id, poster, fanart"
    movieid: A valid Movie ID (e.g. tt1375666)
        
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'movieid': movieid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_movies_by_title(title: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Result set includes all search results
		Each item includes fields:
		Title
		Year
		Movie  ID"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'title': title, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_movie_by_id(movieid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A valid Movie ID (e.g. tt1375666)
		return Title, Description, Year, Release Date, Rated, Runtime, Genre, Directors, Actors, Languages, Country
		 Rating, votes, Popularity, id"
    movieid: A valid Movie ID (e.g. tt1375666)
        
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'movieid': movieid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_upcoming_movies(page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return movie results with title, year, id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {}
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tv_series_seasons_by_id(seriesid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A valid TV Series ID (e.g. tt2741602)
		return Season number, season air date, Episode count, Season trailer"
    seriesid: A valid Series ID (e.g. tt2741602)
        
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'seriesid': seriesid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_similar_tv_shows(seriesid: str, page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return tv series results with title, id, release date"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {'seriesid': seriesid, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_recently_added_movies_by_release_date(page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get recently added movies 
		return title, year,  id"
    
    """
    url = f"https://movies-tv-shows-database.p.rapidapi.com/"
    querystring = {}
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

