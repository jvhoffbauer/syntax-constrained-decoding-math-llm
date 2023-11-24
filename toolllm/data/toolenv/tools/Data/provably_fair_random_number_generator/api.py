import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def welcome(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "."
    
    """
    url = f"https://provably-fair-random-number-generator.p.rapidapi.com/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "provably-fair-random-number-generator.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def revealandresetserverseed(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "."
    
    """
    url = f"https://provably-fair-random-number-generator.p.rapidapi.com/reset"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "provably-fair-random-number-generator.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getresult(clientseed: str, is_id: str, generatedresults: str, itemoptions: str='[]', deckcounter: int=None, outofx: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a Provably fair result of multiple types | PercentileResult - returns Double - No optional params | AnyResult - returns Double - Required outOfX (maximum result) | CardDeck - returns List of cards - Required deckCount (amount of decks to generate and shuffle) | RandomShuffle - returns List - Required itemOptions | RandomSelector - return Object - Required itemOptions"
    
    """
    url = f"https://provably-fair-random-number-generator.p.rapidapi.com/result"
    querystring = {'clientSeed': clientseed, 'id': is_id, 'generatedResults': generatedresults, }
    if itemoptions:
        querystring['itemOptions'] = itemoptions
    if deckcounter:
        querystring['deckCounter'] = deckcounter
    if outofx:
        querystring['outOfX'] = outofx
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "provably-fair-random-number-generator.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def viewwithblockedseed(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "."
    
    """
    url = f"https://provably-fair-random-number-generator.p.rapidapi.com/view"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "provably-fair-random-number-generator.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def makefreshaccount(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "."
    
    """
    url = f"https://provably-fair-random-number-generator.p.rapidapi.com/new"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "provably-fair-random-number-generator.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def verifyresult(generatedresults: str, nonce: int, serverseed: str, clientseed: str, itemoptions: str='[]', outofx: int=None, deckcounter: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "."
    
    """
    url = f"https://provably-fair-random-number-generator.p.rapidapi.com/verify"
    querystring = {'generatedResults': generatedresults, 'nonce': nonce, 'serverSeed': serverseed, 'clientSeed': clientseed, }
    if itemoptions:
        querystring['itemOptions'] = itemoptions
    if outofx:
        querystring['outOfX'] = outofx
    if deckcounter:
        querystring['deckCounter'] = deckcounter
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "provably-fair-random-number-generator.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

