import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def getbookdetail(is_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Detail of book by Book ID"
    
    """
    url = f"https://reading-home-apis.p.rapidapi.com/readinghome/api/get_book_detail_rapiapi"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "reading-home-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getbooksbytitlesearch(search: str, page: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Paginated List of Books on Title Searched"
    
    """
    url = f"https://reading-home-apis.p.rapidapi.com/readinghome/api/get_books_by_search_rapidapi"
    querystring = {'search': search, 'page': page, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "reading-home-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getbooksbyauthorsearch(page: int, search: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get List of Books of a Searched Author Name"
    
    """
    url = f"https://reading-home-apis.p.rapidapi.com/readinghome/api/get_books_by_author_rapidapi"
    querystring = {'page': page, 'search': search, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "reading-home-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getbooksbycategory(is_id: int, page: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This will get a paginated list of books in a specific category"
    
    """
    url = f"https://reading-home-apis.p.rapidapi.com/readinghome/api/get_books_by_category_id_rapidapi"
    querystring = {'id': is_id, 'page': page, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "reading-home-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getallcategories(page: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Paginated List of All Categories"
    
    """
    url = f"https://reading-home-apis.p.rapidapi.com/readinghome/api/get_all_categories_rapiapi"
    querystring = {'page': page, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "reading-home-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

