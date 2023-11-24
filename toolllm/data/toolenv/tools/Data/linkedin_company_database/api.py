import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def linkedin_company_employee_count(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API endpoint allows you to collect company employee count on LinkedIn."
    query: Internal Linkedin ID of the target company (e.g `1035`).
        
    """
    url = f"https://linkedin-company-database.p.rapidapi.com/v2/linkedin/company/employee_count"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "linkedin-company-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def linkedin_company_info(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API endpoint allows you to get data from LinkedIn Company Page."
    query: Internal Linkedin ID or username of the target company (e.g `https://www.linkedin.com/company/microsoft`, `microsoft` or `1035`)
        
    """
    url = f"https://linkedin-company-database.p.rapidapi.com/v2/linkedin/company/info"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "linkedin-company-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

