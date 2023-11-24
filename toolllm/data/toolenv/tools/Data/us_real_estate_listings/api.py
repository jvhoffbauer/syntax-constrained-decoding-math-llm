import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_a_property_list_for_sale_by_parameters_zip_address_radius(location: str, foreclosure: bool=None, outside_features: str=None, price_reduced: bool=None, hide_pending_contingent: bool=None, lot_size_max: int=None, hoa_max: int=None, existing: bool=None, community_ammenities: str=None, hide_foreclosure: bool=None, has_virtual_tours: bool=None, expand_search_radius: str=None, open_house: bool=None, no_hoa_fee: bool=None, year_built_max: int=None, has_3d_tours: bool=None, days_on: str=None, lot_size_min: int=None, year_built_min: int=None, home_size_max: int=None, new_construction: bool=None, home_size_min: int=None, baths_min: int=None, beds_min: int=None, beds_max: int=None, baths_max: int=None, sort: str=None, price_min: int=None, offset: int=0, price_max: int=None, property_type: str=None, limit: int=50, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a property list for sale by parameters.
		Let me know if you need any other parameters."
    location: Location: city or zip or address
        outside_features: - `swimming_pool`
- `spa_or_hot_tub`
- `horse_facilities`

For multiple selections, use comma separate values: `swimming_pool,spa_or_hot_tub`
        hoa_max: Maximum HOA fee in USD
        existing: Existing Homes
        community_ammenities: - `community_swimming_pool`
- `community_spa_or_hot_tub`
- `community_golf`
- `community_security_features`
- `community_boat_facilities`
- `tennis_court`
- `community_clubhouse`
- `senior_community`

For multiple selections, use comma separate values: `senior_community,community_clubhouse`
        expand_search_radius: Expand search radius
        no_hoa_fee: `true` for properties without HOA fee only.
        year_built_max: Maximum home age
        lot_size_min: Minimum lot size in sqft.
        year_built_min: Minimum home age
        home_size_max: Maximum home size (sqft)
        new_construction: `true` for New construction only. Leave it blank for any
        home_size_min: Minimum home size (sqft)
        baths_min: Bathrooms
        beds_min: Minimum bedrooms
        beds_max: Maximum bedrooms
        baths_max: Bathrooms
        sort: - `relevance` - **default**
- `price_low_to_high`
- `price_high_to_low`
- `number_of_photos`
- `newest`
- `largest_sqft`
- `price_reduced_date`
        price_min: Minimum listing price (USD)
        offset: Offset results, default 0. Maximum 9800
        price_max: Maximum listing price (USD)
        property_type: If empty, all available types will be searched. 

Available types:
- `single_family`
- `condos`
- `townhome`
- `multi_family`
- `mobile`
- `farm`
- `land`

For multiple selections, use comma separate values: `condos,multi_family`
        limit: The number of results. Maximum 200, default 50
        
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/for-sale"
    querystring = {'location': location, }
    if foreclosure:
        querystring['foreclosure'] = foreclosure
    if outside_features:
        querystring['outside_features'] = outside_features
    if price_reduced:
        querystring['price_reduced'] = price_reduced
    if hide_pending_contingent:
        querystring['hide_pending_contingent'] = hide_pending_contingent
    if lot_size_max:
        querystring['lot_size_max'] = lot_size_max
    if hoa_max:
        querystring['hoa_max'] = hoa_max
    if existing:
        querystring['existing'] = existing
    if community_ammenities:
        querystring['community_ammenities'] = community_ammenities
    if hide_foreclosure:
        querystring['hide_foreclosure'] = hide_foreclosure
    if has_virtual_tours:
        querystring['has_virtual_tours'] = has_virtual_tours
    if expand_search_radius:
        querystring['expand_search_radius'] = expand_search_radius
    if open_house:
        querystring['open_house'] = open_house
    if no_hoa_fee:
        querystring['no_hoa_fee'] = no_hoa_fee
    if year_built_max:
        querystring['year_built_max'] = year_built_max
    if has_3d_tours:
        querystring['has_3d_tours'] = has_3d_tours
    if days_on:
        querystring['days_on'] = days_on
    if lot_size_min:
        querystring['lot_size_min'] = lot_size_min
    if year_built_min:
        querystring['year_built_min'] = year_built_min
    if home_size_max:
        querystring['home_size_max'] = home_size_max
    if new_construction:
        querystring['new_construction'] = new_construction
    if home_size_min:
        querystring['home_size_min'] = home_size_min
    if baths_min:
        querystring['baths_min'] = baths_min
    if beds_min:
        querystring['beds_min'] = beds_min
    if beds_max:
        querystring['beds_max'] = beds_max
    if baths_max:
        querystring['baths_max'] = baths_max
    if sort:
        querystring['sort'] = sort
    if price_min:
        querystring['price_min'] = price_min
    if offset:
        querystring['offset'] = offset
    if price_max:
        querystring['price_max'] = price_max
    if property_type:
        querystring['property_type'] = property_type
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def discover_just_sold_homes_and_properties(location: str, lot_size_max: int=None, lot_size_min: int=None, home_size_max: int=None, beds_max: int=None, baths_min: int=None, home_size_min: int=None, beds_min: int=None, limit: int=50, sort: str=None, year_built_min: int=None, year_built_max: int=None, property_type: str=None, offset: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Discover just sold homes and properties"
    location: Location: city or zip or address
        lot_size_max: Maximum lot size (sqft)
        lot_size_min: Minimum lot size (sqft)
        home_size_max: Maximum home size (sqft)
        home_size_min: Minimum home size (sqft)
        limit: The number of results. Maximum 200, default 50
        sort: Default `price_high_to_low`
        property_type: If empty, all available types will be searched. 

- `multi_family`
- `single_family`
- `mobile`
- `land`
- `farm`
- `condos`
- `townhome`

For multiple selections, use comma separate values: `condos,multi_family`
        offset: Offset results, default 0. Maximum 9800
        
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/sold-homes"
    querystring = {'location': location, }
    if lot_size_max:
        querystring['lot_size_max'] = lot_size_max
    if lot_size_min:
        querystring['lot_size_min'] = lot_size_min
    if home_size_max:
        querystring['home_size_max'] = home_size_max
    if beds_max:
        querystring['beds_max'] = beds_max
    if baths_min:
        querystring['baths_min'] = baths_min
    if home_size_min:
        querystring['home_size_min'] = home_size_min
    if beds_min:
        querystring['beds_min'] = beds_min
    if limit:
        querystring['limit'] = limit
    if sort:
        querystring['sort'] = sort
    if year_built_min:
        querystring['year_built_min'] = year_built_min
    if year_built_max:
        querystring['year_built_max'] = year_built_max
    if property_type:
        querystring['property_type'] = property_type
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_the_property_details_using_mls_id(mlsid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the property details using MLS id."
    mlsid: e.g., F10361904 Or 2314318
        
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/property-by-mls"
    querystring = {'mlsId': mlsid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def agent_listings(member_id: str, abbreviation: str, advertiser_id: int, type: str=None, page: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get agent's listings."
    member_id: Agent's mls data from `/agent/profile`
        abbreviation: Agent's mls data from `/agent/profile`
        type: Default `all`.
        
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/agent/listings"
    querystring = {'member_id': member_id, 'abbreviation': abbreviation, 'advertiser_id': advertiser_id, }
    if type:
        querystring['type'] = type
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def agent_find(zip: str, price_max: int=None, price_min: int=None, recommendations_count_min: int=None, agent_rating_min: int=None, name: str=None, agent_type: str=None, sort: str=None, types: str=None, limit: int=20, offset: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for agents, teams, and offices by zip code and name."
    price_max: Option filter by setting max price
        price_min: Option filter by setting min price
        recommendations_count_min: Number of recommendations (max 10)
        agent_rating_min: Rating (max 5)
        limit: For paging purpose (max 20)
        offset: The offset of items to be ignored in response for paging
        
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/agent/find"
    querystring = {'zip': zip, }
    if price_max:
        querystring['price_max'] = price_max
    if price_min:
        querystring['price_min'] = price_min
    if recommendations_count_min:
        querystring['recommendations_count_min'] = recommendations_count_min
    if agent_rating_min:
        querystring['agent_rating_min'] = agent_rating_min
    if name:
        querystring['name'] = name
    if agent_type:
        querystring['agent_type'] = agent_type
    if sort:
        querystring['sort'] = sort
    if types:
        querystring['types'] = types
    if limit:
        querystring['limit'] = limit
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def agent_recommendations(advertiser_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get agent's recommendations"
    
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/agent/recommendations"
    querystring = {'advertiser_id': advertiser_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def agent_reviews(advertiser_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get agent reviews"
    
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/agent/reviews"
    querystring = {'advertiser_id': advertiser_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def agent_profile(advertiser_id: int, nrds_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get agent's profile."
    
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/agent/profile"
    querystring = {'advertiser_id': advertiser_id, 'nrds_id': nrds_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_a_property_list_for_rent_by_parameters(location: str, beds_max: int=None, days_on: str=None, price_max: int=None, home_size_min: int=None, price_min: int=None, home_size_max: int=None, baths_max: int=None, baths_min: int=None, beds_min: int=None, property_type: str=None, offset: int=0, sort: str=None, limit: int=50, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a property list for rent by parameters.
		Let me know if you need any other parameters."
    location: Location: city or zip or address
        property_type: If empty, all available types will be searched. 

Available types:
- `apartment`
- `single_family`
- `condos`
- `townhome`
-  `other`

For multiple selections, use comma separate values: `condos,multi_family`
        offset: Offset results, default 0. Maximum 9800
        sort: - `relevance` - **default**
- `price_high_to_low`
- `price_low_to_high`
- `number_of_photos`
- `newest`
        limit: The number of results. Maximum 200, default 50
        
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/for-rent"
    querystring = {'location': location, }
    if beds_max:
        querystring['beds_max'] = beds_max
    if days_on:
        querystring['days_on'] = days_on
    if price_max:
        querystring['price_max'] = price_max
    if home_size_min:
        querystring['home_size_min'] = home_size_min
    if price_min:
        querystring['price_min'] = price_min
    if home_size_max:
        querystring['home_size_max'] = home_size_max
    if baths_max:
        querystring['baths_max'] = baths_max
    if baths_min:
        querystring['baths_min'] = baths_min
    if beds_min:
        querystring['beds_min'] = beds_min
    if property_type:
        querystring['property_type'] = property_type
    if offset:
        querystring['offset'] = offset
    if sort:
        querystring['sort'] = sort
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_the_property_details_by_property_id(is_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the property details by property_id."
    
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/property"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_location_suggestion(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Location suggestion. Data used in other endpoints."
    
    """
    url = f"https://us-real-estate-listings.p.rapidapi.com/location-suggest"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

