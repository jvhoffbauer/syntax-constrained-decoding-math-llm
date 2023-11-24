import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_stores_in_a_city(state: str, api_key: str, city: str, brand: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all stores in the city, [use endpoint /api/v1.1/cities/ to get all city names]                
		    Filter by city,state,brand_alias
		Example Payload
		 {
		    "api_key":"iopII2344_ADDDxxw1i1",
		    "city": "Los Angeles",
		    "state": "CA",
		    "brand": "taco-bell" (Optional)
		  }
		Example Response
		 [{
		    "brand_name": "Western Union",
		    "store_address": "600 West 7th St",
		    "phone_no": "(213) 896-0083"
		  },{
		    "brand_name": "Simple Mobile",
		    "store_address": "727 N Vine St",
		    "phone_no": "(323) 466-7300"
		  }]"
    
    """
    url = f"https://stores-and-brands-api.p.rapidapi.com/stores-in-city/"
    querystring = {'state': state, 'api_key': api_key, 'city': city, }
    if brand:
        querystring['brand'] = brand
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "stores-and-brands-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stores_near_me(radius: int, lat: str, long: str, api_key: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Find Stores Near Me by sending lat and long 
		    Get all stores in the city, [use endpoint /api/v1.1/cities/ to get all city names]                
		    Filter by city,state,brand_alias
		Example Payload
		 {
		    "api_key":"iopII2344_ADDDxxw1i1",
		    "lat": "12.34",
		    "long": "11.55",
		    "radius", 10 (optional in kms)
		  }
		Example Response
		 [{
		    "brand_name": "Western Union",
		    "store_address": "600 West 7th St",
		    "phone_no": "(213) 896-0083"
		  },{
		    "brand_name": "Simple Mobile",
		    "store_address": "727 N Vine St",
		    "phone_no": "(323) 466-7300"
		  }]"
    
    """
    url = f"https://stores-and-brands-api.p.rapidapi.com/stores-near-me/"
    querystring = {'radius': radius, 'lat': lat, 'long': long, 'api_key': api_key, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "stores-and-brands-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

