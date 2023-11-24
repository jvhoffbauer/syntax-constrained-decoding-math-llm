import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def vat_number_check(vatnumber: str, countrycode: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint responds to the request with the data associated with the VAT number provided as a query parameter.  The request must contain two query parameters: the country code associated with the VAT number (For example: lu) and the VAT number itself (For example: 20260743)."
    
    """
    url = f"https://eu-vat-number-check-vat-check-rest-api.p.rapidapi.com/"
    querystring = {'vatnumber': vatnumber, 'countrycode': countrycode, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "eu-vat-number-check-vat-check-rest-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

