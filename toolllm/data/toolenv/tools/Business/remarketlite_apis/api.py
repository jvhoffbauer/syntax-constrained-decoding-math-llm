import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def getlistingsbyradius_valuation(street: str, radius: str, zip: str, state: str, city: str, orderid: str, longitude: str=None, latitude: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search listings around a point or address within the specified Radius"
    street: Street Address around which radius search needs to be performed
        radius: Radius in whcih search needs to be done
        zip: PostalCode of address around which radius search needs to be performed
        state: State of the address around which radius search needs to be performed
        city: City of the address around which radius search needs to be performed
        orderid: Alpha numeric combinations to uniquely reference an order
        longitude: Longitude of the centre point for Radius Search
        latitude: Latitude of the centre point for Radius Search
        
    """
    url = f"https://remarketlite-apis.p.rapidapi.com/mktlite/val/v2/GetListingsByRadius"
    querystring = {'Street': street, 'Radius': radius, 'Zip': zip, 'State': state, 'City': city, 'OrderId': orderid, }
    if longitude:
        querystring['Longitude'] = longitude
    if latitude:
        querystring['Latitude'] = latitude
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "remarketlite-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getlistingsbygeo_idx(zip: str, orderid: str, state: str, city: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API returns property listings by accepting various filters like Zip code, Street, City and State"
    zip: The PostalCode in which the search needs to be performed
        orderid: Alpha numeric combinations to uniquely reference an order
        state: The State in which the search needs to be performed
        city: The City in which the search needs to be performed
        
    """
    url = f"https://remarketlite-apis.p.rapidapi.com/mktlite/idx/v2/GetListingsByGeo"
    querystring = {'Zip': zip, 'OrderId': orderid, 'State': state, 'City': city, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "remarketlite-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getlistingsbyradius_idx(state: str, street: str, zip: str, radius: str, orderid: str, city: str, latitude: str=None, longitude: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search listings around a point or address within the specified Radius"
    state: State of the address around which radius search needs to be performed
        street: Street Address around which radius search needs to be performed
        zip: PostalCode of address around which radius search needs to be performed
        radius: Radius in whcih search needs to be done
        orderid: Alpha numeric combinations to uniquely reference an order
        city: City of the address around which radius search needs to be performed
        latitude: Latitude of the centre point for Radius Search
        longitude: Longitude of the centre point for Radius Search
        
    """
    url = f"https://remarketlite-apis.p.rapidapi.com/mktlite/idx/v2/GetListingsByRadius"
    querystring = {'State': state, 'Street': street, 'Zip': zip, 'Radius': radius, 'OrderId': orderid, 'City': city, }
    if latitude:
        querystring['Latitude'] = latitude
    if longitude:
        querystring['Longitude'] = longitude
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "remarketlite-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getlistingsbygeo_valuation(orderid: str, state: str, city: str, zip: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API returns property listings by accepting various filters like Zip code, Street, City and State"
    orderid: Alpha numeric combinations to uniquely reference an order
        state: The State in which the search needs to be performed
        city: The City in which the search needs to be performed
        zip: The PostalCode in which the search needs to be performed
        
    """
    url = f"https://remarketlite-apis.p.rapidapi.com/mktlite/val/v2/GetListingsByGeo"
    querystring = {'OrderId': orderid, 'State': state, 'City': city, 'Zip': zip, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "remarketlite-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

