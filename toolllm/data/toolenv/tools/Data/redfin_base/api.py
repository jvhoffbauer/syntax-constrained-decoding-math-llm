import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_by_url(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search by URL"
    
    """
    url = f"https://redfin-base.p.rapidapi.com/WebAPIs/redfin/searchByURL"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-base.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_location_infomation_by_zipcode(zipcode: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get location infomation by zipcode"
    
    """
    url = f"https://redfin-base.p.rapidapi.com/WebAPIs/base/getLocationInfoByZipCode"
    querystring = {'zipcode': zipcode, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-base.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_zipcode_by_county(county: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get zipcode by county"
    
    """
    url = f"https://redfin-base.p.rapidapi.com/WebAPIs/base/getZipCodeByCounty"
    querystring = {'county': county, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-base.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_zipcode_by_city(city: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get ZipCode by City"
    
    """
    url = f"https://redfin-base.p.rapidapi.com/WebAPIs/base/getZipCodeByCity"
    querystring = {'city': city, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-base.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_by_sub_url(sub_url: str, excl_ll: bool=None, price_reduced: str=None, financing_type: str=None, property_tax: int=None, hoa_feets: int=None, green_home: bool=None, elevator: bool=None, pets_allowed: bool=None, washer_dryer_hookup: bool=None, fireplace: bool=None, pool_types: str=None, basement_types: str=None, min_sqft: int=None, garage_spots: str=None, max_stories: int=None, max_num_beds: int=None, max_sqft: int=None, max_lot_size: int=None, home_type: str=None, search_type: str=None, sold_within_days: str=None, min_num_beds: int=None, min_price: int=None, min_price_per_sqft: int=None, min_lot_size: int=None, num_baths: int=None, time_on_redfin: str=None, min_stories: int=None, dogs_allowed: bool=None, has_view: bool=None, accessible_home: bool=None, max_price_per_sqft: int=None, waterfront: bool=None, include_outdoor_parking: bool=None, max_year_built: int=None, status: str='active,comingsoon', cats_allowed: bool=None, guest_house: bool=None, fixer_upper: bool=None, keyword_search: str=None, primary_bed_on_main: bool=None, air_conditioning: bool=None, has_exclude_55_communities: bool=None, min_year_built: int=None, max_price: int=None, sort: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search by Sub URL"
    sub_url: The input value can be full URL or sub URL
- **Full URL**: `https://www.redfin.com/zipcode/01026`
- **Sub URL**: `/zipcode/01026` (use the Auto-complete API to get the value, it is a property URL)
        excl_ll: Exclude land leases
        financing_type: Accepted financing
        property_tax: COMMENT:
Suggested Values:
`0`: No property taxes ❚`250`: $250/year
`500`: $500/year❚`750`: $750/year
`1000`: $1,000/year❚`1250`: $1,250/year
`1500`: $1,500/year❚`1750`: $1,750/year
`2000`: $2,000/year❚`2500`: $2,500/year
`3000`: $3,000/year❚`3500`: $3,500/year
`4000`: $4,000/year❚`4500`: $4,500/year
`5000`: $5,000/year❚`5500`: $5,500/year
`6000`: $6,000/year❚`6500`: $6,500/year
`7000`: $7,000/year❚`8000`: $8,000/year
`10000`: $10,000/year❚`12000`: $12,000/year
`14000`: $14,000/year❚`16000`: $16,000/year
`20000`: $20,000/year❚`24000`: $24,000/year

        hoa_feets: Suggested Values:
`0`: No HOA Fee ❚ `25`: $25/month
`50`: $50/month ❚ `75`: $75/month
`100`: $100/month❚  `150`: $150/month
`200`: $200/month ❚ `250`: $250/month
 `300`: $300/month ❚ `400`: $400/month
 `500`: $500/month ❚ `600`: $600/month
 `700`: $700/month ❚ `800`: $800/month
 `900`: $900/month ❚`1000`: $1000/month
 `1250`: $1250/month ❚ `1500`: $1500/month
 `1750`: $1750/month ❚`2000`: $2000/month
 `2500`: $2500/month ❚ `3000`: $3000/month
 `3500`: $3500/month ❚ `4000`: $4000/month
 `4500`: $4500/month ❚ `5000`: $5000/month
        basement_types: Enter the parameters below:
  ● Finished
  ● Unfinished
※ Separated by a comma for multiple options
EX: Finished, Unfinished
        min_sqft: Suggested Values: `750`, `1000`, `1100`, `1200`, `1300`, `1400`, `1500`, `1600`, `1700`, `1800`, `1900`, `2000`, `2250`, `2500`, `2750`, `3000`, `4000`, `5000`, `7500`, `10000`
        max_stories: Enter a value in the range 1 ～ 20
        max_num_beds: Enter a value in the range 1 ～ 5
        max_sqft: Suggested Values: `750`, `1000`, `1100`, `1200`, `1300`, `1400`, `1500`, `1600`, `1700`, `1800`, `1900`, `2000`, `2250`, `2500`, `2750`, `3000`, `4000`, `5000`, `7500`, `10000`
        max_lot_size: Suggested Values:
`2000`＝2,000 sqft❚`4500`＝4,500 sqft
`6500`＝6,500 sqft❚`8000`＝8,000 sqft
`9500`＝9,500 sqft❚`10890`＝25 acres
`21780`＝5 acres❚`43560`＝1 acre
`87120`＝2 acres❚`130680`＝3 acres
 `174240`＝4 acres❚`217800`＝5 acres
 `435600`＝10 acres❚ `871200`＝20 acres
`1742400`＝40 acres❚ `4356000`＝100 acres
        home_type: Enter the parameters below:
For `search_type `＝ **ForSale** OR **Sold**
  ● House
  ● Townhouse
  ● Condo
  ● Land
  ● MultiFamily
  ● Mobile
  ● Coop
  ● Other
For `search_type `＝ **ForRent**
  ● Apartment
※ Separated by a comma for multiple options
EX: House, Townhouse
        search_type: Default＝**ForSale**
        sold_within_days: Default ＝ Last_3_months
For `search_type `＝**Sold**

        min_num_beds: Enter a value in the range 1 ～ 5
        min_price_per_sqft: Price/Sq. ft.
Suggested Values:  `50`, `100`, `150`, `200`, `250`, `300`, `400`, `500`, `600`, `800`, `1000`, `1400`, `1800`, `2200`, `2600`, `3000`
        min_lot_size: Suggested Values:
`2000`＝2,000 sqft❚`4500`＝4,500 sqft
`6500`＝6,500 sqft❚`8000`＝8,000 sqft
`9500`＝9,500 sqft❚`10890`＝25 acres
`21780`＝5 acres❚`43560`＝1 acre
`87120`＝2 acres❚`130680`＝3 acres
 `174240`＝4 acres❚`217800`＝5 acres
 `435600`＝10 acres❚ `871200`＝20 acres
`1742400`＝40 acres❚ `4356000`＝100 acres
        num_baths: Suggested Values: `1`, `1.5`, `2`, `2.5`, `3.4`
        min_stories: Enter a value in the range 1 ～ 20
        dogs_allowed: For `search_type `＝**ForRent**
        max_price_per_sqft: Price/Sq. ft.
Suggested Values:  `50`, `100`, `150`, `200`, `250`, `300`, `400`, `500`, `600`, `800`, `1000`, `1400`, `1800`, `2200`, `2600`, `3000`
        include_outdoor_parking: 【Include outdoor parking】 value is reflected when at 【Garage spots】 is selected
        status: For search_type ＝**ForSale**

Enter the parameters below: 
● active
● comingsoon
● undercontract_pending
※ Separated by a comma for multiple options
EX: active, comingsoon
        cats_allowed: For `search_type `＝**ForRent**
        keyword_search: E.g. office, balcony, modern,place
        max_price: Filter by price
        sort: Default ＝ Recommended
        
    """
    url = f"https://redfin-base.p.rapidapi.com/WebAPIs/redfin/searchBySubURL"
    querystring = {'sub_url': sub_url, }
    if excl_ll:
        querystring['excl_ll'] = excl_ll
    if price_reduced:
        querystring['price_reduced'] = price_reduced
    if financing_type:
        querystring['financing_type'] = financing_type
    if property_tax:
        querystring['property_tax'] = property_tax
    if hoa_feets:
        querystring['hoa_feets'] = hoa_feets
    if green_home:
        querystring['green_home'] = green_home
    if elevator:
        querystring['elevator'] = elevator
    if pets_allowed:
        querystring['pets_allowed'] = pets_allowed
    if washer_dryer_hookup:
        querystring['washer_dryer_hookup'] = washer_dryer_hookup
    if fireplace:
        querystring['fireplace'] = fireplace
    if pool_types:
        querystring['pool_types'] = pool_types
    if basement_types:
        querystring['basement_types'] = basement_types
    if min_sqft:
        querystring['min_sqft'] = min_sqft
    if garage_spots:
        querystring['garage_spots'] = garage_spots
    if max_stories:
        querystring['max_stories'] = max_stories
    if max_num_beds:
        querystring['max_num_beds'] = max_num_beds
    if max_sqft:
        querystring['max_sqft'] = max_sqft
    if max_lot_size:
        querystring['max_lot_size'] = max_lot_size
    if home_type:
        querystring['home_type'] = home_type
    if search_type:
        querystring['search_type'] = search_type
    if sold_within_days:
        querystring['sold_within_days'] = sold_within_days
    if min_num_beds:
        querystring['min_num_beds'] = min_num_beds
    if min_price:
        querystring['min_price'] = min_price
    if min_price_per_sqft:
        querystring['min_price_per_sqft'] = min_price_per_sqft
    if min_lot_size:
        querystring['min-lot-size'] = min_lot_size
    if num_baths:
        querystring['num_baths'] = num_baths
    if time_on_redfin:
        querystring['time_on_redfin'] = time_on_redfin
    if min_stories:
        querystring['min_stories'] = min_stories
    if dogs_allowed:
        querystring['dogs_allowed'] = dogs_allowed
    if has_view:
        querystring['has_view'] = has_view
    if accessible_home:
        querystring['accessible_home'] = accessible_home
    if max_price_per_sqft:
        querystring['max_price_per_sqft'] = max_price_per_sqft
    if waterfront:
        querystring['waterfront'] = waterfront
    if include_outdoor_parking:
        querystring['include_outdoor_parking'] = include_outdoor_parking
    if max_year_built:
        querystring['max_year_built'] = max_year_built
    if status:
        querystring['status'] = status
    if cats_allowed:
        querystring['cats_allowed'] = cats_allowed
    if guest_house:
        querystring['guest_house'] = guest_house
    if fixer_upper:
        querystring['fixer_upper'] = fixer_upper
    if keyword_search:
        querystring['keyword_search'] = keyword_search
    if primary_bed_on_main:
        querystring['primary_bed_on_main'] = primary_bed_on_main
    if air_conditioning:
        querystring['air_conditioning'] = air_conditioning
    if has_exclude_55_communities:
        querystring['has_exclude_55_communities'] = has_exclude_55_communities
    if min_year_built:
        querystring['min_year_built'] = min_year_built
    if max_price:
        querystring['max_price'] = max_price
    if sort:
        querystring['sort'] = sort
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-base.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def auto_complete(location: str='01026', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "You send a request and receive the following information:
		- `id`: The unique identifier for the city.
		- `type`: The type of the city.
		- `name`: The name of the city.
		- `subName`: The additional description of the city.
		- `url`: The direct URL to access the city's information page on Redfin.com.
		- `active`: The active status of the city.
		- `claimedHome`: The status of claimed home ownership.
		- `invalidMRS`: The invalid MRS (Market Revenue Share) status.
		- `businessMarketIds`: The list of relevant business market IDs.
		- `countryCode`: The country code.
		- `internalSearchVolume`: The internal search volume statistic."
    location: **Input**: City, Address, School, Agent, ZIP
        
    """
    url = f"https://redfin-base.p.rapidapi.com/WebAPIs/redfin/locationAutocomplete"
    querystring = {}
    if location:
        querystring['location'] = location
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-base.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_region_info(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API will return `region_type_id`, `region_id`
		➞ Will use for API 【Search by region】"
    url: The input value can be full URL or sub URL
- **Full URL**: `https://www.redfin.com/zipcode/01026`
- **Sub URL**: `/zipcode/01026` (use the Auto-complete API to get the value, it is a property URL)
        
    """
    url = f"https://redfin-base.p.rapidapi.com/WebAPIs/redfin/regionInfo"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-base.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_by_region(region_type: int, region_id: int, financing_type: str=None, hoa_feets: int=None, min_price_per_sqft: int=None, property_tax: int=None, max_price_per_sqft: int=None, has_exclude_55_communities: bool=None, min_sqft: int=None, price_reduced: str=None, excl_ll: bool=None, max_year_built: int=None, elevator: bool=None, max_sqft: int=None, dogs_allowed: bool=None, garage_spots: str=None, min_year_built: int=None, fireplace: bool=None, home_type: str=None, primary_bed_on_main: bool=None, accessible_home: bool=None, keyword_search: str=None, guest_house: bool=None, green_home: bool=None, fixer_upper: bool=None, pets_allowed: bool=None, has_view: bool=None, washer_dryer_hookup: bool=None, waterfront: bool=None, air_conditioning: bool=None, pool_types: str=None, include_outdoor_parking: bool=None, basement_types: str=None, max_lot_size: int=None, min_stories: int=None, max_stories: int=None, min_lot_size: int=None, time_on_redfin: str=None, cats_allowed: bool=None, max_num_beds: int=None, num_baths: int=None, min_num_beds: int=None, min_price: int=None, max_price: int=None, sort: str=None, sold_within_days: str=None, status: str='active,comingsoon', search_type: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search by region"
    region_type: One of the following :       
` -1`: Unknowns |   `1`: Neighborhood
`2`: Zip Code  |   `4`: State
`5`: County |   `6`: City
`7`: School|   `8`: School District
`9`: Service Region|  `10`: Minor Civil Division
`11`: Country|  `30`: CA Postal Code
`31`: CA Province|  `32`:  CA Provincial Division
`33`: CA Municipality|   `34`: CA Forward Sortation Area
Or Use API 【**Get region info**】to get   `region_type_id`
        region_id: Use the【Get region info】API to get the `region_id  ` value.
        financing_type: Accepted financing
        hoa_feets: Suggested Values:
`0`: No HOA Fee ❚ `25`: $25/month
`50`: $50/month ❚ `75`: $75/month
`100`: $100/month❚  `150`: $150/month
`200`: $200/month ❚ `250`: $250/month
 `300`: $300/month ❚ `400`: $400/month
 `500`: $500/month ❚ `600`: $600/month
 `700`: $700/month ❚ `800`: $800/month
 `900`: $900/month ❚`1000`: $1000/month
 `1250`: $1250/month ❚ `1500`: $1500/month
 `1750`: $1750/month ❚`2000`: $2000/month
 `2500`: $2500/month ❚ `3000`: $3000/month
 `3500`: $3500/month ❚ `4000`: $4000/month
 `4500`: $4500/month ❚ `5000`: $5000/month
        min_price_per_sqft: Price/Sq. ft.
Suggested Values:  `50`, `100`, `150`, `200`, `250`, `300`, `400`, `500`, `600`, `800`, `1000`, `1400`, `1800`, `2200`, `2600`, `3000`
        property_tax: COMMENT:
Suggested Values:
`0`: No property taxes ❚`250`: $250/year
`500`: $500/year❚`750`: $750/year
`1000`: $1,000/year❚`1250`: $1,250/year
`1500`: $1,500/year❚`1750`: $1,750/year
`2000`: $2,000/year❚`2500`: $2,500/year
`3000`: $3,000/year❚`3500`: $3,500/year
`4000`: $4,000/year❚`4500`: $4,500/year
`5000`: $5,000/year❚`5500`: $5,500/year
`6000`: $6,000/year❚`6500`: $6,500/year
`7000`: $7,000/year❚`8000`: $8,000/year
`10000`: $10,000/year❚`12000`: $12,000/year
`14000`: $14,000/year❚`16000`: $16,000/year
`20000`: $20,000/year❚`24000`: $24,000/year

        max_price_per_sqft: Price/Sq. ft.
Suggested Values:  `50`, `100`, `150`, `200`, `250`, `300`, `400`, `500`, `600`, `800`, `1000`, `1400`, `1800`, `2200`, `2600`, `3000`
        min_sqft: Suggested Values: `750`, `1000`, `1100`, `1200`, `1300`, `1400`, `1500`, `1600`, `1700`, `1800`, `1900`, `2000`, `2250`, `2500`, `2750`, `3000`, `4000`, `5000`, `7500`, `10000`
        excl_ll: Exclude land leases
        max_sqft: Suggested Values: `750`, `1000`, `1100`, `1200`, `1300`, `1400`, `1500`, `1600`, `1700`, `1800`, `1900`, `2000`, `2250`, `2500`, `2750`, `3000`, `4000`, `5000`, `7500`, `10000`
        dogs_allowed: For `search_type `＝**ForRent**
        home_type: Enter the parameters below:
For `search_type `＝ **ForSale** OR **Sold**
  ● House
  ● Townhouse
  ● Condo
  ● Land
  ● MultiFamily
  ● Mobile
  ● Coop
  ● Other
For `search_type `＝ **ForRent**
  ● Apartment
※ Separated by a comma for multiple options
EX: House, Townhouse
        keyword_search: E.g. office, balcony, modern,place
        include_outdoor_parking: 【Include outdoor parking】 value is reflected when at 【Garage spots】 is selected
        basement_types: Enter the parameters below:
  ● Finished
  ● Unfinished
※ Separated by a comma for multiple options
EX: Finished, Unfinished
        max_lot_size: Suggested Values:
`2000`＝2,000 sqft❚`4500`＝4,500 sqft
`6500`＝6,500 sqft❚`8000`＝8,000 sqft
`9500`＝9,500 sqft❚`10890`＝25 acres
`21780`＝5 acres❚`43560`＝1 acre
`87120`＝2 acres❚`130680`＝3 acres
 `174240`＝4 acres❚`217800`＝5 acres
 `435600`＝10 acres❚ `871200`＝20 acres
`1742400`＝40 acres❚ `4356000`＝100 acres
        min_stories: Enter a value in the range 1 ～ 20
        max_stories: Enter a value in the range 1 ～ 20
        min_lot_size: Suggested Values:
`2000`＝2,000 sqft❚`4500`＝4,500 sqft
`6500`＝6,500 sqft❚`8000`＝8,000 sqft
`9500`＝9,500 sqft❚`10890`＝25 acres
`21780`＝5 acres❚`43560`＝1 acre
`87120`＝2 acres❚`130680`＝3 acres
 `174240`＝4 acres❚`217800`＝5 acres
 `435600`＝10 acres❚ `871200`＝20 acres
`1742400`＝40 acres❚ `4356000`＝100 acres
        cats_allowed: For `search_type `＝**ForRent**
        max_num_beds: Enter a value in the range 1 ～ 5
        num_baths: Suggested Values: `1`, `1.5`, `2`, `2.5`, `3.4`
        min_num_beds: Enter a value in the range 1 ～ 5
        max_price: Filter by price
        sort: Default ＝ Recommended
        sold_within_days: Default ＝ Last_3_months
For `search_type `＝**Sold**

        status: For search_type ＝**ForSale**

Enter the parameters below: 
● active
● comingsoon
● undercontract_pending
※ Separated by a comma for multiple options
EX: active, comingsoon
        search_type: Default＝**ForSale**
        
    """
    url = f"https://redfin-base.p.rapidapi.com/WebAPIs/redfin/searchByRegion"
    querystring = {'region_type': region_type, 'region_id': region_id, }
    if financing_type:
        querystring['financing_type'] = financing_type
    if hoa_feets:
        querystring['hoa_feets'] = hoa_feets
    if min_price_per_sqft:
        querystring['min_price_per_sqft'] = min_price_per_sqft
    if property_tax:
        querystring['property_tax'] = property_tax
    if max_price_per_sqft:
        querystring['max_price_per_sqft'] = max_price_per_sqft
    if has_exclude_55_communities:
        querystring['has_exclude_55_communities'] = has_exclude_55_communities
    if min_sqft:
        querystring['min_sqft'] = min_sqft
    if price_reduced:
        querystring['price_reduced'] = price_reduced
    if excl_ll:
        querystring['excl_ll'] = excl_ll
    if max_year_built:
        querystring['max_year_built'] = max_year_built
    if elevator:
        querystring['elevator'] = elevator
    if max_sqft:
        querystring['max_sqft'] = max_sqft
    if dogs_allowed:
        querystring['dogs_allowed'] = dogs_allowed
    if garage_spots:
        querystring['garage_spots'] = garage_spots
    if min_year_built:
        querystring['min_year_built'] = min_year_built
    if fireplace:
        querystring['fireplace'] = fireplace
    if home_type:
        querystring['home_type'] = home_type
    if primary_bed_on_main:
        querystring['primary_bed_on_main'] = primary_bed_on_main
    if accessible_home:
        querystring['accessible_home'] = accessible_home
    if keyword_search:
        querystring['keyword_search'] = keyword_search
    if guest_house:
        querystring['guest_house'] = guest_house
    if green_home:
        querystring['green_home'] = green_home
    if fixer_upper:
        querystring['fixer_upper'] = fixer_upper
    if pets_allowed:
        querystring['pets_allowed'] = pets_allowed
    if has_view:
        querystring['has_view'] = has_view
    if washer_dryer_hookup:
        querystring['washer_dryer_hookup'] = washer_dryer_hookup
    if waterfront:
        querystring['waterfront'] = waterfront
    if air_conditioning:
        querystring['air_conditioning'] = air_conditioning
    if pool_types:
        querystring['pool_types'] = pool_types
    if include_outdoor_parking:
        querystring['include_outdoor_parking'] = include_outdoor_parking
    if basement_types:
        querystring['basement_types'] = basement_types
    if max_lot_size:
        querystring['max_lot_size'] = max_lot_size
    if min_stories:
        querystring['min_stories'] = min_stories
    if max_stories:
        querystring['max_stories'] = max_stories
    if min_lot_size:
        querystring['min-lot-size'] = min_lot_size
    if time_on_redfin:
        querystring['time_on_redfin'] = time_on_redfin
    if cats_allowed:
        querystring['cats_allowed'] = cats_allowed
    if max_num_beds:
        querystring['max_num_beds'] = max_num_beds
    if num_baths:
        querystring['num_baths'] = num_baths
    if min_num_beds:
        querystring['min_num_beds'] = min_num_beds
    if min_price:
        querystring['min_price'] = min_price
    if max_price:
        querystring['max_price'] = max_price
    if sort:
        querystring['sort'] = sort
    if sold_within_days:
        querystring['sold_within_days'] = sold_within_days
    if status:
        querystring['status'] = status
    if search_type:
        querystring['search_type'] = search_type
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "redfin-base.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

