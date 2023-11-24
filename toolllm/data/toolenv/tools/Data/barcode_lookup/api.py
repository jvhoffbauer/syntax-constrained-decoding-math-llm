import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def product(asin: str=None, page: str=None, barcode: int=None, mpn: str=None, search: str=None, category: str=None, title: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Endpoint to retrieve product data."
    asin: ASIN
        page: Page number for any search query (10 results per page)
        barcode: UPC, EAN or ISBN number
        mpn: Manufacturer Part Number
        search: Any search term or phrase
        title: Product Name
        
    """
    url = f"https://barcode-lookup.p.rapidapi.com/v3/products"
    querystring = {}
    if asin:
        querystring['asin'] = asin
    if page:
        querystring['page'] = page
    if barcode:
        querystring['barcode'] = barcode
    if mpn:
        querystring['mpn'] = mpn
    if search:
        querystring['search'] = search
    if category:
        querystring['category'] = category
    if title:
        querystring['title'] = title
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "barcode-lookup.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

