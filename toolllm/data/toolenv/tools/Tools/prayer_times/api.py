import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def prayer_times_by_city(country: str, city: str, method: int=None, school: int=None, latitudeadjustmentmethod: int=None, state: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Prayer Times for a given day by city and country"
    country: A country name or ISO 2 digit aplha code, like 'US' or 'United States of America'
        city: A city name, like Denver
        method: Any of the prayer time calculation methods specified on https://aladhan.com/calculation-methods
        school: 1 for Hanfi. 0 for all others, including, Shafi, Hanbali, etc.
        latitudeadjustmentmethod: Method for adjusting times higher latitudes - for instance, if you are checking timings in the UK or Sweden. 1 - Middle of the Night 2 - One Seventh 3 - Angle Based
        state: A US state name or 2 letter abbreviation, like 'Colorado' or 'CO'
        
    """
    url = f"https://aladhan.p.rapidapi.com/timingsByCity"
    querystring = {'country': country, 'city': city, }
    if method:
        querystring['method'] = method
    if school:
        querystring['school'] = school
    if latitudeadjustmentmethod:
        querystring['latitudeAdjustmentMethod'] = latitudeadjustmentmethod
    if state:
        querystring['state'] = state
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "aladhan.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def prayer_times_calendar_by_city(city: str, month: int, year: int, country: str, method: int=None, school: int=None, latitudeadjustmentmethod: int=None, state: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a prayer times calendar for a given month, year and city"
    city: Name of a city. Example: Denver
        month: Month number - 1 to 12
        year: 4 digit value for the year. Example: 2016
        country: Name or ISO 2 letter alpha country code. Example: 'US' or 'United States of America'
        method: Any of the prayer time calculation methods specified on https://aladhan.com/calculation-methods
        school: 1 for Hanfi. 0 for all others, including, Shafi, Hanbali, etc.
        latitudeadjustmentmethod: Method for adjusting times higher latitudes - for instance, if you are checking timings in the UK or Sweden. 1 - Middle of the Night 2 - One Seventh 3 - Angle Based
        state: US state name or abbreviation. Example: 'Colorado' or 'CO'
        
    """
    url = f"https://aladhan.p.rapidapi.com/calendarByCity"
    querystring = {'city': city, 'month': month, 'year': year, 'country': country, }
    if method:
        querystring['method'] = method
    if school:
        querystring['school'] = school
    if latitudeadjustmentmethod:
        querystring['latitudeAdjustmentMethod'] = latitudeadjustmentmethod
    if state:
        querystring['state'] = state
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "aladhan.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def prayer_times_by_address(address: str, method: str=None, school: int=None, latitudeadjustmentmethod: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get prayer times by address"
    method: Any of the prayer time calculation methods specified on https://aladhan.com/calculation-methods
        school: 1 for Hanfi. 0 for all others, including, Shafi, Hanbali, etc.
        latitudeadjustmentmethod: Method for adjusting times higher latitudes - for instance, if you are checking timings in the UK or Sweden. 1 - Middle of the Night 2 - One Seventh 3 - Angle Based
        
    """
    url = f"https://aladhan.p.rapidapi.com/timingsByAddress"
    querystring = {'address': address, }
    if method:
        querystring['method'] = method
    if school:
        querystring['school'] = school
    if latitudeadjustmentmethod:
        querystring['latitudeAdjustmentMethod'] = latitudeadjustmentmethod
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "aladhan.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def calendar_by_address(address: str, year: int, month: int, method: int=None, school: int=None, latitudeadjustmentmethod: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a prayer times calendar for a month by address"
    year: 4 digit year - example 2017
        month: 2 digit month, example 03 for March
        method: Any of the prayer time calculation methods specified on https://aladhan.com/calculation-methods
        school: 1 for Hanfi. 0 for all others, including, Shafi, Hanbali, etc.
        latitudeadjustmentmethod: Method for adjusting times higher latitudes - for instance, if you are checking timings in the UK or Sweden. 1 - Middle of the Night 2 - One Seventh 3 - Angle Based
        
    """
    url = f"https://aladhan.p.rapidapi.com/calendarByAddress"
    querystring = {'address': address, 'year': year, 'month': month, }
    if method:
        querystring['method'] = method
    if school:
        querystring['school'] = school
    if latitudeadjustmentmethod:
        querystring['latitudeAdjustmentMethod'] = latitudeadjustmentmethod
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "aladhan.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

