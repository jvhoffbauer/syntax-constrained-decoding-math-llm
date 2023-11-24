import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search(query: str, aspect_ratio: str=None, usage_rights: str=None, type: str=None, safe_search: bool=None, color: str=None, time: str=None, file_type: str=None, region: str='us', country: str=None, size: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get real-time image search results from across the web. Supports all Google Images search filters."
    query: Search query / keyword.
        aspect_ratio: Find images with a specific aspect ratio.

**Allowed values:** *tall, square, wide, panoramic*
        usage_rights: Find images with specific usage rights / license / copyright.

**Allowed values:** *creative_commons, commercial*
        type: Find images of a specific type.

**Allowed values:** *face, photo, clipart, lineart, animated*
        color: Find images with a specific dominant color.

**Allowed values:** *red, orange, yellow, green, teal, blue, purple, pink, white, gray, black, brown, full, transparent, grayscale*
        time: Find images last updated in a specific time range.

**Allowed values:** *day, week, month, year*
        file_type: Find images of a specific format / file type.

**Allowed values:** *jpg, jpeg, png, gif, svg, webp, ico, raw*
        region: The country / region from which to make the query.

**Allowed values:** 2-letter country code, see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
**Default:** us.
        country: Find images published in a specific country / region.

**Allowed values:** 2-letter country code, see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        size: Find images of a specific size.

**Allowed values:** *large, medium, icon, 400x300+, 640x480+, 800x600+, 1024x768+, 2mp+, 4mp+, 6mp+, 8mp+, 10mp+, 12mp+, 15mp+, 20mp+, 40mp+, 70mp+*
        
    """
    url = f"https://real-time-image-search.p.rapidapi.com/search"
    querystring = {'query': query, }
    if aspect_ratio:
        querystring['aspect_ratio'] = aspect_ratio
    if usage_rights:
        querystring['usage_rights'] = usage_rights
    if type:
        querystring['type'] = type
    if safe_search:
        querystring['safe_search'] = safe_search
    if color:
        querystring['color'] = color
    if time:
        querystring['time'] = time
    if file_type:
        querystring['file_type'] = file_type
    if region:
        querystring['region'] = region
    if country:
        querystring['country'] = country
    if size:
        querystring['size'] = size
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "real-time-image-search.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

