import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_product_detail_by_id(shop_id: int, item_id: int, site: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GET product detail by 'item_id' and 'shop_id'"
    shop_id: if the product url is [https://shopee.com.my/Xiaomi-Redmi-AirDots-TWS-Mi-True-Wireless-EarBuds-Basic-Earphone-Bluetooth-5.0-Bass-Voice-Control-(BLACK)-i.70413398.7041129024?ads_keyword=wkdaelpmissisiht&adsid=10115290&campaignid=5587639&position=120](url),then the item_id is 7041129024,shop_id is 70413398
        item_id: if the product url is [https://shopee.com.my/Xiaomi-Redmi-AirDots-TWS-Mi-True-Wireless-EarBuds-Basic-Earphone-Bluetooth-5.0-Bass-Voice-Control-(BLACK)-i.70413398.7041129024?ads_keyword=wkdaelpmissisiht&adsid=10115290&campaignid=5587639&position=120](url),then the item_id is 7041129024,shop_id is 70413398
        site: Optional values: my, th, vn, ph, sg, id, tw, br
        
    """
    url = f"https://shopee-e-commerce-data.p.rapidapi.com/api/sc/shopee/item_detail"
    querystring = {'shop_id': shop_id, 'item_id': item_id, 'site': site, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shopee-e-commerce-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_shop_items(site: str, shop_id: int, page: int=None, pagesize: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Shop all items"
    
    """
    url = f"https://shopee-e-commerce-data.p.rapidapi.com/api/sc/shopee/shop/items"
    querystring = {'site': site, 'shop_id': shop_id, }
    if page:
        querystring['page'] = page
    if pagesize:
        querystring['pageSize'] = pagesize
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shopee-e-commerce-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_search_items(keyword: str, site: str, by: str=None, page: int=1, pagesize: int=60, order: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GET search items by keyword"
    site: Optional values: my, th, vn, ph, sg, id, tw, br
        
    """
    url = f"https://shopee-e-commerce-data.p.rapidapi.com/api/sc/shopee/search/items"
    querystring = {'keyword': keyword, 'site': site, }
    if by:
        querystring['by'] = by
    if page:
        querystring['page'] = page
    if pagesize:
        querystring['pageSize'] = pagesize
    if order:
        querystring['order'] = order
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shopee-e-commerce-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_shop_detail(shop_id: int, site: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GET shop detail  by shop_id"
    site: Optional values: my, th, vn, ph, sg, id, tw, br
        
    """
    url = f"https://shopee-e-commerce-data.p.rapidapi.com/api/sc/shopee/shop/shop_info"
    querystring = {'shop_id': shop_id, 'site': site, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shopee-e-commerce-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_search_hints(site: str, keyword: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "GET search hints by keyword"
    site: Optional values: my, th, vn, ph, sg, id, tw, br
        
    """
    url = f"https://shopee-e-commerce-data.p.rapidapi.com/api/sc/shopee/search/hints"
    querystring = {'site': site, 'keyword': keyword, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "shopee-e-commerce-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

