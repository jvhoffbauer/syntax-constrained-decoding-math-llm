import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def listing_subscriptions(hub_mode: str, page: int=1, by_page: int=20, search: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This call will allow you to retrieve subscriptions on your account. This call allows you to retrieve subscriptions on your account. You can also use the search parameter to find subscriptions to specific feeds."
    page: If there are more than 20 matching subscriptions, you may want to paginate over them. First page (default) is 1.
        by_page: Number of items per page. Max is 500. Min is 1.
        search: A search query. Please see superfeedr docus for the various fields and values to use.
        
    """
    url = f"https://superfeedr-superfeedr-v1.p.rapidapi.com/"
    querystring = {'hub.mode': hub_mode, }
    if page:
        querystring['page'] = page
    if by_page:
        querystring['by_page'] = by_page
    if search:
        querystring['search'] = search
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "superfeedr-superfeedr-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieving_past_content(hub_topic: str=None, hub_callback: str=None, count: int=10, before: str=None, after: str=None, format: str=None, callback: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This call allows you to retrieve past entries from one or more feeds. Note that you need to be subscribed to the feed(s) in order to do this."
    hub_topic: The URL of the HTTP resource for which you want the past entries.
        hub_callback: The value can either be a callback with which you are subscribed to one or more feeds or a search query that should match one or more callback urls used to subscribed to several feeds. Please, use the query syntax used to search for subscriptions. In both cases, make sure there are less than 200 matching feeds.
        count: Optional number of items you want to retrieve. Current max is 50 and default is 10.
        before: The id of an entry in the feed. The response will only include entries published before this one.
        after: The id of an entry in the feed. The response will only include entries published after this one.
        format: json if you want to retrieve entries in json format (for feeds only!).
        callback: This will render the entries as a JSONP.
        
    """
    url = f"https://superfeedr-superfeedr-v1.p.rapidapi.com/"
    querystring = {}
    if hub_topic:
        querystring['hub.topic'] = hub_topic
    if hub_callback:
        querystring['hub.callback'] = hub_callback
    if count:
        querystring['count'] = count
    if before:
        querystring['before'] = before
    if after:
        querystring['after'] = after
    if format:
        querystring['format'] = format
    if callback:
        querystring['callback'] = callback
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "superfeedr-superfeedr-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

