import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def generates_captions(imageurl: str, usehashtags: bool=None, limit: int=3, useemojis: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Generates descriptive captions for a given image. By default, the generated captions exclude emojis or hashtags, and a maximum of three captions are returned."
    imageurl: Url of the image
        usehashtags: If true, hashtags will be added to generate captions.
        limit: Number of captions. Must be <=5.
        useemojis: If true, emojis will be added to generate captions.
        
    """
    url = f"https://image-caption-generator2.p.rapidapi.com/v2/captions"
    querystring = {'imageUrl': imageurl, }
    if usehashtags:
        querystring['useHashtags'] = usehashtags
    if limit:
        querystring['limit'] = limit
    if useemojis:
        querystring['useEmojis'] = useemojis
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "image-caption-generator2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

