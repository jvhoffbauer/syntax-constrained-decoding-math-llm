import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def orgcode_cards(muid: str, msid: str, orgcode: str, locale: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a list of cards for the given session. User authentication is required."
    muid: User ID.
        msid: Session ID.
        orgcode: The organization associated with the request.
        locale: Language used.
        
    """
    url = f"https://test2113.p.rapidapi.com/{orgcode}/cards"
    querystring = {'muid': muid, 'msid': msid, 'locale': locale, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "test2113.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def orgcode_cardart_bins(muid: str, locale: str, orgcode: str, msid: str, bins: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns card art URLs by BINs. Different URLs can be defined for each BIN/range of BINs. User authentication is not required."
    muid: User ID.
        locale: Language used.
        orgcode: The organization associated with the request.
        msid: Session ID.
        bins: One or more six-digit bin separated by commas.
        
    """
    url = f"https://test2113.p.rapidapi.com/{orgcode}/cardart/{bins}"
    querystring = {'muid': muid, 'locale': locale, 'msid': msid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "test2113.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def orgcode_cards_cardid(cardid: str, muid: str, msid: str, orgcode: str, locale: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns card information for a given card ID. User authentication is required."
    cardid: The card ID.
        muid: User ID.
        msid: Session ID.
        orgcode: The organization associated with the request.
        locale: Language used.
        
    """
    url = f"https://test2113.p.rapidapi.com/{orgcode}/cards/{cardid}"
    querystring = {'muid': muid, 'msid': msid, 'locale': locale, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "test2113.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def orgcode_accounts_accountid_cards(locale: str, msid: str, orgcode: str, muid: str, accountid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a list of cards belonging to a specific account. User authentication is required."
    locale: Language used.
        msid: Session ID.
        orgcode: The organization associated with the request.
        muid: User ID.
        accountid: The parent account ID.
        
    """
    url = f"https://test2113.p.rapidapi.com/{orgcode}/accounts/{accountid}/cards"
    querystring = {'locale': locale, 'msid': msid, 'muid': muid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "test2113.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

