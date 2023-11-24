import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def figlet(text: str, style: str='slant', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Create a ASCII art from a given text"
    text: String to convert to ASCII art
        style: Style of the figlet text you want. Pick one from the list returned from /figlet/list_styles. Otherwise a random style will be chosen.
        
    """
    url = f"https://ascii.p.rapidapi.com/figlet"
    querystring = {'text': text, }
    if style:
        querystring['style'] = style
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ascii.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_figlet_styles(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List the available figlet styles"
    
    """
    url = f"https://ascii.p.rapidapi.com/figlet/list_styles"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ascii.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def cowsay(text: str, style: str='skull', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Make an ASCII cow say things"
    text: Text to put in cow's mouth
        style: Cow style you want to use.
        
    """
    url = f"https://ascii.p.rapidapi.com/cowsay"
    querystring = {'text': text, }
    if style:
        querystring['style'] = style
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ascii.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_cowsay_styles(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List available cow styles"
    
    """
    url = f"https://ascii.p.rapidapi.com/cowsay/list_styles"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ascii.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

