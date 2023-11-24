import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_jobs(company_id: int, geo_code: int=92000000, start: str='0', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search jobs posted on LinkedIn. This endpoint is useful for scraping job openings of a specific company on LinkedIn. 
		
		To scrape all results from each search, change the param *start* from 0 to 25, 50, ... until you see less than 25 results returned.
		
		**2 credits per call.**"
    geo_code: Use this param to target jobs in specific region/country. To search worldwide, use 92000000.
        
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/search-jobs"
    querystring = {'company_id': company_id, }
    if geo_code:
        querystring['geo_code'] = geo_code
    if start:
        querystring['start'] = start
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_profile_pdf_cv(linkedin_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the CV of a LinkedIn profile in PDF format. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-pdf-cv"
    querystring = {'linkedin_url': linkedin_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_open_to_work_status(linkedin_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Given a LinkedIn profile URL, the API will let you know if that profile is “open to work” or not. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-opentowork-status"
    querystring = {'linkedin_url': linkedin_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_profile_posts(linkedin_url: str, type: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get 50 latest posts of a person based on his/her LinkedIn profile url. **2 credits per call.**"
    type: Possible values: 

- posts: to scrape posts from tab Posts -- posts or posts reshared by the person

- comments: to scrape posts from tab Comments -- posts the person commented

- reactions: to scrape posts from tab Reactions -- posts the person reacted


        
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-posts"
    querystring = {'linkedin_url': linkedin_url, 'type': type, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_linkedin_profile_by_sales_nav_url(linkedin_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get full profile data, including experience & education history, skillset and company related details. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile-by-salesnavurl"
    querystring = {'linkedin_url': linkedin_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_company_jobs_count(company_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get number of opening jobs the company posted on LinkedIn. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-jobs-count"
    querystring = {'company_id': company_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_company_ads_count(company_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get number of ads the company posted on LinkedIn. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-ads-count"
    querystring = {'company_id': company_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_company_posts(linkedin_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get 50 latest posts from a LinkedIn company page. **2 credits per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-posts"
    querystring = {'linkedin_url': linkedin_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_company_by_domain(domain: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Find a company on LinkedIn using its web domain. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-domain"
    querystring = {'domain': domain, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_company_data_by_linkedin_url(linkedin_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Given a company’s LinkedIn URL, the API will return valuable data points in JSON format. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-linkedinurl"
    querystring = {'linkedin_url': linkedin_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_job_details(job_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Scrape the full job details, including the company basic information. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-job-details"
    querystring = {'job_url': job_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_search_results(page: str, request_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get search results. Please make sure the search is "done" before calling this endpoint."
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-search-results"
    querystring = {'page': page, 'request_id': request_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def check_search_status(request_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the status of your search using the request_id given in step 1."
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/check-search-status"
    querystring = {'request_id': request_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_linkedin_profile_data(linkedin_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get full profile data, including experience & education history, skillset and company related details. Accept all type of profile urls. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"
    querystring = {'linkedin_url': linkedin_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_profile_recent_activity_time(linkedin_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the time of the latest activity. **2 credits per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-recent-activity-time"
    querystring = {'linkedin_url': linkedin_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_company_data_by_id(company_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Given a company’s LinkedIn internal ID, the API will return valuable data points in JSON format. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-id"
    querystring = {'company_id': company_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_open_profile_status(linkedin_url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Given a LinkedIn profile URL, the API will let you know if that profile is “open profile” or not. **1 credit per call.**"
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/get-open-profile-status"
    querystring = {'linkedin_url': linkedin_url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_supported_countries(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get supported countries. Use the country codes in your "Search employees" endpoint."
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/supported-location"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_supported_industries(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get supported industries. Use the industry_id in your "Search employees" endpoint."
    
    """
    url = f"https://fresh-linkedin-profile-data.p.rapidapi.com/supported-industry"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

