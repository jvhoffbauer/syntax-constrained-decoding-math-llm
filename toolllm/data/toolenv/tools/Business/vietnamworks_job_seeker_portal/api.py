import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def job_search(page_number: int=None, job_title: str='job search query', job_location: str='cities', job_category: str='job search categories', job_level: int=None, job_salary: int=None, job_benefit: str='benefit types', page_size: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Job Search"
    job_location: (Maximum is 3) list of city ids which can be found in https://api-staging.vietnamworks.com/general/configuration/
        job_category: (Maximum is 3) list of industry ids which can be found in https://api-staging.vietnamworks.com/general/configuration/
        job_benefit: (Maximum is 3) list of industry ids which can be found in https://api-staging.vietnamworks.com/general/configuration/
        
    """
    url = f"https://chrisshayan-vietnamworks-job-seeker-portal-v1.p.rapidapi.com/jobs/search"
    querystring = {}
    if page_number:
        querystring['page_number'] = page_number
    if job_title:
        querystring['job_title'] = job_title
    if job_location:
        querystring['job_location'] = job_location
    if job_category:
        querystring['job_category'] = job_category
    if job_level:
        querystring['job_level'] = job_level
    if job_salary:
        querystring['job_salary'] = job_salary
    if job_benefit:
        querystring['job_benefit'] = job_benefit
    if page_size:
        querystring['page_size'] = page_size
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrisshayan-vietnamworks-job-seeker-portal-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def general_configuration(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Access to the metadata of our system"
    
    """
    url = f"https://chrisshayan-vietnamworks-job-seeker-portal-v1.p.rapidapi.com/general/configuration/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "chrisshayan-vietnamworks-job-seeker-portal-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

