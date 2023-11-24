import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_coupons_endpoint(sort: str='-id', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "- This Endpoint provides daily AI analyzed Betting coupons with high win rate.
		- To load all tips organized in Ascending order pass parameter sort with value "-id"."
    
    """
    url = f"https://daily-betting-tips.p.rapidapi.com/daily-betting-tip-api/items/daily_betting_coupons"
    querystring = {}
    if sort:
        querystring['sort'] = sort
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "daily-betting-tips.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_predictions_by_date(q: str, sort: str='-id', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Endpoint is used to load Betting Tips from API the tips, this returns only tips for a given date passed as parameter.
		To load tips for a given date organised in Ascending order pass parameter sort with value "-id".
		The date format for a given date should be "dd.MM.yyyy", else response from API will be empty."
    
    """
    url = f"https://daily-betting-tips.p.rapidapi.com/daily-betting-tip-api/items/daily_betting_tips"
    querystring = {'q': q, }
    if sort:
        querystring['sort'] = sort
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "daily-betting-tips.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_predictions(sort: str='-id', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Endpoint is used to load all Betting Tips from API the tips are organised into multiple coupons.
		To load all tips organised in Ascending order pass parameter sort with value "-id"."
    
    """
    url = f"https://daily-betting-tips.p.rapidapi.com/daily-betting-tip-api/items/daily_betting_tips"
    querystring = {}
    if sort:
        querystring['sort'] = sort
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "daily-betting-tips.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_predictions_performance_statistics(q: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Endpoint is used to check the predictions performance for a given date.
		The date format for a given date should be "dd.MM.yyyy", else response from API will be empty."
    
    """
    url = f"https://daily-betting-tips.p.rapidapi.com/daily-betting-tip-api/items/daily_bets_stats"
    querystring = {'q': q, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "daily-betting-tips.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

