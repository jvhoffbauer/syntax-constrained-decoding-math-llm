import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def ip_location_by_ipv4_ipv6_ip_address(ip: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Free IP Geo Location API which provide 100% accurate geo location information of any IPv4, IPv6 IP address or Domain name like its city latitude, longitude, zipcode, state/province, country, country codes, country flag, currency, dialing code. timezone, total number of cities & states/province in country, continent code, continent name and many more details in JSON format. You can also test our API online by this IP lookup tool: https://ipworld.info/iplocator"
    ip: any IPv4 IP address you can put here
        apikey: API key which you can get it free after signup here https://ipworld.info/signup
        
    """
    url = f"https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"
    querystring = {'ip': ip, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ip_location_by_domain_name(ip: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Free IP Geo Location API which provide 100% accurate complete information of any IP address or Domain name with its city latitude, longitude, zipcode, state/province, country, country codes, country flag, currency, dialing code. timezone, total number of cities & states/province in country, continent code, continent name and many more details in JSON format. You can also test our API online by this IP lookup tool: https://ipworld.info/iplocator"
    ip: You can insert any domain name 
        apikey: API key which you can get it free after sign up here https://ipworld.info/signup
        
    """
    url = f"https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"
    querystring = {'ip': ip, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

