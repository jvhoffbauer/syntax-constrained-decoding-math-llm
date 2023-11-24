import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_users(country: str='ma', pcursor: str=None, language: str='en', user_name: str='paul', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Users API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/search-users"
    querystring = {}
    if country:
        querystring['country'] = country
    if pcursor:
        querystring['pcursor'] = pcursor
    if language:
        querystring['language'] = language
    if user_name:
        querystring['user_name'] = user_name
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_posts(keyword: str, pcursor: str=None, language: str='en', country: str='ma', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Posts API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/search-posts"
    querystring = {'keyword': keyword, }
    if pcursor:
        querystring['pcursor'] = pcursor
    if language:
        querystring['language'] = language
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_trending(language: str='en', pcursor: str=None, country: str='ma', count: str='30', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Trending API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/search-trending"
    querystring = {}
    if language:
        querystring['language'] = language
    if pcursor:
        querystring['pcursor'] = pcursor
    if country:
        querystring['country'] = country
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_top_music(country: str='ma', language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Top Music API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/search-top-music"
    querystring = {}
    if country:
        querystring['country'] = country
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_recommend(language: str='en', pcursor: str=None, country: str='ma', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "User Recommend API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/user-recommend"
    querystring = {}
    if language:
        querystring['language'] = language
    if pcursor:
        querystring['pcursor'] = pcursor
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def login_with_mobile_code(countrycode: str, sms_code: str, session: str, mobile: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Login with Mobile Code API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/login-with-mobile-code"
    querystring = {'countryCode': countrycode, 'sms_code': sms_code, 'session': session, 'mobile': mobile, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def send_sms_code(countrycode: str, mobile: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Send SMS Code API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/send-sms-code"
    querystring = {'countryCode': countrycode, 'mobile': mobile, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_followers(userid: str, token: str, pcursor: str=None, count: str='20', page: str='1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "User Followers API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/user-followers"
    querystring = {'userId': userid, 'token': token, }
    if pcursor:
        querystring['pcursor'] = pcursor
    if count:
        querystring['count'] = count
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_following(userid: str, token: str, page: str='1', pcursor: str=None, count: str='20', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "User Following API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/user-following"
    querystring = {'userId': userid, 'token': token, }
    if page:
        querystring['page'] = page
    if pcursor:
        querystring['pcursor'] = pcursor
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_user(userid: str, language: str='en', country: str='ma', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get User API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/user-profile"
    querystring = {'userId': userid, }
    if language:
        querystring['language'] = language
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def tag_search(keyword: str, count: str='30', language: str='en', country: str='ma', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Tag Search API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/tag-search"
    querystring = {'keyword': keyword, }
    if count:
        querystring['count'] = count
    if language:
        querystring['language'] = language
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_mix(keyword: str, pcursor: str=None, country: str='ma', language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Mix API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/search-mix"
    querystring = {'keyword': keyword, }
    if pcursor:
        querystring['pcursor'] = pcursor
    if country:
        querystring['country'] = country
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_suggest(keyword: str, country: str='ma', language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Suggest API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/search-suggest"
    querystring = {'keyword': keyword, }
    if country:
        querystring['country'] = country
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_music(keyword: str, country: str='ma', pcursor: str=None, language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Music API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/search-music"
    querystring = {'keyword': keyword, }
    if country:
        querystring['country'] = country
    if pcursor:
        querystring['pcursor'] = pcursor
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_music(musicid: str, country: str='ma', language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Music API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/get-music"
    querystring = {'musicId': musicid, }
    if country:
        querystring['country'] = country
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def top_music(count: str='20', pcursor: str=None, language: str='en', country: str='ma', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Top Music API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/top-music"
    querystring = {}
    if count:
        querystring['count'] = count
    if pcursor:
        querystring['pcursor'] = pcursor
    if language:
        querystring['language'] = language
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def liked_posts(userid: str, language: str='en', count: str='30', country: str='ma', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Liked Posts API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/liked-posts"
    querystring = {'userId': userid, }
    if language:
        querystring['language'] = language
    if count:
        querystring['count'] = count
    if country:
        querystring['country'] = country
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_feed(userid: str, country: str='ma', count: str='30', pcursor: str=None, language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "User Feed API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/feed-profile"
    querystring = {'userId': userid, }
    if country:
        querystring['country'] = country
    if count:
        querystring['count'] = count
    if pcursor:
        querystring['pcursor'] = pcursor
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def feed_hot(country: str='ma', count: str='30', language: str='en', pcursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Feed Hot API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/feed-hot"
    querystring = {}
    if country:
        querystring['country'] = country
    if count:
        querystring['count'] = count
    if language:
        querystring['language'] = language
    if pcursor:
        querystring['pcursor'] = pcursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def feed(country: str='ma', language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Feed API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/feed"
    querystring = {}
    if country:
        querystring['country'] = country
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_comments(photoid: str, count: str='10', order: str='desc', country: str='ma', pcursor: str=None, language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List Comments API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/list-comments"
    querystring = {'photoId': photoid, }
    if count:
        querystring['count'] = count
    if order:
        querystring['order'] = order
    if country:
        querystring['country'] = country
    if pcursor:
        querystring['pcursor'] = pcursor
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_post(photoid: str, country: str='ma', language: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Post API"
    
    """
    url = f"https://kwai4.p.rapidapi.com/get-post"
    querystring = {'photoId': photoid, }
    if country:
        querystring['country'] = country
    if language:
        querystring['language'] = language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kwai4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

