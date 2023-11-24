import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def my_answer(question: str='Will I be lucky today?', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Answer for your important question..
		Think of a question or write it in a query parameter."
    
    """
    url = f"https://yes-no-maybe.p.rapidapi.com/answer"
    querystring = {}
    if question:
        querystring['question'] = question
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yes-no-maybe.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

