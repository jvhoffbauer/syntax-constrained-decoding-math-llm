import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def https_flightslogic_com_about_php(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "FlightsLogic provides Flight Booking Software, Flight Booking API to the travel agents, tour operators and travel companies worldwide."
    
    """
    url = f"https://flightslogics-flight-booking-flight-booking-software.p.rapidapi.comhttps://flightslogic.com/about.php"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "flightslogics-flight-booking-flight-booking-software.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

