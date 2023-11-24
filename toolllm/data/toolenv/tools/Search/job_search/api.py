import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_jobs(agent: str, ip: str, l: str, q: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search jobs by input value"
    
    """
    url = f"https://job-search6.p.rapidapi.com/api/v1/search/jobs"
    querystring = {'agent': agent, 'ip': ip, 'l': l, 'q': q, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "job-search6.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

