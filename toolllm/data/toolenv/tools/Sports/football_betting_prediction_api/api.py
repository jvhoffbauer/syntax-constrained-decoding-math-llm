import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_predictions_and_results_by_date(date: str='2023-05-18', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The 'Get Predictions and Results by Date' endpoint offers users the ability to retrieve football match predictions and results for a specific date (previous dates). Users can input their desired date in the 'date' query parameter in the format 'YYYY-MM-DD'."
    
    """
    url = f"https://football-betting-prediction-api.p.rapidapi.com/"
    querystring = {}
    if date:
        querystring['date'] = date
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "football-betting-prediction-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_predictions_for_today(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API endpoint is specifically designed to retrieve today's football match predictions. By leveraging real-time data and sophisticated predictive algorithms, it provides the latest forecasts for match outcomes happening on the current day.
		
		The 'Get Predictions for Today' endpoint delivers essential data such as predicted winner, expected goals, potential scorers, and other valuable betting information. This immediate, data-driven insight enables bettors to make informed decisions and strategies for today's matches.
		
		Easy to integrate and use, this endpoint serves as a crucial tool for any football betting platform, enhancing user engagement and betting success rate by providing accurate and timely predictions for today's football matches."
    
    """
    url = f"https://football-betting-prediction-api.p.rapidapi.com/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "football-betting-prediction-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

