import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def recognize_track(link: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Max file size: **20 Mb**
		Recomended formats: **WAV** ,  **OGG** ,  **MP3** ,  **M4A** ,  **MP4**"
    link: ### Example links:

 - http://example.com/files/file_1.wav
        
    """
    url = f"https://shazam-song-recognizer.p.rapidapi.com/recognize"
    querystring = {'link': link, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shazam-song-recognizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_artists(query: str, lang: str='-', start_from: str='0', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search all artists by prefix"
    lang: Country code in ISO 3166-1 alpha-2 format. Affects the search result.
For example: UZ, RU, GB, UK
Default: -
        
    """
    url = f"https://shazam-song-recognizer.p.rapidapi.com/search_artist"
    querystring = {'query': query, }
    if lang:
        querystring['lang'] = lang
    if start_from:
        querystring['start_from'] = start_from
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shazam-song-recognizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def related_tracks(track_id: str, start_from: str='0', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Related tracks based track id
		https://www.shazam.com/track/621482386/rampampam"
    
    """
    url = f"https://shazam-song-recognizer.p.rapidapi.com/related_tracks"
    querystring = {'track_id': track_id, }
    if start_from:
        querystring['start_from'] = start_from
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shazam-song-recognizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_tracks_in_country(country_code: str, start_from: str='0', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the best tracks by country code
		https://www.shazam.com/charts/discovery/uzbekistan"
    country_code: Country code in ISO 3166-1 alpha-2 format.
For example: UZ, RU, GB, UK
        
    """
    url = f"https://shazam-song-recognizer.p.rapidapi.com/top_country_tracks"
    querystring = {'country_code': country_code, }
    if start_from:
        querystring['start_from'] = start_from
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shazam-song-recognizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_tracks_in_city(city_name: str, country_code: str, limit: str='10', start_from: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieving information from an artist profile
		https://www.shazam.com/charts/top-50/uzbekistan/tashkent"
    country_code: Country code in ISO 3166-1 alpha-2 format.
For example: UZ, RU, GB, UK
        
    """
    url = f"https://shazam-song-recognizer.p.rapidapi.com/top_city_tracks"
    querystring = {'city_name': city_name, 'country_code': country_code, }
    if limit:
        querystring['limit'] = limit
    if start_from:
        querystring['start_from'] = start_from
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shazam-song-recognizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def track_listenings_count(track_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the number of times a particular song has been played
		https://www.shazam.com/track/621482386/rampampam"
    
    """
    url = f"https://shazam-song-recognizer.p.rapidapi.com/listening_counter"
    querystring = {'track_id': track_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shazam-song-recognizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_tracks(query: str, lang: str='-', limit: str='10', start_from: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search all tracks by prefix"
    lang: Country code in ISO 3166-1 alpha-2 format. Affects the search result.
For example: UZ, RU, GB, UK
Default: -
        
    """
    url = f"https://shazam-song-recognizer.p.rapidapi.com/search_track"
    querystring = {'query': query, }
    if lang:
        querystring['lang'] = lang
    if limit:
        querystring['limit'] = limit
    if start_from:
        querystring['start_from'] = start_from
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shazam-song-recognizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def about_track(track_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get track information
		https://www.shazam.com/track/621482386/rampampam"
    
    """
    url = f"https://shazam-song-recognizer.p.rapidapi.com/track_about"
    querystring = {'track_id': track_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shazam-song-recognizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(query: str, lang: str='-', limit: str='10', start_from: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "pass"
    lang: Country code in ISO 3166-1 alpha-2 format. Affects the search result.
For example: UZ, RU, GB, UK
Default: -
        
    """
    url = f"https://shazam-song-recognizer.p.rapidapi.com/search"
    querystring = {'query': query, }
    if lang:
        querystring['lang'] = lang
    if limit:
        querystring['limit'] = limit
    if start_from:
        querystring['start_from'] = start_from
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shazam-song-recognizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

