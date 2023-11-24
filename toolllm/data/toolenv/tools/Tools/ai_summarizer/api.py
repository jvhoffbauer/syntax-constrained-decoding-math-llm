import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def summarizer(text: str, num_sentences: int=2, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This is an API that allows you to summarize a given text using OpenAI's services. The API takes two main parameters, "text" and "num_sentences", and returns a summarized version of the input text."
    
    """
    url = f"https://ai-summarizer.p.rapidapi.com/"
    querystring = {'text': text, }
    if num_sentences:
        querystring['num_sentences'] = num_sentences
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ai-summarizer.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

