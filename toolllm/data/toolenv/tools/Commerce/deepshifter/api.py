import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def wallet_balance(walletaddress: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This function returns the current wallet balance for a given address. The value returned is represented in ETH so to get the raw value multiply the returned value by 18."
    
    """
    url = f"https://deepshifter.p.rapidapi.com/walletBalance/{walletaddress}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "deepshifter.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def current_block(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This function returns the current block number for the ethereal mainnet."
    
    """
    url = f"https://deepshifter.p.rapidapi.com/blockNumber"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "deepshifter.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def gas_price(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This returns the current average ethereal network gas price."
    
    """
    url = f"https://deepshifter.p.rapidapi.com/gasPrice"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "deepshifter.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def uniswap_quote(fee: str, amountin: str, sqrtpricelimitx96: str, tokenout: str, tokenin: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Send the contract address of the token you want to swap and the contract address of the token you want to receive and get a live quote directly from the Uniswap V2 and V3 pools."
    
    """
    url = f"https://deepshifter.p.rapidapi.com/{tokenin}/{tokenout}/{fee}/{sqrtpricelimitx96}/{amountin}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "deepshifter.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

