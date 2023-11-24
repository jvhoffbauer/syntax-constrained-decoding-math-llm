import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def matrix(coordinates: str, radiuses: str='"500;200;300"', annotations: str='"distance"', fallback_coordinate: str='"snapped"', generate_hints: str='"false"', fallback_speed: int=None, sources: int=0, exclude: str='"toll"', destinations: int=2, bearings: str='"10,20;40,30;30,9"', approaches: str='"curb;curb;curb"', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Computes duration of the fastest route between all pairs of supplied coordinates. Returns the durations or distances or both between the coordinate pairs. Note that the distances are not the shortest distance between two coordinates, but rather the distances of the fastest routes."
    coordinates: String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5
        radiuses: Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default)
        annotations: Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ]
        fallback_coordinate: When using a fallback_speed, use the user-supplied coordinate (input), or the snapped location (snapped) for calculating distances. [ input (default), or snapped ]
        generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String
        fallback_speed: If no route found between a source/destination pair, calculate the as-the-crow-flies distance,  then use this speed to estimate duration. double > 0
        sources: Use location with given index as source. [ {index};{index}[;{index} ...] or all (default) ] => index	 0 <= integer < #locations
        exclude: Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none.
        destinations: Use location with given index as destination. [ {index};{index}[;{index} ...] or all (default) ]
        bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array.
Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing	{value},{range} integer 0 .. 360,integer 0 .. 180
        approaches: Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default)
        
    """
    url = f"https://locationiq2.p.rapidapi.com/matrix/driving/{coordinates}"
    querystring = {}
    if radiuses:
        querystring['radiuses'] = radiuses
    if annotations:
        querystring['annotations'] = annotations
    if fallback_coordinate:
        querystring['fallback_coordinate'] = fallback_coordinate
    if generate_hints:
        querystring['generate_hints'] = generate_hints
    if fallback_speed:
        querystring['fallback_speed'] = fallback_speed
    if sources:
        querystring['sources'] = sources
    if exclude:
        querystring['exclude'] = exclude
    if destinations:
        querystring['destinations'] = destinations
    if bearings:
        querystring['bearings'] = bearings
    if approaches:
        querystring['approaches'] = approaches
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "locationiq2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def autocomplete(normalizecity: int, q: str, viewbox: str='"-132.84908,47.69382,-70.44674,30.82531"', limit: int=10, countrycodes: str='"us"', tag: str='"place"', accept_language: str='"en"', bounded: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Autocomplete API is a variant of the Search API that returns place predictions in response to an HTTP request.  The request specifies a textual search string and optional geographic bounds.  The service can be used to provide autocomplete functionality for text-based geographic searches, by returning places such as businesses, addresses and points of interest as a user types. The Autocomplete API can match on full words as well as substrings. Applications can therefore send queries as the user types, to provide on-the-fly place predictions."
    normalizecity: For responses with no city value in the address section, the next available element in this order - city_district, locality, town, borough, municipality, village, hamlet, quarter, neighbourhood - from the address section will be normalized to city. Defaults to 1 for SDKs.
        q: Address to geocode
        viewbox: The preferred area to find search results.  To restrict results to those within the viewbox, use along with the bounded option. Tuple of 4 floats. Any two corner points of the box - `max_lon,max_lat,min_lon,min_lat` or `min_lon,min_lat,max_lon,max_lat` - are accepted in any order as long as they span a real box. 
        limit: Limit the number of returned results. Default is 10.
        countrycodes: Limit search to a list of countries.
        tag: Restricts the autocomplete search results to elements of specific OSM class and type.  Example - To restrict results to only class place and type city: tag=place:city, To restrict the results to all of OSM class place: tag=place
        accept_language: Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native
        bounded: Restrict the results to only items contained with the viewbox
        
    """
    url = f"https://locationiq2.p.rapidapi.com/autocomplete.php"
    querystring = {'normalizecity': normalizecity, 'q': q, }
    if viewbox:
        querystring['viewbox'] = viewbox
    if limit:
        querystring['limit'] = limit
    if countrycodes:
        querystring['countrycodes'] = countrycodes
    if tag:
        querystring['tag'] = tag
    if accept_language:
        querystring['accept-language'] = accept_language
    if bounded:
        querystring['bounded'] = bounded
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "locationiq2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def reverse(normalizecity: int, lat: int, format: str, lon: int, addressdetails: int=1, accept_language: str='"en"', postaladdress: int=0, namedetails: int=0, showdistance: int=0, statecode: int=0, extratags: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Reverse geocoding is the process of converting a coordinate or location (latitude, longitude) to a readable address or place name. This permits the identification of nearby street addresses, places, and/or area subdivisions such as a neighborhood, county, state, or country."
    normalizecity: Normalizes village to city level data to city
        lat: Latitude of the location to generate an address for.
        format: Format to geocode. Only JSON supported for SDKs
        lon: Longitude of the location to generate an address for.
        addressdetails: Include a breakdown of the address into elements. Defaults to 1.
        accept_language: Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native
        postaladdress: Returns address inside the postaladdress key, that is specifically formatted for each country. Currently supported for addresses in Germany. Defaults to 0 [0,1]
        namedetails: Include a list of alternative names in the results. These may include language variants, references, operator and brand.
        showdistance: Returns the straight line distance (meters) between the input location and the result's location. Value is set in the distance key of the response. Defaults to 0 [0,1]
        statecode: Adds state or province code when available to the statecode key inside the address element. Currently supported for addresses in the USA, Canada and Australia. Defaults to 0
        extratags: Include additional information in the result if available, e.g. wikipedia link, opening hours.
        
    """
    url = f"https://locationiq2.p.rapidapi.com/reverse.php"
    querystring = {'normalizecity': normalizecity, 'lat': lat, 'format': format, 'lon': lon, }
    if addressdetails:
        querystring['addressdetails'] = addressdetails
    if accept_language:
        querystring['accept-language'] = accept_language
    if postaladdress:
        querystring['postaladdress'] = postaladdress
    if namedetails:
        querystring['namedetails'] = namedetails
    if showdistance:
        querystring['showdistance'] = showdistance
    if statecode:
        querystring['statecode'] = statecode
    if extratags:
        querystring['extratags'] = extratags
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "locationiq2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def balance(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Balance API provides a count of request credits left in the user's account for the day. Balance is reset at midnight UTC everyday (00:00 UTC)."
    
    """
    url = f"https://locationiq2.p.rapidapi.com/balance.php"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "locationiq2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(q: str, format: str, normalizecity: int, addressdetails: int=1, bounded: int=1, statecode: int=0, limit: int=10, extratags: int=0, postaladdress: int=0, namedetails: int=1, accept_language: str='"en"', countrycodes: str='"us"', dedupe: int=1, matchquality: int=0, viewbox: str='"-132.84908,47.69382,-70.44674,30.82531"', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Search API allows converting addresses, such as a street address, into geographic coordinates (latitude and longitude). These coordinates can serve various use-cases, from placing markers on a map to helping algorithms determine nearby bus stops. This process is also known as Forward Geocoding."
    q: Address to geocode
        format: Format to geocode. Only JSON supported for SDKs
        normalizecity: For responses with no city value in the address section, the next available element in this order - city_district, locality, town, borough, municipality, village, hamlet, quarter, neighbourhood - from the address section will be normalized to city. Defaults to 1 for SDKs.
        addressdetails: Include a breakdown of the address into elements. Defaults to 0.
        bounded: Restrict the results to only items contained with the viewbox
        statecode: Adds state or province code when available to the statecode key inside the address element. Currently supported for addresses in the USA, Canada and Australia. Defaults to 0
        limit: Limit the number of returned results. Default is 10.
        extratags: Include additional information in the result if available, e.g. wikipedia link, opening hours.
        postaladdress: Returns address inside the postaladdress key, that is specifically formatted for each country. Currently supported for addresses in Germany. Defaults to 0 [0,1]
        namedetails: Include a list of alternative names in the results. These may include language variants, references, operator and brand.
        accept_language: Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native
        countrycodes: Limit search to a list of countries.
        dedupe: Sometimes you have several objects in OSM identifying the same place or object in reality. The simplest case is a street being split in many different OSM ways due to different characteristics. Nominatim will attempt to detect such duplicates and only return one match; this is controlled by the dedupe parameter which defaults to 1. Since the limit is, for reasons of efficiency, enforced before and not after de-duplicating, it is possible that de-duplicating leaves you with less results than requested.
        matchquality: Returns additional information about quality of the result in a matchquality object. Read more Defaults to 0 [0,1]
        viewbox: The preferred area to find search results.  To restrict results to those within the viewbox, use along with the bounded option. Tuple of 4 floats. Any two corner points of the box - `max_lon,max_lat,min_lon,min_lat` or `min_lon,min_lat,max_lon,max_lat` - are accepted in any order as long as they span a real box. 
        
    """
    url = f"https://locationiq2.p.rapidapi.com/search.php"
    querystring = {'q': q, 'format': format, 'normalizecity': normalizecity, }
    if addressdetails:
        querystring['addressdetails'] = addressdetails
    if bounded:
        querystring['bounded'] = bounded
    if statecode:
        querystring['statecode'] = statecode
    if limit:
        querystring['limit'] = limit
    if extratags:
        querystring['extratags'] = extratags
    if postaladdress:
        querystring['postaladdress'] = postaladdress
    if namedetails:
        querystring['namedetails'] = namedetails
    if accept_language:
        querystring['accept-language'] = accept_language
    if countrycodes:
        querystring['countrycodes'] = countrycodes
    if dedupe:
        querystring['dedupe'] = dedupe
    if matchquality:
        querystring['matchquality'] = matchquality
    if viewbox:
        querystring['viewbox'] = viewbox
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "locationiq2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def matching(coordinates: str, radiuses: str='"None"', generate_hints: str='"false"', bearings: str='"None"', tidy: str='"false"', gaps: str='"ignore"', waypoints: str='"0;1;2"', annotations: str='"false"', steps: str='"true"', geometries: str='"polyline"', exclude: str='"toll"', timestamps: str='"200;300;900"', overview: str='"simplified"', approaches: str='"curb;curb;curb"', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Matching API matches or snaps given GPS points to the road network in the most plausible way.  Please note the request might result multiple sub-traces.  Large jumps in the timestamps (> 60s) or improbable transitions lead to trace splits if a complete matching could not be found. The algorithm might not be able to match all points. Outliers are removed if they can not be matched successfully."
    coordinates: String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5
        radiuses: Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default)
        generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String
        bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array.
Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing	{value},{range} integer 0 .. 360,integer 0 .. 180
        tidy: Allows the input track modification to obtain better matching quality for noisy tracks. [ true, false (default) ]
        gaps: Allows the input track splitting based on huge timestamp gaps between points. [ split (default), ignore ]
        waypoints: Treats input coordinates indicated by given indices as waypoints in returned Match object. Default is to treat all input coordinates as waypoints. [ {index};{index};{index}... ]
        annotations: Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ]
        steps: Returned route steps for each route leg [ true, false (default) ]
        geometries: Returned route geometry format (influences overview and per step) [ polyline (default), polyline6, geojson ]
        exclude: Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none.
        timestamps: Timestamps for the input locations in seconds since UNIX epoch. Timestamps need to be monotonically increasing. [ {timestamp};{timestamp}[;{timestamp} ...]  integer seconds since UNIX epoch
        overview: Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all. [ simplified (default), full, false ]
        approaches: Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default)
        
    """
    url = f"https://locationiq2.p.rapidapi.com/matching/driving/{coordinates}"
    querystring = {}
    if radiuses:
        querystring['radiuses'] = radiuses
    if generate_hints:
        querystring['generate_hints'] = generate_hints
    if bearings:
        querystring['bearings'] = bearings
    if tidy:
        querystring['tidy'] = tidy
    if gaps:
        querystring['gaps'] = gaps
    if waypoints:
        querystring['waypoints'] = waypoints
    if annotations:
        querystring['annotations'] = annotations
    if steps:
        querystring['steps'] = steps
    if geometries:
        querystring['geometries'] = geometries
    if exclude:
        querystring['exclude'] = exclude
    if timestamps:
        querystring['timestamps'] = timestamps
    if overview:
        querystring['overview'] = overview
    if approaches:
        querystring['approaches'] = approaches
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "locationiq2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def directions(coordinates: str, continue_straight: str='"default"', geometries: str='"polyline"', exclude: str='"toll"', generate_hints: str='"false"', steps: str='"true"', bearings: str='"10,20;40,30;30,9"', annotations: str='"false"', radiuses: str='"500;200;300"', approaches: str='"curb;curb;curb"', alternatives: int=0, overview: str='"simplified"', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Finds the fastest route between coordinates in the supplied order."
    coordinates: String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5
        continue_straight: Forces the route to keep going straight at waypoints constraining uturns there even if it would be faster. Default value depends on the profile [ default (default), true, false ]
        geometries: Returned route geometry format (influences overview and per step) [ polyline (default), polyline6, geojson ]
        exclude: Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none.
        generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String
        steps: Returned route steps for each route leg [ true, false (default) ]
        bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array.
Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing	{value},{range} integer 0 .. 360,integer 0 .. 180
        annotations: Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ]
        radiuses: Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default)
        approaches: Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default)
        alternatives: Search for alternative routes. Passing a number alternatives=n searches for up to n alternative routes. [ true, false (default), or Number ]
        overview: Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all. [ simplified (default), full, false ]
        
    """
    url = f"https://locationiq2.p.rapidapi.com/directions/driving/{coordinates}"
    querystring = {}
    if continue_straight:
        querystring['continue_straight'] = continue_straight
    if geometries:
        querystring['geometries'] = geometries
    if exclude:
        querystring['exclude'] = exclude
    if generate_hints:
        querystring['generate_hints'] = generate_hints
    if steps:
        querystring['steps'] = steps
    if bearings:
        querystring['bearings'] = bearings
    if annotations:
        querystring['annotations'] = annotations
    if radiuses:
        querystring['radiuses'] = radiuses
    if approaches:
        querystring['approaches'] = approaches
    if alternatives:
        querystring['alternatives'] = alternatives
    if overview:
        querystring['overview'] = overview
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "locationiq2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def nearest(coordinates: str, exclude: str='"toll"', number: int=3, bearings: str='"10,20"', generate_hints: str='"false"', approaches: str='"curb"', radiuses: str='"1000"', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Snaps a coordinate to the street network and returns the nearest n matches. Where coordinates only supports a single {longitude},{latitude} entry."
    coordinates: String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5
        exclude: Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none.
        number: Number of nearest segments that should be returned. [ integer >= 1 (default 1) ]
        bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array.
Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing	{value},{range} integer 0 .. 360,integer 0 .. 180
        generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String
        approaches: Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default)
        radiuses: Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default)
        
    """
    url = f"https://locationiq2.p.rapidapi.com/nearest/driving/{coordinates}"
    querystring = {}
    if exclude:
        querystring['exclude'] = exclude
    if number:
        querystring['number'] = number
    if bearings:
        querystring['bearings'] = bearings
    if generate_hints:
        querystring['generate_hints'] = generate_hints
    if approaches:
        querystring['approaches'] = approaches
    if radiuses:
        querystring['radiuses'] = radiuses
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "locationiq2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

