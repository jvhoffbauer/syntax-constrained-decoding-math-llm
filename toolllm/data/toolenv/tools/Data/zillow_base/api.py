import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def locationsuggestions(location: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a location"
    location: State, county, neighborhood, city, street name, zip code
        
    """
    url = f"https://zillow-base1.p.rapidapi.com/WebAPIs/zillow/locationSuggestions"
    querystring = {'location': location, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-base1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def locationsuggestions_v2(location: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a location"
    location: State, county, neighborhood, city, street name, zip code
        
    """
    url = f"https://zillow-base1.p.rapidapi.com/WebAPIs/zillow/locationSuggestions/v2"
    querystring = {'location': location, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-base1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getzipcodebycounty(county: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get zip code by county"
    
    """
    url = f"https://zillow-base1.p.rapidapi.com/WebAPIs/zillow/getZipCodeByCounty"
    querystring = {'county': county, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-base1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getlocationinfobyzipcode(zipcode: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get location information by zip code"
    
    """
    url = f"https://zillow-base1.p.rapidapi.com/WebAPIs/zillow/getLocationInfoByZipCode"
    querystring = {'zipcode': zipcode, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-base1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getzipcodebycity(city: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get zip code by city"
    
    """
    url = f"https://zillow-base1.p.rapidapi.com/WebAPIs/zillow/getZipCodeByCity"
    querystring = {'city': city, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-base1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_by_url(currentpage: int=1, url: str='https://www.zillow.com/brownsville-tx/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Brownsville%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-97.80795063281249%2C%22east%22%3A-96.96200336718749%2C%22south%22%3A25.648006723151287%2C%22north%22%3A26.253066850624663%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A51167%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A40569%2C%22max%22%3A243413%7D%2C%22mp%22%3A%7B%22min%22%3A200%2C%22max%22%3A1200%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22sqft%22%3A%7B%22min%22%3A750%2C%22max%22%3A1500%7D%7D%2C%22isListVisible%22%3Atrue%7D', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search by URL"
    
    """
    url = f"https://zillow-base1.p.rapidapi.com/WebAPIs/zillow/searchByUrl"
    querystring = {}
    if currentpage:
        querystring['currentPage'] = currentpage
    if url:
        querystring['url'] = url
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-base1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(location: str, is_city_view: bool=None, days_on_zillow: str=None, is_water_view: bool=None, has_basement_unfinished: bool=None, is_mountain_view: bool=None, has_basement_finished: bool=None, keywords: str=None, has_pool: bool=None, is_park_view: bool=None, is_waterfront: bool=None, has_single_story_only: bool=None, min_year_built: int=None, max_year_built: int=None, has_air_conditioning: bool=None, max_lot_size: int=None, min_lot_size: int=None, max_square_feet: int=None, min_square_feet: int=None, has_garage: int=None, parking_spots: int=None, has_3d_tour: bool=None, has_open_house: bool=None, has_incomplete_hoa: bool=None, max_hoa: str=None, max_baths: int=None, min_baths: int=None, home_type: str=None, max_beds: int=None, min_beds: int=None, sort_by: str='Homes_For_You', page: int=1, min_price: int=None, max_price: int=None, status_type: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for properties"
    location: 
Location details, address, county, Zip code.
        is_city_view: `is_city_view`= City(View)
        days_on_zillow: Days on Z. Use with 
status_type=**ForSale** OR **ForRent**
        is_water_view: `is_water_view`= Water(View)
        has_basement_unfinished: `has_basement_unfinished`=Has basement unfinished
        is_mountain_view: `is_mountain_view`= Mountain(View)
        has_basement_finished: `has_basement_finished`=Has basement finished
        keywords: Filter with keywords: MLS #, yard, etc.
        has_pool: `has_pool`=Must have pool (Other Amenities)
        is_park_view: `is_park_view`= Park(View)
        is_waterfront: `is_waterfront`=Waterfront (Other Amenities)
        has_single_story_only: `has_single_story_only`:  Single-story only (Number Of Stories)
        min_year_built: Format: YYYY,  For instance: 2021
        max_year_built: Format: YYYY,  For instance: 2023
        has_air_conditioning: `has_air_conditioning`=Must have A/C (Other Amenities)
        max_lot_size: Available values:

- `2000`=2,000 sqft
- `3000`=3,000 sqft
- `4000`=4,000 sqft
- `5000`=5,000 sqft
- `7500`=7,500 sqft
- `10890`=1/4 acre/10,890 sqft
- `21780`=1/2 acre
- `43560`=1 acre
- `87120`=2 acres
- `217800`=5 acres
- `435600`=10 acres
- `871200`=20 acres
- `2178000`=50 acres
- `4356000`=100 acres
        min_lot_size: Available values:

- `1000`=1,000 sqft
- `2000`=2,000 sqft
- `3000`=3,000 sqft
- `4000`=4,000 sqft
- `5000`=5,000 sqft
- `7500`=7,500 sqft
- `10890`=1/4 acre/10,890 sqft
- `21780`=1/2 acre
- `43560`=1 acre
- `87120`=2 acres
- `217800`=5 acres
- `435600`=10 acres
- `871200`=20 acres
- `2178000`=50 acres
- `4356000`=100 acres
        has_garage: ◆`has_garage`=Must have garage(Parking Spots)
◆For status_type = **ForSale** OR **RecentlySold**
        parking_spots: ◆`min_parking_spots`=Parking Spots
◆For status_type = **ForSale** OR **RecentlySold**
        has_3d_tour: ◆`has_3d_tour`= Must have 3D Tour (Tours )
◆For status_type = **ForSale** OR **ForRent**
        has_open_house: ◆`has_open_house`= Must have open house (Tours )
◆For status_type = **ForSale**
        has_incomplete_hoa: ◆has_incomplete_hoa =  Include homes with incomplete HOA data
◆For status_type = **ForSale** OR **RecentlySold**
◆Default - `true`
        max_hoa: For status_type =**ForSale** OR **RecentlySold**
- `Any`: Any
- `0`: No HOA Fee
- `50`: $50/month
- `100`: $100/month
- `200`: $200/month
- `300`: $300/month
- `400`: $400/month
- `500`: $500/month
- `600`: $600/month
- `700`: $700/month
- `800`: $800/month
- `900`: $900/month
- `1000 `$1000/month
        home_type: Property type comma-separated or empty for all types
**For Rent**
- `Houses`: Houses
- `ApartmentOrCondo`: Apartments/Condos/Co-ops
- `Townhomes`: Townhomes

**For others:**
- `Houses`: Houses
- `Townhomes`: Townhomes
- `Multifamily`: Multi-family
- `CondosOrCoops`: Condos/Co-ops
- `LotsLand`: Lots/Land
- `Apartments`: Apartments
- `Manufactured`: Manufactured
        sort_by: **ForSale** OR **RecentlySold** are available:

- Homes_for_You
- Price_High_Low
- Price_Low_High
- Newest:
- Bedrooms
- Bathrooms
- Square_Feet
- Lot_Size
default: Homes_for_You

**ForRent** are available:

- Verified_Source
- Payment_High_Low
- Payment_Low_High
- Newest
- Bedrooms
- Bathrooms
- Square_Feet
- Lot_Size
default: Verified_Source
        
    """
    url = f"https://zillow-base1.p.rapidapi.com/WebAPIs/zillow/search"
    querystring = {'location': location, }
    if is_city_view:
        querystring['is_city_view'] = is_city_view
    if days_on_zillow:
        querystring['days_on_zillow'] = days_on_zillow
    if is_water_view:
        querystring['is_water_view'] = is_water_view
    if has_basement_unfinished:
        querystring['has_basement_unfinished'] = has_basement_unfinished
    if is_mountain_view:
        querystring['is_mountain_view'] = is_mountain_view
    if has_basement_finished:
        querystring['has_basement_finished'] = has_basement_finished
    if keywords:
        querystring['keywords'] = keywords
    if has_pool:
        querystring['has_pool'] = has_pool
    if is_park_view:
        querystring['is_park_view'] = is_park_view
    if is_waterfront:
        querystring['is_waterfront'] = is_waterfront
    if has_single_story_only:
        querystring['has_single_story_only'] = has_single_story_only
    if min_year_built:
        querystring['min_year_built'] = min_year_built
    if max_year_built:
        querystring['max_year_built'] = max_year_built
    if has_air_conditioning:
        querystring['has_air_conditioning'] = has_air_conditioning
    if max_lot_size:
        querystring['max_lot_size'] = max_lot_size
    if min_lot_size:
        querystring['min_lot_size'] = min_lot_size
    if max_square_feet:
        querystring['max_square_feet'] = max_square_feet
    if min_square_feet:
        querystring['min_square_feet'] = min_square_feet
    if has_garage:
        querystring['has_garage'] = has_garage
    if parking_spots:
        querystring['parking_spots'] = parking_spots
    if has_3d_tour:
        querystring['has_3d_tour'] = has_3d_tour
    if has_open_house:
        querystring['has_open_house'] = has_open_house
    if has_incomplete_hoa:
        querystring['has_incomplete_hoa'] = has_incomplete_hoa
    if max_hoa:
        querystring['max_hoa'] = max_hoa
    if max_baths:
        querystring['max_baths'] = max_baths
    if min_baths:
        querystring['min_baths'] = min_baths
    if home_type:
        querystring['home_type'] = home_type
    if max_beds:
        querystring['max_beds'] = max_beds
    if min_beds:
        querystring['min_beds'] = min_beds
    if sort_by:
        querystring['sort_by'] = sort_by
    if page:
        querystring['page'] = page
    if min_price:
        querystring['min_price'] = min_price
    if max_price:
        querystring['max_price'] = max_price
    if status_type:
        querystring['status_type'] = status_type
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-base1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def property_details(zpid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Property details"
    
    """
    url = f"https://zillow-base1.p.rapidapi.com/WebAPIs/zillow/homedetails"
    querystring = {'zpid': zpid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "zillow-base1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

