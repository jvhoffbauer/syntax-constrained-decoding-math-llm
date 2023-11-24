import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def video_and_recommendations(videoid: str, geo: str='GB', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns details about a video and the first page or recommendations.
		Pass the returned `pagination` of this endpoint into the "Recommended videos (w/ pagination)" endpoint to obtain the next recommendations."
    
    """
    url = f"https://fastytapi.p.rapidapi.com/ytapi/video"
    querystring = {'videoId': videoid, }
    if geo:
        querystring['geo'] = geo
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fastytapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def channel_s_videos_streams_shorts_ids_w_pagination(videostype: str, channelid: str, geo: str='GB', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the list of videos/streams(a.k.a. lives)/shorts ids with some basic information for each.
		
		Pagination is possible, which allows to retrieve all videos/streams/shorts of a channel with several subsequent requests. For this, provide the `pagination` received in the previous request to this endpoint.
		
		Results are returned ordered by upload date, from latest to oldest."
    
    """
    url = f"https://fastytapi.p.rapidapi.com/ytapi/videoIds"
    querystring = {'videosType': videostype, 'channelId': channelid, }
    if geo:
        querystring['geo'] = geo
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fastytapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def video_recommendations_w_pagination(videoid: str, pagination: str=None, geo: str='GB', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return video recommendations given a videoId."
    
    """
    url = f"https://fastytapi.p.rapidapi.com/ytapi/videoRecommendations"
    querystring = {'videoId': videoid, }
    if pagination:
        querystring['pagination'] = pagination
    if geo:
        querystring['geo'] = geo
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fastytapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_channel(q: str, geo: str='GB', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns list of channel when searching YouTube for the provided query."
    
    """
    url = f"https://fastytapi.p.rapidapi.com/ytapi/searchChannel"
    querystring = {'q': q, }
    if geo:
        querystring['geo'] = geo
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fastytapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def recommended_channels(channelid: str, geo: str='GB', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a list of recommended channels for the provided channel.
		
		Note: this endpoint requires some heavier computations, response time might take ~5 seconds."
    
    """
    url = f"https://fastytapi.p.rapidapi.com/ytapi/channelRecommendations"
    querystring = {'channelId': channelid, }
    if geo:
        querystring['geo'] = geo
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fastytapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def channel(channelid: str, geo: str='GB', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns channel-related information."
    channelid: 24-characters-long channel id
        
    """
    url = f"https://fastytapi.p.rapidapi.com/ytapi/channel"
    querystring = {'channelId': channelid, }
    if geo:
        querystring['geo'] = geo
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fastytapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

