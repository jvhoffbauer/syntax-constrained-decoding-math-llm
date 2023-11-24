import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def products_search_deprecated(start: str, rows: str, query: str, sizes: str=None, brand: str=None, sort: str=None, gender: str=None, color_groups: str='black', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for product by name"
    rows: The number of records to return
        query: The name of products to look for
        sizes: Look for values in facet_fields object, you can pass this param multiple times
        brand: Look for values in facet_fields object, you can pass this param multiple times
        sort: One of the following newest|low|high|rate|popular
        gender: Look for values in facet_fields object, you can pass this param multiple times
        color_groups: Look for values in facet_fields object, you can pass this param multiple times
        
    """
    url = f"https://apidojo-forever21-v1.p.rapidapi.com/products/search"
    querystring = {'start': start, 'rows': rows, 'query': query, }
    if sizes:
        querystring['sizes'] = sizes
    if brand:
        querystring['brand'] = brand
    if sort:
        querystring['sort'] = sort
    if gender:
        querystring['gender'] = gender
    if color_groups:
        querystring['color_groups'] = color_groups
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def categories_v2_list(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List all categories from F21"
    
    """
    url = f"https://apidojo-forever21-v1.p.rapidapi.com/categories/v2/list"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def products_list_deprecated(page: str, pagesize: str, category: str, sort: str=None, size: str='Medium', maxprice: str='250', color: str='red', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List products by category"
    page: The page number to display data
        pagesize: The records return in each page
        category: Look for values from /categories/list
        sort: One of the following newest|low|high|rate|popular
        size: Look for values in Sizes object, you can pass this param multiple times
        maxprice: Limit products return under this amount of money
        color: Look for values in Variants object, you can pass this param multiple times
        
    """
    url = f"https://apidojo-forever21-v1.p.rapidapi.com/products/list"
    querystring = {'page': page, 'pagesize': pagesize, 'category': category, }
    if sort:
        querystring['sort'] = sort
    if size:
        querystring['size'] = size
    if maxprice:
        querystring['maxprice'] = maxprice
    if color:
        querystring['color'] = color
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def categories_list_deprecated(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List all categories from F21"
    
    """
    url = f"https://apidojo-forever21-v1.p.rapidapi.com/categories/list"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def products_detail_deprecated(productid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get detail information of product by id"
    productid: Look for values of ProductId object from /products/list API
        
    """
    url = f"https://apidojo-forever21-v1.p.rapidapi.com/products/detail"
    querystring = {'productid': productid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def products_v2_list(category: str, pagenumber: int=1, pagesize: int=48, minprice: str=None, filtersize: str='XS/S', sortby: int=0, maxprice: str=None, filtercolor: str='BLACK', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List products by category"
    category: The value of Category field returned in .../categories/v2/list endpoint
        pagenumber: The page number to display data
        pagesize: The records return in each page
        minprice: Search for products higher this amount of money, leave empty to ignore this filter.
        filtersize: The value of Filter/SizeList/Key JSON object returned right in this endpoint. Pass this parameter multiple times to apply multiple filters at once. Ex : ...&filterSize=XS/S&filterSize=S&...

        sortby: One of the following 1-Newest|2-HighToLow|3-LowToHight|4-HighestRating|5-Most popular
        maxprice: Search for products lower this amount of money, leave empty to ignore this filter.
        filtercolor: The value of Filter/ColorList/Key JSON object returned right in this endpoint. Pass this parameter multiple times to apply multiple filters at once. Ex : ...&filterColor=BLACK&filterColor=BLUE&...
        
    """
    url = f"https://apidojo-forever21-v1.p.rapidapi.com/products/v2/list"
    querystring = {'category': category, }
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if pagesize:
        querystring['pageSize'] = pagesize
    if minprice:
        querystring['minPrice'] = minprice
    if filtersize:
        querystring['filterSize'] = filtersize
    if sortby:
        querystring['sortby'] = sortby
    if maxprice:
        querystring['maxPrice'] = maxprice
    if filtercolor:
        querystring['filterColor'] = filtercolor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def products_v2_detail(productid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get detail information of product by id"
    productid: Look for values of ProductId object returned in .../products/v2/list endpoint
        
    """
    url = f"https://apidojo-forever21-v1.p.rapidapi.com/products/v2/detail"
    querystring = {'productId': productid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

