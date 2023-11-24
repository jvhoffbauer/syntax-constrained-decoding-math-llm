import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def validatephone(countrycode: str, phone: str, key: str, format: str='JSON', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This method can be used as an extra-layer of your system for validating phone numbers."
    countrycode: The ISO 3166-1 alpha-2 format of the country code of the phone number.
        phone: The Phone Number you want to validate.
        key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
        format: Sets the format of the API response. JSON is the default format.
        
    """
    url = f"https://greip.p.rapidapi.com/validatePhone"
    querystring = {'countryCode': countrycode, 'phone': phone, 'key': key, }
    if format:
        querystring['format'] = format
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "greip.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def iplookup(ip: str, key: str, format: str='XML', params: str='currency', lang: str='AR', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the geolocation data of a specific IP Address."
    ip: The IP Address you want to lookup.
        key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
        format: Sets the format of the API response. JSON is the default format.
        params: The modules you want to use of the request. It's a CSV (Comma Separated Values)
        lang: Used to inform the API to retrieve the response in your native language.
        
    """
    url = f"https://greip.p.rapidapi.com/IPLookup"
    querystring = {'ip': ip, 'key': key, }
    if format:
        querystring['format'] = format
    if params:
        querystring['params'] = params
    if lang:
        querystring['lang'] = lang
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "greip.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def country(countrycode: str, key: str, lang: str='AR', format: str='XML', params: str='language', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Country endpoint: Returns the information of a specific country by passing the `countrCode`."
    countrycode: The Country Code of the country you want to fetch it's data.
        key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
        lang: Used to inform the API to retrieve the response in your native language.
        format: Sets the format of the API response. JSON is the default format.
        params: The modules you want to use of the request. It's a CSV (Comma Separated Values)
        
    """
    url = f"https://greip.p.rapidapi.com/Country"
    querystring = {'CountryCode': countrycode, 'key': key, }
    if lang:
        querystring['lang'] = lang
    if format:
        querystring['format'] = format
    if params:
        querystring['params'] = params
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "greip.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def validateemail(email: str, key: str, format: str='JSON', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This method can be used as an extra-layer of your system for validating email addresses."
    email: The Email Address you want to validate.
        key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
        format: Sets the format of the API response. JSON is the default format.
        
    """
    url = f"https://greip.p.rapidapi.com/validateEmail"
    querystring = {'email': email, 'key': key, }
    if format:
        querystring['format'] = format
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "greip.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

