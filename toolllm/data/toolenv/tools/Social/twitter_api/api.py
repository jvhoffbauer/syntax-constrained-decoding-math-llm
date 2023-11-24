import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_user_s_latest_tweets_by_screenname(screenname: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint gets lates user's tweets by it's screenname."
    
    """
    url = f"https://twitter-api45.p.rapidapi.com/timeline.php"
    querystring = {'screenname': screenname, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def tweet_info_by_the_id(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "With this endpoint you can get tweet info by it's id."
    
    """
    url = f"https://twitter-api45.p.rapidapi.com/tweet.php"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_user_information_by_the_twitter_screenname(screenname: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this method you can get information about user by the screenname. 
		
		Built with the scraper by scraper.tech"
    
    """
    url = f"https://twitter-api45.p.rapidapi.com/screenname.php"
    querystring = {'screenname': screenname, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "twitter-api45.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

