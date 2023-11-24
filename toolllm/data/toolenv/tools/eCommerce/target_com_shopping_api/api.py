import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def product_search(store_id: str, keyword: str, offset: str='0', count: str='25', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the list of products based on keyword."
    count: maximum 25
        
    """
    url = f"https://target-com-shopping-api.p.rapidapi.com/product_search"
    querystring = {'store_id': store_id, 'keyword': keyword, }
    if offset:
        querystring['offset'] = offset
    if count:
        querystring['count'] = count
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def product_details(store_id: str, tcin: str, longitude: str='-122.200', latitude: str='37.820', zip: str='94611', state: str='CA', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns detailed product information.
		Including:
		```
		product variants (with different dimension like size, color and etc.
		ratings and reviews
		item images/videos
		price
		promotion
		child products
		```"
    store_id: The id of the store which product details data is being retrieved from. (optional)
Value comes from nearby store API.
        tcin: Target product id.
Value comes from product search API.
        longitude: User's longitude information. (optional)
        latitude: User's latitude information. (optional)
        zip: User's zipcode. (optional)
        state: State code of user's location. (optional)
        
    """
    url = f"https://target-com-shopping-api.p.rapidapi.com/product_details"
    querystring = {'store_id': store_id, 'tcin': tcin, }
    if longitude:
        querystring['longitude'] = longitude
    if latitude:
        querystring['latitude'] = latitude
    if zip:
        querystring['zip'] = zip
    if state:
        querystring['state'] = state
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def nearby_stores(place: str, within: str='100', limit: str='20', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the list of stores near to specified ZIP code."
    within: Radius of searching distance in miles
        
    """
    url = f"https://target-com-shopping-api.p.rapidapi.com/nearby_stores"
    querystring = {'place': place, }
    if within:
        querystring['within'] = within
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def product_fulfillment(tcin: str, zip: str='94611', state: str='CA', longitude: str='-122.200', store_id: str='3330', latitude: str='37.820', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns product fulfillment information."
    tcin: Target product id.
Value comes from product search API.

        zip: The zipcode of user's search location.
(optional)
        state: State code where is user is located at. (optional)
        longitude: User's longitude Information (optional)
        store_id: The id of the Target store from which the fulfillment information is being retrieved.
Value comes from nearby stores api.
(optional)
        latitude: User's longitude Information (optional)
        
    """
    url = f"https://target-com-shopping-api.p.rapidapi.com/product_fulfillment"
    querystring = {'tcin': tcin, }
    if zip:
        querystring['zip'] = zip
    if state:
        querystring['state'] = state
    if longitude:
        querystring['longitude'] = longitude
    if store_id:
        querystring['store_id'] = store_id
    if latitude:
        querystring['latitude'] = latitude
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_autocomplete(q: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Product autocompletion based on search keyword."
    
    """
    url = f"https://target-com-shopping-api.p.rapidapi.com/autocomplete"
    querystring = {'q': q, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "target-com-shopping-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

