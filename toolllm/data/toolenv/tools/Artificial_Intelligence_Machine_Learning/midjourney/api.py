import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_upscaled_binary_image(image_pos: str, set_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "returns requested binary image ("image/png") from the set"
    
    """
    url = f"https://midjourney4.p.rapidapi.com/rapida/sets/{set_id}/upscale"
    querystring = {'image_pos': image_pos, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "midjourney4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_binary_image_set(set_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "returns requested binary image ("image/png"). Full image set"
    
    """
    url = f"https://midjourney4.p.rapidapi.com/rapida/sets/{set_id}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "midjourney4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_generation_status(track_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get status of the previously posted job.
		
		- outcome - if Failure, then it comes from MJ, like censorship.
		- estimated_time - in seconds. based on previous generation.
		- percent - available when actual generation started"
    
    """
    url = f"https://midjourney4.p.rapidapi.com/rapida/sets"
    querystring = {'track_id': track_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "midjourney4.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

