import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_sex_offenders(radius: str, lat: str, lng: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Params:
		@lat: latitude
		@lng: longitude
		@radius: search radius in Miles (Mi), e.g. radius = 0.2 means the API will search for sex offenders within 0.2 miles of the given lat and lng
		
		Response:
		@offenders: List of Offender Object; If no offenders are found, it will return empty list `offenders: []`.
		
		Extensive database of National Registered Sex Offenders API for the United States. This API covers 750k+ offender records, 1M+ crime records, 19k+ cities, and all 50 states. Supports lat/lng search with radius."
    
    """
    url = f"https://sex-offenders.p.rapidapi.com/sexoffender"
    querystring = {'radius': radius, 'lat': lat, 'lng': lng, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sex-offenders.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

