import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def user_following(user_id: str=None, username: str='elonmusk', cursor: str=None, count: int=20, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get user following"
    count: Available for paid users only - Default is 20 (max is 100)
        
    """
    url = f"https://twttrapi.p.rapidapi.com/user-following"
    querystring = {}
    if user_id:
        querystring['user_id'] = user_id
    if username:
        querystring['username'] = username
    if cursor:
        querystring['cursor'] = cursor
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_followers(username: str='elonmusk', user_id: str=None, cursor: str=None, count: int=20, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get user followers"
    count: Available for paid users only - Default is 20 (max is 100)
        
    """
    url = f"https://twttrapi.p.rapidapi.com/user-followers"
    querystring = {}
    if username:
        querystring['username'] = username
    if user_id:
        querystring['user_id'] = user_id
    if cursor:
        querystring['cursor'] = cursor
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_likes(user_id: str=None, username: str='elonmusk', cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get user's likes"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/user-likes"
    querystring = {}
    if user_id:
        querystring['user_id'] = user_id
    if username:
        querystring['username'] = username
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def following_timeline(cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the "Following" timeline"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/following-timeline"
    querystring = {}
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def for_you_timeline(cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the "For You" timeline"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/for-you-timeline"
    querystring = {}
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tweet(tweet_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a tweet"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/get-tweet"
    querystring = {'tweet_id': tweet_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_media(username: str='elonmusk', user_id: str=None, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get user's images"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/user-media"
    querystring = {}
    if username:
        querystring['username'] = username
    if user_id:
        querystring['user_id'] = user_id
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_tweets(cursor: str=None, user_id: str=None, username: str='elonmusk', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get user's tweets"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/user-tweets"
    querystring = {}
    if cursor:
        querystring['cursor'] = cursor
    if user_id:
        querystring['user_id'] = user_id
    if username:
        querystring['username'] = username
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_dm_conversation(user_id: str=None, max_id: str=None, username: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get single conversation messages"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/get-dm-conversation"
    querystring = {}
    if user_id:
        querystring['user_id'] = user_id
    if max_id:
        querystring['max_id'] = max_id
    if username:
        querystring['username'] = username
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_dm_conversations(cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get direct message conversations and messages"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/get-dm-conversations"
    querystring = {}
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_suggestions(query: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search suggestions"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/search-suggestions"
    querystring = {'query': query, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_videos(query: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search videos"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/search-videos"
    querystring = {'query': query, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_images(query: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search images"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/search-images"
    querystring = {'query': query, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_users(query: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search users"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/search-users"
    querystring = {'query': query, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_latest(query: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search latest results"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/search-latest"
    querystring = {'query': query, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_top(query: str, cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search top results"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/search-top"
    querystring = {'query': query, }
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tweet_conversation(tweet_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a tweet conversation"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/get-tweet-conversation"
    querystring = {'tweet_id': tweet_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_user(username: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get user information"
    
    """
    url = f"https://twttrapi.p.rapidapi.com/get-user"
    querystring = {'username': username, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

