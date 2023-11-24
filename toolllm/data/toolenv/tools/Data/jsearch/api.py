import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search(query: str, categories: str=None, employer: str=None, radius: int=None, company_types: str=None, num_pages: str='1', employment_types: str=None, job_requirements: str=None, date_posted: str=None, job_titles: str=None, remote_jobs_only: bool=None, page: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for jobs posted on job sites across the web."
    query: Free-form jobs search query. It is highly recommended to include job title and location as part of the query, see query examples below.

**Query examples**
- *web development in chicago*
- *marketing manager in new york via linkedin*
- *developer in germany 60306*
        categories: **[Deprecated]** Find jobs in specific categories/industries - specified as a comma (,) separated list of `categories` filter values (i.e. filter *value* field) as returned by the **Search Filters** endpoint.

**Example**: *categories=R0MxODpNYW5hZ2VtZW50,R0MwNTpBcnRGYXNoaW9uRGVzaWdu*
        employer: Find jobs posted by specific employers - specified as a comma (,) separated list of `employer` filter values (i.e. filter *value* field) as returned by the **Search Filters** endpoint.

**Example**: *employers= L2cvMTFoMTV4eHhydDpJbmZpbml0eSBDb25zdWx0aW5n,L2cvMTFmMDEzOXIxbjpDeWJlckNvZGVycw==*
        radius: Return jobs within a certain distance from location as specified as part of the query (in km).
        company_types: Find jobs posted by companies of certain types - specified as a comma (,) separated list of `company_types` filter values (i.e. filter *value* field) as returned by the **Search Filters** endpoint.

**Example**: *company_types= L2J1c2luZXNzL25haWNzMjAwNy81MjpGaW5hbmNl,L2J1c2luZXNzL25haWNzMjAwNy81MTpJbmZvcm1hdGlvbg==*
        num_pages: Number of pages to return, starting from `page`.
Allowed values: `1-20`.
Default: `1`.

 **Note**: requests for more than one page and up to 10 pages are charged x2 and requests for more than 10 pages are charged 3x.
        employment_types: Find jobs of particular employment types, specified as a comma delimited list of the following values: `FULLTIME`, `CONTRACTOR`, `PARTTIME`, `INTERN`.
        job_requirements: Find jobs with specific requirements, specified as a comma delimited list of the following values: `under_3_years_experience`, `more_than_3_years_experience`, `no_experience`, `no_degree`.
        date_posted: Find jobs posted within the time you specify.
Allowed values: `all`, `today`, `3days`, `week`,`month`.
Default: `all`.
        job_titles: Find jobs with specific job titles - specified as a comma (,) separated list of `job_titles` filter values (i.e. filter *value* field) as returned by the **Search Filters** endpoint.

**Example**: *job_titles=c2VuaW9y,YXNzb2NpYXRl*
        remote_jobs_only: Find remote jobs only (work from home).
Default: `false`.
        page: Page to return (each page includes up to 10 results).
Allowed values: `1-100`.
Default: `1`.
        
    """
    url = f"https://jsearch.p.rapidapi.com/search"
    querystring = {'query': query, }
    if categories:
        querystring['categories'] = categories
    if employer:
        querystring['employer'] = employer
    if radius:
        querystring['radius'] = radius
    if company_types:
        querystring['company_types'] = company_types
    if num_pages:
        querystring['num_pages'] = num_pages
    if employment_types:
        querystring['employment_types'] = employment_types
    if job_requirements:
        querystring['job_requirements'] = job_requirements
    if date_posted:
        querystring['date_posted'] = date_posted
    if job_titles:
        querystring['job_titles'] = job_titles
    if remote_jobs_only:
        querystring['remote_jobs_only'] = remote_jobs_only
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def job_details(job_id: str, extended_publisher_details: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all job details, including additional application options / links, employer reviews and estimated salaries for similar jobs."
    job_id: Job Id of the job for which to get details. Batching of up to 20 Job Ids is supported by separating multiple Job Ids by comma (,).

Note that each Job Id in a batch request is counted as a request for quota calculation.
        extended_publisher_details: Return additional publisher details such as website url and favicon.
        
    """
    url = f"https://jsearch.p.rapidapi.com/job-details"
    querystring = {'job_id': job_id, }
    if extended_publisher_details:
        querystring['extended_publisher_details'] = extended_publisher_details
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_filters(query: str, job_titles: str=None, radius: int=None, company_types: str=None, categories: str=None, job_requirements: str=None, remote_jobs_only: bool=None, date_posted: str=None, employers: str=None, employment_types: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Accepts all **Search** endpoint parameters (except for `page` and `num_pages`) and returns the relevant filters and their estimated result counts for later use in search or for analytics."
    query: Free-form jobs search query. It is highly recommended to include job title and location as part of the query, see query examples below.

**Query examples**
- *web development in chicago*
- *marketing manager in new york via linkedin*
- *developer in germany 60306*
        job_titles: Job title filter - specified as a comma (,) separated list of `job_titles` filter values (i.e. filter *value* field) as returned by a previous call to this endpoint.

**Example**: *job_titles=c2VuaW9y,YXNzb2NpYXRl*
        radius: Return jobs within a certain distance from location as specified as part of the query (in km).
        company_types: Company types filter - specified as a comma (,) separated list of `company_types` filter values (i.e. filter *value* field) as returned by a previous call to this endpoint.

**Example**: *company_types= L2J1c2luZXNzL25haWNzMjAwNy81MjpGaW5hbmNl,L2J1c2luZXNzL25haWNzMjAwNy81MTpJbmZvcm1hdGlvbg==*
        categories: **[Deprecated]** Categories/industries filter - specified as a comma (,) separated list of `categories` filter values (i.e. filter *value* field) as returned by a previous call to this endpoint.

**Example**: *categories=R0MxODpNYW5hZ2VtZW50,R0MwNTpBcnRGYXNoaW9uRGVzaWdu*
        job_requirements: Find jobs with specific requirements, specified as a comma delimited list of the following values: `under_3_years_experience`, `more_than_3_years_experience`, `no_experience`, `no_degree`.
        remote_jobs_only: Find remote jobs only (work from home).
Default: `false`.
        date_posted: Find jobs posted within the time you specify.
Possible values: `all`, `today`, `3days`, `week`,`month`.
Default: `all`.
        employers: Employers filter - specified as a comma (,) separated list of `employers` filter values (i.e. filter *value* field) as returned by a previous call to this endpoint.

**Example**: *employers= L2cvMTFoMTV4eHhydDpJbmZpbml0eSBDb25zdWx0aW5n,L2cvMTFmMDEzOXIxbjpDeWJlckNvZGVycw==*
        employment_types: Find jobs of particular employment types, specified as a comma delimited list of the following values: `FULLTIME`, `CONTRACTOR`, `PARTTIME`, `INTERN`.
        
    """
    url = f"https://jsearch.p.rapidapi.com/search-filters"
    querystring = {'query': query, }
    if job_titles:
        querystring['job_titles'] = job_titles
    if radius:
        querystring['radius'] = radius
    if company_types:
        querystring['company_types'] = company_types
    if categories:
        querystring['categories'] = categories
    if job_requirements:
        querystring['job_requirements'] = job_requirements
    if remote_jobs_only:
        querystring['remote_jobs_only'] = remote_jobs_only
    if date_posted:
        querystring['date_posted'] = date_posted
    if employers:
        querystring['employers'] = employers
    if employment_types:
        querystring['employment_types'] = employment_types
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def estimated_salary(location: str='New-York, NY, USA', job_title: str='NodeJS Developer', radius: int=100, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get estimated salaries for a jobs around a location"
    location: Location in which to get salary estimation.
        job_title: Job title for which to get salary estimation.
        radius: Search radius in km (measured from location).
Default: `200`.
        
    """
    url = f"https://jsearch.p.rapidapi.com/estimated-salary"
    querystring = {}
    if location:
        querystring['location'] = location
    if job_title:
        querystring['job_title'] = job_title
    if radius:
        querystring['radius'] = radius
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

