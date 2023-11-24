import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def categories_list(caid: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List categories and their recursive children categories if available"
    caid: The value of categoryId fields returned right in this endpoint. The default root category is 214970.
        
    """
    url = f"https://wayfair.p.rapidapi.com/categories/list"
    querystring = {'caid': caid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wayfair.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def reviews_list(sku: str, page: int=1, star: str=None, sort_order: str='RELEVANCE', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List reviews relating to specific product"
    sku: The value of sku fields returned in .../products/list or .../products/search endpoint.
        page: For paging purpose
        star: Leave empty or  1 to 5
        sort_order: One of the following : RELEVANCE|HELPFUL|DATE&#95;ASCENDING|DATE&#95;DESCENDING|IMAGE|RATING&#95;DESCENDING|RATING&#95;ASCENDING
        
    """
    url = f"https://wayfair.p.rapidapi.com/reviews/list"
    querystring = {'sku': sku, }
    if page:
        querystring['page'] = page
    if star:
        querystring['star'] = star
    if sort_order:
        querystring['sort_order'] = sort_order
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wayfair.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def products_list(categoryid: int, currentzipcode: str=None, page: int=1, itemsperpage: int=48, sortid: int=None, filterstringunencoded: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List products with filters and options"
    categoryid: The value of categoryId fields returned in .../categories/list endpoint
        currentzipcode: The postal code to get near available products.
        page: For paging purpose
        itemsperpage: For paging purpose
        sortid: Check availableSorts field returned right in this endpoint for suitable sortId
        filterstringunencoded: The value of filterStringUnencoded fields returned right in this endpoint to filter products, pass this parameter multiple times for multiple filters. Ex : ...&filterStringUnencoded=a1234567890~2147483646&filterStringUnencoded=at&#95;style~Tiffany&...
        
    """
    url = f"https://wayfair.p.rapidapi.com/products/list"
    querystring = {'categoryId': categoryid, }
    if currentzipcode:
        querystring['currentZipCode'] = currentzipcode
    if page:
        querystring['page'] = page
    if itemsperpage:
        querystring['itemsPerPage'] = itemsperpage
    if sortid:
        querystring['sortId'] = sortid
    if filterstringunencoded:
        querystring['filterStringUnencoded'] = filterstringunencoded
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wayfair.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def products_search(keyword: str, filters: str=None, curpage: int=1, itemsperpage: int=48, sortby: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for products by term or phrase"
    keyword: Any term or phrase to look for relating products
        filters: The value of filter&#95;string&#95;unencoded fields returned right in this endpoint to filter products, pass this parameter multiple times for multiple filters. Ex : ...&filters=colorList~White&filters=masterClID~180&...
        curpage: For paging purpose
        itemsperpage: For paging purpose
        sortby: The value of sort_value fields returned right in this endpoint. Default is 0
        
    """
    url = f"https://wayfair.p.rapidapi.com/products/search"
    querystring = {'keyword': keyword, }
    if filters:
        querystring['filters'] = filters
    if curpage:
        querystring['curpage'] = curpage
    if itemsperpage:
        querystring['itemsperpage'] = itemsperpage
    if sortby:
        querystring['sortby'] = sortby
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wayfair.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def products_detail(sku: str, wfproductoptions: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get detail information of specific product"
    sku: The value of sku fields returned in .../products/list or .../products/search endpoint.
        wfproductoptions: The value of id fields under relevantAttributes JSON object returned right in this endpoint, pass this parameter multiple time for multiple options. Ex : ...&wfProductOptions=1234567890&wfProductOptions=special_offers&...
        
    """
    url = f"https://wayfair.p.rapidapi.com/products/detail"
    querystring = {'sku': sku, }
    if wfproductoptions:
        querystring['wfProductOptions'] = wfproductoptions
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wayfair.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def auto_complete(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get auto suggestions by term or phrase"
    query: Any term or phrase that you are familiar with
        
    """
    url = f"https://wayfair.p.rapidapi.com/auto-complete"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wayfair.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

