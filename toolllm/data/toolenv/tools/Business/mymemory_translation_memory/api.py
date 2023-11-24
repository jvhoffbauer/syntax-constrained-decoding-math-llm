import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_translations(langpair: str, q: str, onlyprivate: str='0', mt: str='1', de: str='a@b.c', key: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API gets a list of translation from the translation memory ranked by quality and similarity (what we call match). MyMemory will check if a sentence has been already translated in the private TM specified. If we don't find it in the private TM of the translator, we search it in the public TMs (shared among all the translators). Again, if we don't have this translation we ask MT providers to generate it.  In order to get the best from MyMemory, it is highly recommended to use different keys for each translators and also different keys for different topics (as a real Translation Memory)."
    langpair: The language pair. Two ISO-631 language codes, separated by |.
MyMemory support over 80 languages but some combinations may contains no data. Nepali into Vietnamese?
        q: the text you want to translate. Normally a sentence.
        onlyprivate: If a key has been specified, only private matches will be returned. 0 (disabled: default) | 1 (enabled)
        mt: Enables MT in results: 0 (disabled) | 1 (enabled: default)
        de: A valid email (recommended for CAT tools and high volume usage)
        key: Gives access to private memories and customized API limits
        
    """
    url = f"https://translated-mymemory---translation-memory.p.rapidapi.com/get"
    querystring = {'langpair': langpair, 'q': q, }
    if onlyprivate:
        querystring['onlyprivate'] = onlyprivate
    if mt:
        querystring['mt'] = mt
    if de:
        querystring['de'] = de
    if key:
        querystring['key'] = key
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def create_key(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "MyMemory provides a specific API to create a new private TM key. Such key can be then used in the API call to identify a private TM or to privately contribute to a TM. Every contribution that has been created with a private TM key will be only shown if the same private TM key is used in the GET call; no other users will see private contributions without the right private TM key."
    
    """
    url = f"https://translated-mymemory---translation-memory.p.rapidapi.com/createkey"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def set_contribution(seg: str, tra: str, langpair: str, key: str='ce1hG0w.8a8Xs', de: str='a@b.c', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The SET api is used to save a contribution. You can either save a contribution privately with your private TM key or add it to the public collaborative TM."
    seg: The source segment
        tra: The translation of the source segment
        langpair: Source and language pair, separated by the | symbol. Use ISO standard names or RFC3066
        key: Gives access to private memories and customized API limits
        de: A valid email (recommended for CAT tools and high volume usage)
        
    """
    url = f"https://translated-mymemory---translation-memory.p.rapidapi.com/set"
    querystring = {'seg': seg, 'tra': tra, 'langpair': langpair, }
    if key:
        querystring['key'] = key
    if de:
        querystring['de'] = de
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

