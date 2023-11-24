import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def fetch_events(c: str, json: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Fetches a list of events in either JSON or iCalendar format for the selected calendar"
    
    """
    url = f"https://calendars.p.rapidapi.com/ical_fetch"
    querystring = {'c': c, }
    if json:
        querystring['json'] = json
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "calendars.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

