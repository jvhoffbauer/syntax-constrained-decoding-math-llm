import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_property_by_geo(locale: str, swlat: int, nelng: int, nelat: int, swlng: int, currency: str, has_step_free_shower: bool=None, has_step_free_guest_entrance: bool=None, children: int=None, has_crib: bool=None, has_self_check_in: bool=None, has_carbon_monoxide_alarm: bool=None, has_accessible_parking_spot: bool=None, has_instant_book: bool=None, has_step_free_bathroom_access: bool=None, has_guest_entrance_wider_than_32_inches: bool=None, has_shower_or_bath_chair: bool=None, has_hot_tub: bool=None, has_hair_dryer: bool=None, has_smoke_alarm: bool=None, has_indoor_fireplace: bool=None, has_dryer: bool=None, has_shower_grab_bar: bool=None, has_tv: bool=None, has_bedroom_entrance_wider_than_32_inches: bool=None, has_iron: bool=None, has_step_free_path_to_the_guest_entrance: bool=None, has_breakfast: bool=None, has_smoking_allowed: bool=None, has_step_free_bedroom_access: bool=None, pets: int=None, max_price: int=None, has_pool: bool=None, has_free_parking: bool=None, has_kitchen: bool=None, has_bbq_grill: bool=None, has_gym: bool=None, has_ev_charger: bool=None, min_bathroom: int=None, property_type: str=None, adults: int=None, has_dedicated_workspace: bool=None, infants: int=None, min_bed: int=None, has_private_room: bool=None, min_bedroom: int=None, has_shared_room: bool=None, has_entire_place: bool=None, checkin: str=None, page: int=None, checkout: str=None, category: str=None, has_bathroom_entrance_wider_than_32_inches: bool=None, has_toilet_grab_bar: bool=None, has_superhost: bool=None, has_wifi: bool=None, has_air_conditioning: bool=None, has_washer: bool=None, min_price: int=None, has_heating: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Property By GEO"
    locale: id item from the Get Languages API
        currency: id item from the Get Currency API
        property_type: Property type comma-separated or empty for all types:
Ex: House,Apartment,Guesthouse,Hotel

- House
- Apartment
- Guesthouse
- Hotel
        checkin: Format: YYYY-MM-DD
        checkout: Format: YYYY-MM-DD
        category: Response from this API: data->categories-> id
Ex: Tag:677
        
    """
    url = f"https://airbnb-search.p.rapidapi.com/property/search-geo"
    querystring = {'locale': locale, 'swLat': swlat, 'neLng': nelng, 'neLat': nelat, 'swLng': swlng, 'currency': currency, }
    if has_step_free_shower:
        querystring['has_step_free_shower'] = has_step_free_shower
    if has_step_free_guest_entrance:
        querystring['has_step_free_guest_entrance'] = has_step_free_guest_entrance
    if children:
        querystring['children'] = children
    if has_crib:
        querystring['has_crib'] = has_crib
    if has_self_check_in:
        querystring['has_self_check_in'] = has_self_check_in
    if has_carbon_monoxide_alarm:
        querystring['has_carbon_monoxide_alarm'] = has_carbon_monoxide_alarm
    if has_accessible_parking_spot:
        querystring['has_accessible_parking_spot'] = has_accessible_parking_spot
    if has_instant_book:
        querystring['has_instant_book'] = has_instant_book
    if has_step_free_bathroom_access:
        querystring['has_step_free_bathroom_access'] = has_step_free_bathroom_access
    if has_guest_entrance_wider_than_32_inches:
        querystring['has_guest_entrance_wider_than_32_inches'] = has_guest_entrance_wider_than_32_inches
    if has_shower_or_bath_chair:
        querystring['has_shower_or_bath_chair'] = has_shower_or_bath_chair
    if has_hot_tub:
        querystring['has_hot_tub'] = has_hot_tub
    if has_hair_dryer:
        querystring['has_hair_dryer'] = has_hair_dryer
    if has_smoke_alarm:
        querystring['has_smoke_alarm'] = has_smoke_alarm
    if has_indoor_fireplace:
        querystring['has_indoor_fireplace'] = has_indoor_fireplace
    if has_dryer:
        querystring['has_dryer'] = has_dryer
    if has_shower_grab_bar:
        querystring['has_shower_grab_bar'] = has_shower_grab_bar
    if has_tv:
        querystring['has_tv'] = has_tv
    if has_bedroom_entrance_wider_than_32_inches:
        querystring['has_bedroom_entrance_wider_than_32_inches'] = has_bedroom_entrance_wider_than_32_inches
    if has_iron:
        querystring['has_iron'] = has_iron
    if has_step_free_path_to_the_guest_entrance:
        querystring['has_step_free_path_to_the_guest_entrance'] = has_step_free_path_to_the_guest_entrance
    if has_breakfast:
        querystring['has_breakfast'] = has_breakfast
    if has_smoking_allowed:
        querystring['has_smoking_allowed'] = has_smoking_allowed
    if has_step_free_bedroom_access:
        querystring['has_step_free_bedroom_access'] = has_step_free_bedroom_access
    if pets:
        querystring['pets'] = pets
    if max_price:
        querystring['max_price'] = max_price
    if has_pool:
        querystring['has_pool'] = has_pool
    if has_free_parking:
        querystring['has_free_parking'] = has_free_parking
    if has_kitchen:
        querystring['has_kitchen'] = has_kitchen
    if has_bbq_grill:
        querystring['has_bbq_grill'] = has_bbq_grill
    if has_gym:
        querystring['has_gym'] = has_gym
    if has_ev_charger:
        querystring['has_ev_charger'] = has_ev_charger
    if min_bathroom:
        querystring['min_bathroom'] = min_bathroom
    if property_type:
        querystring['property_type'] = property_type
    if adults:
        querystring['adults'] = adults
    if has_dedicated_workspace:
        querystring['has_dedicated_workspace'] = has_dedicated_workspace
    if infants:
        querystring['infants'] = infants
    if min_bed:
        querystring['min_bed'] = min_bed
    if has_private_room:
        querystring['has_private_room'] = has_private_room
    if min_bedroom:
        querystring['min_bedroom'] = min_bedroom
    if has_shared_room:
        querystring['has_shared_room'] = has_shared_room
    if has_entire_place:
        querystring['has_entire_place'] = has_entire_place
    if checkin:
        querystring['checkin'] = checkin
    if page:
        querystring['page'] = page
    if checkout:
        querystring['checkout'] = checkout
    if category:
        querystring['category'] = category
    if has_bathroom_entrance_wider_than_32_inches:
        querystring['has_bathroom_entrance_wider_than_32_inches'] = has_bathroom_entrance_wider_than_32_inches
    if has_toilet_grab_bar:
        querystring['has_toilet_grab_bar'] = has_toilet_grab_bar
    if has_superhost:
        querystring['has_superhost'] = has_superhost
    if has_wifi:
        querystring['has_wifi'] = has_wifi
    if has_air_conditioning:
        querystring['has_air_conditioning'] = has_air_conditioning
    if has_washer:
        querystring['has_washer'] = has_washer
    if min_price:
        querystring['min_price'] = min_price
    if has_heating:
        querystring['has_heating'] = has_heating
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "airbnb-search.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_property(locale: str, currency: str, query: str, has_private_room: bool=None, page: int=None, has_ceiling_or_mobile_hoist: bool=None, has_smoke_alarm: bool=None, has_step_free_shower: bool=None, has_step_free_bedroom_access: bool=None, has_shower_or_bath_chair: bool=None, has_bedroom_entrance_wider_than_32_inches: bool=None, has_carbon_monoxide_alarm: bool=None, has_indoor_fireplace: bool=None, has_breakfast: bool=None, has_self_check_in: bool=None, has_toilet_grab_bar: bool=None, has_step_free_path_to_the_guest_entrance: bool=None, has_instant_book: bool=None, has_gym: bool=None, has_accessible_parking_spot: bool=None, has_guest_entrance_wider_than_32_inches: bool=None, has_ev_charger: bool=None, has_crib: bool=None, has_superhost: bool=None, has_bbq_grill: bool=None, has_shower_grab_bar: bool=None, has_step_free_guest_entrance: bool=None, has_step_free_bathroom_access: bool=None, has_bathroom_entrance_wider_than_32_inches: bool=None, has_smoking_allowed: bool=None, category: str=None, has_heating: bool=None, has_washer: bool=None, has_kitchen: bool=None, has_tv: bool=None, has_iron: bool=None, has_air_conditioning: bool=None, has_hot_tub: bool=None, has_dedicated_workspace: bool=None, has_free_parking: bool=None, has_wifi: bool=None, has_pool: bool=None, has_hair_dryer: bool=None, has_dryer: bool=None, min_bathroom: int=None, min_bed: int=None, property_type: str=None, has_shared_room: bool=None, has_entire_place: bool=None, min_bedroom: int=None, pets: int=None, max_price: int=None, min_price: int=None, checkout: str=None, checkin: str=None, children: int=None, adults: int=None, infants: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search Property"
    locale: id item from the Get Languages API
        currency: id item from the Get Currency API
        category: Response from this API: data->categories-> id
Ex: Tag:677
        property_type: Property type comma-separated or empty for all types:
Ex: House,Apartment,Guesthouse,Hotel

- House
- Apartment
- Guesthouse
- Hotel
        checkout: Format: YYYY-MM-DD
        checkin: Format: YYYY-MM-DD
        
    """
    url = f"https://airbnb-search.p.rapidapi.com/property/search"
    querystring = {'locale': locale, 'currency': currency, 'query': query, }
    if has_private_room:
        querystring['has_private_room'] = has_private_room
    if page:
        querystring['page'] = page
    if has_ceiling_or_mobile_hoist:
        querystring['has_ceiling_or_mobile_hoist'] = has_ceiling_or_mobile_hoist
    if has_smoke_alarm:
        querystring['has_smoke_alarm'] = has_smoke_alarm
    if has_step_free_shower:
        querystring['has_step_free_shower'] = has_step_free_shower
    if has_step_free_bedroom_access:
        querystring['has_step_free_bedroom_access'] = has_step_free_bedroom_access
    if has_shower_or_bath_chair:
        querystring['has_shower_or_bath_chair'] = has_shower_or_bath_chair
    if has_bedroom_entrance_wider_than_32_inches:
        querystring['has_bedroom_entrance_wider_than_32_inches'] = has_bedroom_entrance_wider_than_32_inches
    if has_carbon_monoxide_alarm:
        querystring['has_carbon_monoxide_alarm'] = has_carbon_monoxide_alarm
    if has_indoor_fireplace:
        querystring['has_indoor_fireplace'] = has_indoor_fireplace
    if has_breakfast:
        querystring['has_breakfast'] = has_breakfast
    if has_self_check_in:
        querystring['has_self_check_in'] = has_self_check_in
    if has_toilet_grab_bar:
        querystring['has_toilet_grab_bar'] = has_toilet_grab_bar
    if has_step_free_path_to_the_guest_entrance:
        querystring['has_step_free_path_to_the_guest_entrance'] = has_step_free_path_to_the_guest_entrance
    if has_instant_book:
        querystring['has_instant_book'] = has_instant_book
    if has_gym:
        querystring['has_gym'] = has_gym
    if has_accessible_parking_spot:
        querystring['has_accessible_parking_spot'] = has_accessible_parking_spot
    if has_guest_entrance_wider_than_32_inches:
        querystring['has_guest_entrance_wider_than_32_inches'] = has_guest_entrance_wider_than_32_inches
    if has_ev_charger:
        querystring['has_ev_charger'] = has_ev_charger
    if has_crib:
        querystring['has_crib'] = has_crib
    if has_superhost:
        querystring['has_superhost'] = has_superhost
    if has_bbq_grill:
        querystring['has_bbq_grill'] = has_bbq_grill
    if has_shower_grab_bar:
        querystring['has_shower_grab_bar'] = has_shower_grab_bar
    if has_step_free_guest_entrance:
        querystring['has_step_free_guest_entrance'] = has_step_free_guest_entrance
    if has_step_free_bathroom_access:
        querystring['has_step_free_bathroom_access'] = has_step_free_bathroom_access
    if has_bathroom_entrance_wider_than_32_inches:
        querystring['has_bathroom_entrance_wider_than_32_inches'] = has_bathroom_entrance_wider_than_32_inches
    if has_smoking_allowed:
        querystring['has_smoking_allowed'] = has_smoking_allowed
    if category:
        querystring['category'] = category
    if has_heating:
        querystring['has_heating'] = has_heating
    if has_washer:
        querystring['has_washer'] = has_washer
    if has_kitchen:
        querystring['has_kitchen'] = has_kitchen
    if has_tv:
        querystring['has_tv'] = has_tv
    if has_iron:
        querystring['has_iron'] = has_iron
    if has_air_conditioning:
        querystring['has_air_conditioning'] = has_air_conditioning
    if has_hot_tub:
        querystring['has_hot_tub'] = has_hot_tub
    if has_dedicated_workspace:
        querystring['has_dedicated_workspace'] = has_dedicated_workspace
    if has_free_parking:
        querystring['has_free_parking'] = has_free_parking
    if has_wifi:
        querystring['has_wifi'] = has_wifi
    if has_pool:
        querystring['has_pool'] = has_pool
    if has_hair_dryer:
        querystring['has_hair_dryer'] = has_hair_dryer
    if has_dryer:
        querystring['has_dryer'] = has_dryer
    if min_bathroom:
        querystring['min_bathroom'] = min_bathroom
    if min_bed:
        querystring['min_bed'] = min_bed
    if property_type:
        querystring['property_type'] = property_type
    if has_shared_room:
        querystring['has_shared_room'] = has_shared_room
    if has_entire_place:
        querystring['has_entire_place'] = has_entire_place
    if min_bedroom:
        querystring['min_bedroom'] = min_bedroom
    if pets:
        querystring['pets'] = pets
    if max_price:
        querystring['max_price'] = max_price
    if min_price:
        querystring['min_price'] = min_price
    if checkout:
        querystring['checkout'] = checkout
    if checkin:
        querystring['checkin'] = checkin
    if children:
        querystring['children'] = children
    if adults:
        querystring['adults'] = adults
    if infants:
        querystring['infants'] = infants
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "airbnb-search.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def property_details(currency: str, locale: str, is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Property details"
    currency: id item from the Get Currency API
        locale: id item from the Get Languages API
        id: id from search API: data -> homes[index] -> listing -> id
        
    """
    url = f"https://airbnb-search.p.rapidapi.com/property/detail"
    querystring = {'currency': currency, 'locale': locale, 'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "airbnb-search.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def autocomplete(locale: str, currency: str, query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Find location for search"
    locale: id item from the Get Languages API
        currency: id item from the Get Currency API
        
    """
    url = f"https://airbnb-search.p.rapidapi.com/autocomplete"
    querystring = {'locale': locale, 'currency': currency, 'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "airbnb-search.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_currency(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Currency"
    
    """
    url = f"https://airbnb-search.p.rapidapi.com/currency"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "airbnb-search.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_languages(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get languages"
    
    """
    url = f"https://airbnb-search.p.rapidapi.com/languages"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "airbnb-search.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

