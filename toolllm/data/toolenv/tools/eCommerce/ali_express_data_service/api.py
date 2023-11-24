import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def seller_items(sellerid: str, page: int=None, maxprice: int=None, target_language: str=None, minprice: int=None, size: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieves a list of all seller items"
    sellerid: Ali Express Seller Identifier
        page: The page number of the results to be retrieved. Default is 1.
        maxprice: Maximum Item Price
        target_language: The language of translation, list of all supported languages can be found [here](https://rapidapi.com/iamEvara/api/ali-express-data-service/tutorials/list-of-all-supported-languages).
        minprice: Minimum Item Price
        size: Number of results per page.
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/seller/sellerItems"
    querystring = {'sellerId': sellerid, }
    if page:
        querystring['page'] = page
    if maxprice:
        querystring['maxPrice'] = maxprice
    if target_language:
        querystring['target_language'] = target_language
    if minprice:
        querystring['minPrice'] = minprice
    if size:
        querystring['size'] = size
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def seller_info(sellerid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieves detailed seller info"
    sellerid: Ali Express Seller Identifier
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/seller/sellerInfo"
    querystring = {'sellerId': sellerid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_seller_items(sellerid: str, query: str, sort: str=None, maxprice: int=None, target_language: str=None, minprice: int=None, query_language: str=None, size: int=None, page: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Searches for sellers’ items using a query string"
    sellerid: Ali Express Seller Identifier
        query: Search query
        sort: This parameter is used to specify the sorting order of the items returned in the API response. There are six available sorting options for the `sort` parameter:

`default`: This is the default sort option, and it sorts the items based on the Pinduoduo platform's default sort order.

`price_asc`: This option sorts the items in ascending order of their prices, with the lowest priced items appearing first in the response.

`price_desc`: This option sorts the items in descending order of their prices, with the highest priced items appearing first in the response.

`total_price_asc`: This option sorts the items in ascending order of their total prices, which includes any discounts or promotions, with the lowest total priced items appearing first in the response.

`total_price_desc`: This option sorts the items in descending order of their total prices, with the highest total priced items appearing first in the response.

`volume_desc`: This option sorts the items in descending order of their sales volume, with the best-selling items appearing first in the response.

`vendor_rating_desc`: This option sorts the items in descending order of their seller rating, with the highest rated sellers appearing first in the response.

`updated_time_desc`: This option sorts the items in descending order of their update time, with the most recently updated items appearing first in the response.

        maxprice: Maximum Item Price
        target_language: The language of translation, list of all supported languages can be found [here](https://rapidapi.com/iamEvara/api/ali-express-data-service/tutorials/list-of-all-supported-languages).
        minprice: Minimum Item Price
        query_language: The `query_language` parameter specifies the language of the search query provided in the `query` parameter for translation into Chinese. This is important because the query must be in Chinese to be searched on the platform.
        size: Number of results per page.
        page: The page number of the results to be retrieved. Default is 1.
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/seller/searchSellerItems"
    querystring = {'sellerId': sellerid, 'query': query, }
    if sort:
        querystring['sort'] = sort
    if maxprice:
        querystring['maxPrice'] = maxprice
    if target_language:
        querystring['target_language'] = target_language
    if minprice:
        querystring['minPrice'] = minprice
    if query_language:
        querystring['query_language'] = query_language
    if size:
        querystring['size'] = size
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_suggestions(query: str, target_language: str=None, query_language: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Provides suggestions for search queries"
    query: Search query
        target_language: The language of translation, list of all supported languages can be found [here](https://rapidapi.com/iamEvara/api/ali-express-data-service/tutorials/list-of-all-supported-languages).
        query_language: The `query_language` parameter specifies the language of the search query provided in the `query` parameter for translation into Chinese. This is important because the query must be in Chinese to be searched on the platform.
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/search/searchSuggestions"
    querystring = {'query': query, }
    if target_language:
        querystring['target_language'] = target_language
    if query_language:
        querystring['query_language'] = query_language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_items(query: str, sort: str=None, instock: bool=None, hasdiscount: bool=None, query_language: str=None, minprice: int=None, target_language: str=None, maxprice: int=None, page: int=None, size: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Searches for items using a query string"
    query: Search query
        sort: This parameter is used to specify the sorting order of the items returned in the API response. There are six available sorting options for the `sort` parameter:

`default`: This is the default sort option, and it sorts the items based on the Pinduoduo platform's default sort order.

`price_asc`: This option sorts the items in ascending order of their prices, with the lowest priced items appearing first in the response.

`price_desc`: This option sorts the items in descending order of their prices, with the highest priced items appearing first in the response.

`total_price_asc`: This option sorts the items in ascending order of their total prices, which includes any discounts or promotions, with the lowest total priced items appearing first in the response.

`total_price_desc`: This option sorts the items in descending order of their total prices, with the highest total priced items appearing first in the response.

`volume_desc`: This option sorts the items in descending order of their sales volume, with the best-selling items appearing first in the response.

`vendor_rating_desc`: This option sorts the items in descending order of their seller rating, with the highest rated sellers appearing first in the response.

`updated_time_desc`: This option sorts the items in descending order of their update time, with the most recently updated items appearing first in the response.

        instock: If set to true, the results will contain only items in stock, if set to false the results will contain only items out of stock. Don't set the parameter so you can get both results.
        hasdiscount: If set to true, the results will contain only items with discount, if set to false the results will contain only items without a discount. Don't set the parameter so you can get both results.
        query_language: The `query_language` parameter specifies the language of the search query provided in the `query` parameter for translation into Chinese. This is important because the query must be in Chinese to be searched on the platform.
        minprice: Minimum Item Price
        target_language: The language of translation, list of all supported languages can be found [here](https://rapidapi.com/iamEvara/api/ali-express-data-service/tutorials/list-of-all-supported-languages).
        maxprice: Maximum Item Price
        page: The page number of the results to be retrieved. Default is 1.
        size: Number of results per page.
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/search/searchItems"
    querystring = {'query': query, }
    if sort:
        querystring['sort'] = sort
    if instock:
        querystring['inStock'] = instock
    if hasdiscount:
        querystring['hasDiscount'] = hasdiscount
    if query_language:
        querystring['query_language'] = query_language
    if minprice:
        querystring['minPrice'] = minprice
    if target_language:
        querystring['target_language'] = target_language
    if maxprice:
        querystring['maxPrice'] = maxprice
    if page:
        querystring['page'] = page
    if size:
        querystring['size'] = size
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_by_image(imageurl: str, page: int=None, target_language: str=None, size: int=None, sort: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Searches for items based on an uploaded image"
    imageurl: The Url of the image being searched.
        page: The page number of the results to be retrieved. Default is 1.
        target_language: The language of translation, list of all supported languages can be found [here](https://rapidapi.com/iamEvara/api/taobao-tmall-Tao-Bao-data-service/tutorials/list-of-all-supported-languages).
        size: Number of results per page.
        sort: This parameter is used to specify the sorting order of the items returned in the API response. There are six available sorting options for the `sort` parameter:

`default`: This is the default sort option, and it sorts the items based on the Pinduoduo platform's default sort order.

`price_asc`: This option sorts the items in ascending order of their prices, with the lowest priced items appearing first in the response.

`price_desc`: This option sorts the items in descending order of their prices, with the highest priced items appearing first in the response.

`total_price_asc`: This option sorts the items in ascending order of their total prices, which includes any discounts or promotions, with the lowest total priced items appearing first in the response.

`total_price_desc`: This option sorts the items in descending order of their total prices, with the highest total priced items appearing first in the response.

`volume_desc`: This option sorts the items in descending order of their sales volume, with the best-selling items appearing first in the response.

`vendor_rating_desc`: This option sorts the items in descending order of their seller rating, with the highest rated sellers appearing first in the response.

`updated_time_desc`: This option sorts the items in descending order of their update time, with the most recently updated items appearing first in the response.

        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/search/searchByImage"
    querystring = {'imageUrl': imageurl, }
    if page:
        querystring['page'] = page
    if target_language:
        querystring['target_language'] = target_language
    if size:
        querystring['size'] = size
    if sort:
        querystring['sort'] = sort
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def item_reviews(itemid: int, size: int=None, target_language: str=None, page: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieves all item reviews"
    itemid: Ali Express Item Identifier
        size: Number of results per page.
        target_language: The language of translation, list of all supported languages can be found [here](https://rapidapi.com/iamEvara/api/ali-express-data-service/tutorials/list-of-all-supported-languages).
        page: The page number of the results to be retrieved. Default is 1.
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/item/itemReviews"
    querystring = {'itemId': itemid, }
    if size:
        querystring['size'] = size
    if target_language:
        querystring['target_language'] = target_language
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def item_info(itemid: int, target_language: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieves Ali Express item information"
    itemid: Ali Express Item Identifier
        target_language: The language of translation, list of all supported languages can be found [here](https://rapidapi.com/iamEvara/api/ali-express-data-service/tutorials/list-of-all-supported-languages).
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/item/itemInfo"
    querystring = {'itemId': itemid, }
    if target_language:
        querystring['target_language'] = target_language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def item_app_info(itemid: int, target_language: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieves original item information from Ali Express App"
    itemid: Ali Express Item Identifier
        target_language: The language of translation, list of all supported languages can be found [here](https://rapidapi.com/iamEvara/api/ali-express-data-service/tutorials/list-of-all-supported-languages).
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/item/itemAppInfo"
    querystring = {'itemId': itemid, }
    if target_language:
        querystring['target_language'] = target_language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def item_description(itemid: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieves item Description"
    itemid: Ali Express Item Identifier
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/item/itemDescription"
    querystring = {'itemId': itemid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def items_batch_info(itemids: str, target_language: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieves batch information for multiple items at once"
    itemids: Specify the IDs of the items for which simple information will be retrieved. The IDs should be provided as a comma-separated list of values (eg. `3256803705009551,3256803691845385,3256805290149005`).
        target_language: The language of translation, list of all supported languages can be found [here](https://rapidapi.com/iamEvara/api/ali-express-data-service/tutorials/list-of-all-supported-languages).
        
    """
    url = f"https://ali-express-data-service.p.rapidapi.com/item/itemsBatchInfo"
    querystring = {'itemIds': itemids, }
    if target_language:
        querystring['target_language'] = target_language
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ali-express-data-service.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

