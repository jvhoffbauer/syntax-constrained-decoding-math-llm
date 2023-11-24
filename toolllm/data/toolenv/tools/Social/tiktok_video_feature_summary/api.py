import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def comment_list_by_video(url: str, cursor: int=0, count: int=10, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get comment list by video"
    url: https://www.tiktok.com/@tiktok/video/7093219391759764782
or
7093219391759764782
or
https://vm.tiktok.com/ZSeQS6B5k/
        cursor: hasMore is True
        count: max 50
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/comment/list"
    querystring = {'url': url, }
    if cursor:
        querystring['cursor'] = cursor
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def register_device_information(aid: int, os: str='7.1.2', version: str='250304', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Random device information,
		Activated"
    aid: 1180
1233
1340
        os: os version
        version: version code
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/service/registerDevice"
    querystring = {'aid': aid, }
    if os:
        querystring['os'] = os
    if version:
        querystring['version'] = version
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_music_info(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get music info base on id"
    url: id or https://vm.tiktok.com/xxxxxxx
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/music/info"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_user_following_list(user_id: str, time: str='0', count: str='50', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get user following list"
    time: hasMore is True load next page
        count: max 200
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/user/following"
    querystring = {'user_id': user_id, }
    if time:
        querystring['time'] = time
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_user_follower_list(user_id: str, time: str='0', count: str='50', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get user follower list"
    time: hasMore is True load next page
        count: max 200
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/user/followers"
    querystring = {'user_id': user_id, }
    if time:
        querystring['time'] = time
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_related_video_with_keywords(keywords: str, region: str='US', sort_type: int=0, cursor: str='0', publish_time: int=0, count: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get related video  list with list"
    region: Please refer to the region list interface for details
        sort_type: 0 - Relevance
1 - Like count
3 - Date posted
        publish_time: 0 - ALL
1 - Past 24 hours
7 - This week
30 - This month
90 - Last 3 months
180 - Last 6 months
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/feed/search"
    querystring = {'keywords': keywords, }
    if region:
        querystring['region'] = region
    if sort_type:
        querystring['sort_type'] = sort_type
    if cursor:
        querystring['cursor'] = cursor
    if publish_time:
        querystring['publish_time'] = publish_time
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def region_list(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "the region list use in video search params"
    
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/region"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_users_detail_info(user_id: str='107955', unique_id: str='voyagel', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get users detail info
		unique_id or user_id is not empty"
    
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/user/info"
    querystring = {}
    if user_id:
        querystring['user_id'] = user_id
    if unique_id:
        querystring['unique_id'] = unique_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_user_favorite_videos(count: str='10', unique_id: str='voyagel', user_id: str='6741307595983946754', cursor: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get user favorite videos list"
    unique_id: voyagel or @voyagel
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/user/favorite"
    querystring = {}
    if count:
        querystring['count'] = count
    if unique_id:
        querystring['unique_id'] = unique_id
    if user_id:
        querystring['user_id'] = user_id
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_users_video(count: str='10', user_id: str='107955', unique_id: str=None, cursor: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get user post videos
		get user feed
		unique_id or user_id is not empty"
    unique_id: unique_id
tiktok or @tiktok
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/user/posts"
    querystring = {}
    if count:
        querystring['count'] = count
    if user_id:
        querystring['user_id'] = user_id
    if unique_id:
        querystring['unique_id'] = unique_id
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_users_data(keywords: str, count: int=10, cursor: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get users data list by keywords"
    keywords: users nickname
Support for fuzzy search
        count: return count
        cursor: hasMore is True, load next page
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/user/search"
    querystring = {'keywords': keywords, }
    if count:
        querystring['count'] = count
    if cursor:
        querystring['cursor'] = cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_tiktok_video_full_info(url: str, hd: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Support Tiktok & Douyin.
		Returns relevant information about querying video addresses, 
		including high-definition watermark free video addresses, 
		author information, 
		background music information, 
		views, 
		likes, 
		comments, 
		etc- List Item"
    url: Tiktok or Douyin video address
        hd: Get HD Video(High bit rate). This increases the total request time a little.
        
    """
    url = f"https://tiktok-video-feature-summary.p.rapidapi.com/"
    querystring = {'url': url, }
    if hd:
        querystring['hd'] = hd
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tiktok-video-feature-summary.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

