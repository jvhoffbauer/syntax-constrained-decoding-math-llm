import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_all_available_face_parts(face_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get IDs of parts currently applied to the face and available options. Parts may vary from face to face based on recognised attributes."
    face_id: Face ID you got from /generate endpoint
        
    """
    url = f"https://mirror-ai.p.rapidapi.com/get_all_parts"
    querystring = {'face_id': face_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mirror-ai.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_face_attributes(face_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get estimated face attributes such as age and gender."
    face_id: Face ID obtained from Generate endpoint
        
    """
    url = f"https://mirror-ai.p.rapidapi.com/attrs"
    querystring = {'face_id': face_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mirror-ai.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_sticker(sticker: str, face_id: str, loc: str='en', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get URL for a sticker for given face. Supported stickers can be explored at https://mirrorai.github.io
		
		Note that sticker style must match face style used while generating the face.
		
		Currently there are two styles availible:
		* kenga (aka "line" in MirrorAI app)
		* anime"
    
    """
    url = f"https://mirror-ai.p.rapidapi.com/sticker"
    querystring = {'sticker': sticker, 'face_id': face_id, }
    if loc:
        querystring['loc'] = loc
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mirror-ai.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_token(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a token for making further requests. Faces can be managed only with tokens they were generated with."
    
    """
    url = f"https://mirror-ai.p.rapidapi.com/token"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "mirror-ai.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

