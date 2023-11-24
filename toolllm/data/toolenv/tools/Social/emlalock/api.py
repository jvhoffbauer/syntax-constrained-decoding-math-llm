import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def addmaximum(value: str, userid: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Request will raise your maximum duration by VALUE."
    value: Time value (in seconds or short terms).
        userid: Your UserID.
        apikey: Your API key.
        
    """
    url = f"https://emlalock.p.rapidapi.com/addmaximum"
    querystring = {'value': value, 'userid': userid, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def addmaximumrandom(to: str, is_from: str, userid: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Request will raise your maximum duration randomly between FROM and TO."
    to: Time value (in seconds or short terms).
        from: Time value (in seconds or short terms).
        userid: Your UserID.
        apikey: Your API key.
        
    """
    url = f"https://emlalock.p.rapidapi.com/addmaximumrandom"
    querystring = {'to': to, 'from': is_from, 'userid': userid, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def addminimum(userid: str, value: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Request will raise your minimum duration by VALUE."
    userid: Your UserID.
        value: Time value (in seconds or short terms).
        apikey: Your API key.
        
    """
    url = f"https://emlalock.p.rapidapi.com/addminimum"
    querystring = {'userid': userid, 'value': value, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def addminimumrandom(to: str, userid: str, is_from: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Request will raise your minimum duration randomly between FROM and TO."
    to: Time value (in seconds or short terms).
        userid: Your UserID.
        from: Time value (in seconds or short terms).
        apikey: Your API key.
        
    """
    url = f"https://emlalock.p.rapidapi.com/addminimumrandom"
    querystring = {'to': to, 'userid': userid, 'from': is_from, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def info(userid: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Request will do nothing except give you the information each API-job does."
    userid: Your UserID.
        apikey: Your API key.
        
    """
    url = f"https://emlalock.p.rapidapi.com/info"
    querystring = {'userid': userid, 'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def submaximumrandom(userid: str, apikey: str, is_from: str, to: str, holderapikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Request will lower your maximum duration randomly between FROM and TO."
    userid: Your UserID.
        apikey: Your API key.
        from: Time value (in seconds or short terms).
        to: Time value (in seconds or short terms).
        holderapikey: The API key of the holder.
        
    """
    url = f"https://emlalock.p.rapidapi.com/submaximumrandom"
    querystring = {'userid': userid, 'apikey': apikey, 'from': is_from, 'to': to, 'holderapikey': holderapikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def subrandom(to: str, apikey: str, holderapikey: str, is_from: str, userid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Request will lower your duration randomly between FROM and TO."
    to: Time value (in seconds or short terms).
        apikey: Your API key.
        holderapikey: The API key of the holder.
        from: Time value (in seconds or short terms).
        userid: Your UserID.
        
    """
    url = f"https://emlalock.p.rapidapi.com/subrandom"
    querystring = {'to': to, 'apikey': apikey, 'holderapikey': holderapikey, 'from': is_from, 'userid': userid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def subrequirement(value: int, apikey: str, userid: str, holderapikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This Request will lower your maximum duration by VALUE."
    value: Number of requirements.
        apikey: Your API key.
        userid: Your UserID.
        holderapikey: The API key of the holder.
        
    """
    url = f"https://emlalock.p.rapidapi.com/subrequirement"
    querystring = {'value': value, 'apikey': apikey, 'userid': userid, 'holderapikey': holderapikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user(userid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get information about user or yourseld"
    userid: UserID or yourself for own data (includes more data than for other users)
        
    """
    url = f"https://emlalock.p.rapidapi.com/user"
    querystring = {'userid': userid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def feed(chastitysessionid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the activity feed for a given session."
    chastitysessionid: SessionID of the chastity session
        
    """
    url = f"https://emlalock.p.rapidapi.com/feed"
    querystring = {'chastitysessionid': chastitysessionid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def session(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get your session timing information."
    
    """
    url = f"https://emlalock.p.rapidapi.com/session/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def messages(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a list of your received and send private messages."
    
    """
    url = f"https://emlalock.p.rapidapi.com/messages"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def chastity_session(chastitysessionid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get information about a chastity session by their sessionID."
    chastitysessionid: sessionID or default
        
    """
    url = f"https://emlalock.p.rapidapi.com/chastitysession"
    querystring = {'chastitysessionid': chastitysessionid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_chastity_session(userid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get information about a users session by their userID"
    userid: UserID or yourself for own data
        
    """
    url = f"https://emlalock.p.rapidapi.com/userchastitysession"
    querystring = {'userid': userid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def messages_info(messageid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get information about a specific message by messageID."
    messageid: MessageID of the message to show.
        
    """
    url = f"https://emlalock.p.rapidapi.com/messages"
    querystring = {'messageid': messageid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def keys(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List your wearers chastity sessions"
    
    """
    url = f"https://emlalock.p.rapidapi.com/keys"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "emlalock.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

