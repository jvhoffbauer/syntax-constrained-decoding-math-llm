import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def stories_statistics(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "After you make post request to stories route,Call this request to get all info about your stories.
		If get requests say "Stats not found please update".then Please make above post request to this api first."
    
    """
    url = f"https://instagram-statistical-analysis.p.rapidapi.com/api/stories"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-statistical-analysis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def followers_that_you_don_t_follow_back(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return list of your followers to whom you do not follow back.
		If get requests say "Stats not found please update".then Please make post request first."
    
    """
    url = f"https://instagram-statistical-analysis.p.rapidapi.com/api/followers/infb"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-statistical-analysis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def count_of_increased_and_decreased_followers(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Will return how many followers and followings are decreased and increased."
    
    """
    url = f"https://instagram-statistical-analysis.p.rapidapi.com/api/followers/statistics"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-statistical-analysis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def followings_that_don_t_follow_you_back(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Will Return list of people who do not follow you back but you follow them."
    
    """
    url = f"https://instagram-statistical-analysis.p.rapidapi.com/api/followers/nfb"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-statistical-analysis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def new_followers(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns Followers who started following you.
		If get requests say "Stats not found please update".then Please make post request first."
    
    """
    url = f"https://instagram-statistical-analysis.p.rapidapi.com/api/followers/new"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-statistical-analysis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def lost_followers(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns people who stopped following you.
		If get requests say "Stats not found please update".then Please make post request first."
    
    """
    url = f"https://instagram-statistical-analysis.p.rapidapi.com/api/followers/lost"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-statistical-analysis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def popularity_statistics_of_posts(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Will return Posts based on Popularity of posts."
    
    """
    url = f"https://instagram-statistical-analysis.p.rapidapi.com/api/posts/popular"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-statistical-analysis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_rankings_of_posts_based_on_comments(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Ranking of Instagram Posts based on Comments."
    
    """
    url = f"https://instagram-statistical-analysis.p.rapidapi.com/api/posts/ranked/comments"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-statistical-analysis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_rankings_of_posts_based_on_likes(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get likes."
    
    """
    url = f"https://instagram-statistical-analysis.p.rapidapi.com/api/posts/ranked/likes"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram-statistical-analysis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

