import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def getpropertydetails(streetaddress: str, orderid: str, city: str, postalcode: str, state: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the Public Record Details of the given property"
    streetaddress: Street address for PropertySearch
        orderid: Alpha numeric combinations to uniquely reference an order
        city: City of the address to be searched
        postalcode: PostalCode of the address to be searched
        state: State of the address to be searched
        
    """
    url = f"https://public-record.p.rapidapi.com/pubrec/assessor/v1/GetPropertyDetails"
    querystring = {'StreetAddress': streetaddress, 'OrderId': orderid, 'City': city, 'PostalCode': postalcode, 'State': state, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "public-record.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

