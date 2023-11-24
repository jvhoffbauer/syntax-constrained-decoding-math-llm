import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_by_url(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search by URL"
    
    """
    url = f"https://redfin-com-data.p.rapidapi.com/property/search-url"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-com-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def property_details(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Property details"
    url: **1. The value of the url in  the  /Search endpoint**
Ex: /NY/Jamaica/9452-199th-St-11423/home/20743109
**2. Or copy the URL from the browser**
Ex: https://www.redfin.com/NY/Jamaica/9452-199th-St-11423/home/20743109 
        
    """
    url = f"https://redfin-com-data.p.rapidapi.com/property/detail"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-com-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(location: str, has_green_home: bool=None, keyword_search: str=None, has_rv_parking: bool=None, has_guest_house: bool=None, has_pets_allowed: bool=None, has_washer_dryer_hookup: bool=None, has_accessible_home: bool=None, has_primary_bedroom_on_main_floor: bool=None, has_elevator: bool=None, has_basement: bool=None, has_view: bool=None, has_include_outdoor_parking: bool=None, has_fireplace: bool=None, has_fixer_upper: bool=None, has_air_conditioning: bool=None, has_waterfront: bool=None, has_exclude_55_communities: bool=None, min_year_built: int=None, pool_type: str=None, garage_spots: int=None, max_year_built: int=None, min_stories: int=None, max_square_feet: int=None, max_stories: int=None, max_lot_size: int=None, min_lot_size: int=None, min_square_feet: int=None, time_on_redfin: str=None, min_price: int=None, status: str=None, max_bedroom: int=None, min_bathroom: int=None, home_type: str=None, min_bedroom: int=None, max_price: int=None, search_type: str=None, sort: str=None, sub_location: str=None, search_by: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search"
    location: Address or zip code
        garage_spots: garage_spots: 1->5
        home_type: Property type comma-separated or empty for all types:

```
House
Townhouse
Condo
Land
MultiFamily
Mobile
Co-op
Other
```
Ex: House,Townhouse
 
        search_by: Default: places 
        
    """
    url = f"https://redfin-com-data.p.rapidapi.com/property/search"
    querystring = {'location': location, }
    if has_green_home:
        querystring['has_green_home'] = has_green_home
    if keyword_search:
        querystring['keyword_search'] = keyword_search
    if has_rv_parking:
        querystring['has_rv_parking'] = has_rv_parking
    if has_guest_house:
        querystring['has_guest_house'] = has_guest_house
    if has_pets_allowed:
        querystring['has_pets_allowed'] = has_pets_allowed
    if has_washer_dryer_hookup:
        querystring['has_washer_dryer_hookup'] = has_washer_dryer_hookup
    if has_accessible_home:
        querystring['has_accessible_home'] = has_accessible_home
    if has_primary_bedroom_on_main_floor:
        querystring['has_primary_bedroom_on_main_floor'] = has_primary_bedroom_on_main_floor
    if has_elevator:
        querystring['has_elevator'] = has_elevator
    if has_basement:
        querystring['has_basement'] = has_basement
    if has_view:
        querystring['has_view'] = has_view
    if has_include_outdoor_parking:
        querystring['has_include_outdoor_parking'] = has_include_outdoor_parking
    if has_fireplace:
        querystring['has_fireplace'] = has_fireplace
    if has_fixer_upper:
        querystring['has_fixer_upper'] = has_fixer_upper
    if has_air_conditioning:
        querystring['has_air_conditioning'] = has_air_conditioning
    if has_waterfront:
        querystring['has_waterfront'] = has_waterfront
    if has_exclude_55_communities:
        querystring['has_exclude_55_communities'] = has_exclude_55_communities
    if min_year_built:
        querystring['min_year_built'] = min_year_built
    if pool_type:
        querystring['pool_type'] = pool_type
    if garage_spots:
        querystring['garage_spots'] = garage_spots
    if max_year_built:
        querystring['max_year_built'] = max_year_built
    if min_stories:
        querystring['min_stories'] = min_stories
    if max_square_feet:
        querystring['max_square_feet'] = max_square_feet
    if max_stories:
        querystring['max_stories'] = max_stories
    if max_lot_size:
        querystring['max_lot_size'] = max_lot_size
    if min_lot_size:
        querystring['min_lot_size'] = min_lot_size
    if min_square_feet:
        querystring['min_square_feet'] = min_square_feet
    if time_on_redfin:
        querystring['time_on_redfin'] = time_on_redfin
    if min_price:
        querystring['min_price'] = min_price
    if status:
        querystring['status'] = status
    if max_bedroom:
        querystring['max_bedroom'] = max_bedroom
    if min_bathroom:
        querystring['min_bathroom'] = min_bathroom
    if home_type:
        querystring['home_type'] = home_type
    if min_bedroom:
        querystring['min_bedroom'] = min_bedroom
    if max_price:
        querystring['max_price'] = max_price
    if search_type:
        querystring['search_type'] = search_type
    if sort:
        querystring['sort'] = sort
    if sub_location:
        querystring['sub_location'] = sub_location
    if search_by:
        querystring['search_by'] = search_by
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-com-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def autocomplete(location: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Autocomplete"
    
    """
    url = f"https://redfin-com-data.p.rapidapi.com/property/auto-complete"
    querystring = {'location': location, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-com-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

