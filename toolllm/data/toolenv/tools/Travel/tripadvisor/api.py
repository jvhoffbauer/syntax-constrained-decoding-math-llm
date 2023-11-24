import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_cars_same_dropoff(order: str, pickupdate: str, pickuplocationtype: str, pickuptime: str, dropofftime: str, dropoffdate: str, pickupplaceid: str, driverage: str=None, pickupairportcode: str=None, currencycode: str='USD', page: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    order: Order by parameter


        pickupdate: PickUp Date
Format: **YYYY-MM-DD**
        pickuplocationtype: **pickUpLocationType** can be retrieved from **Search Rental Cars Location** API from the **Rental Cars** collection.
        pickuptime: PickUp Time
Format: **YYYY-MM-DD**
        dropofftime: DropOff Time
Format: **YYYY-MM-DD**
        dropoffdate: DropOff Date
Format: **YYYY-MM-DD**
        pickupplaceid: **placeId** for the **location** from where you want to **pick up** the car. **pickUpPlaceId** can be retrieved from **Search Rental Cars Location** API from the **Rental Cars** collection.
        driverage: Age of the Driver
        pickupairportcode: Pass in the **airportCode** as **pickUpAirportCode** if the searched **place type** is **AIRPORT**.
        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        page: Page number. The default page number is 1.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/cars/searchCarsSameDropOff"
    querystring = {'order': order, 'pickUpDate': pickupdate, 'pickUpLocationType': pickuplocationtype, 'pickUpTime': pickuptime, 'dropOffTime': dropofftime, 'dropOffDate': dropoffdate, 'pickUpPlaceId': pickupplaceid, }
    if driverage:
        querystring['driverAge'] = driverage
    if pickupairportcode:
        querystring['pickUpAirportCode'] = pickupairportcode
    if currencycode:
        querystring['currencyCode'] = currencycode
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def rental_availability(rentalid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    rentalid: Get **rentalId** from **Rental Search** API in **Vacation Rentals** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/rentals/rentalAvailability"
    querystring = {'rentalId': rentalid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_cars_different_dropoff(dropoffplaceid: str, order: str, dropofflocationtype: str, dropofftime: str, pickuplocationtype: str, dropoffdate: str, pickupdate: str, pickupplaceid: str, pickuptime: str, pickupairportcode: str=None, page: int=1, currencycode: str='USD', dropoffairportcode: str=None, driverage: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    dropoffplaceid: **placeId** for the **location** from where you want to **drop off** the car. **dropOffPlaceId** can be retrieved from **Search Rental Cars Location** API from the **Rental Cars** collection.
        order: Order by parameter
        dropofflocationtype: **dropOffLocationType** can be retrieved from **Search Rental Cars Location** API from the **Rental Cars** collection.
        dropofftime: DropOff Time
Format: **YYYY-MM-DD**
        pickuplocationtype: **pickUpLocationType** can be retrieved from **Search Rental Cars Location** API from the **Rental Cars** collection.
        dropoffdate: DropOff Date
Format: **YYYY-MM-DD**
        pickupdate: PickUp Date
Format: **YYYY-MM-DD**
        pickupplaceid: **placeId** for the **location** from where you want to **pick up** the car. **pickUpPlaceId** can be retrieved from **Search Rental Cars Location** API from the **Rental Cars** collection.
        pickuptime: PickUp Time
Format: **YYYY-MM-DD**
        pickupairportcode: Pass in the **airportCode** as **pickUpAirportCode** if the searched **place type** is **AIRPORT**.
        page: Page number. The default page number is 1.
        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        dropoffairportcode: Pass in the **airportCode** as **dropOffAirportCode** if the searched **place type** is **AIRPORT**.
        driverage: Age of the Driver
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/cars/searchCarsDifferentDropOff"
    querystring = {'dropOffPlaceId': dropoffplaceid, 'order': order, 'dropOffLocationType': dropofflocationtype, 'dropOffTime': dropofftime, 'pickUpLocationType': pickuplocationtype, 'dropOffDate': dropoffdate, 'pickUpDate': pickupdate, 'pickUpPlaceId': pickupplaceid, 'pickUpTime': pickuptime, }
    if pickupairportcode:
        querystring['pickUpAirportCode'] = pickupairportcode
    if page:
        querystring['page'] = page
    if currencycode:
        querystring['currencyCode'] = currencycode
    if dropoffairportcode:
        querystring['dropOffAirportCode'] = dropoffairportcode
    if driverage:
        querystring['driverAge'] = driverage
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_hotels_filter(checkout: str, checkin: str, geoid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    checkout: CheckOut Date
Format: **YYYY-MM-DD**
        checkin: Checkin Date
Format: **YYYY-MM-DD**
        geoid: Pass in the **geoId** of the location retrieved from the **Search Location** API from the **Hotels** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/hotels/getHotelsFilter"
    querystring = {'checkOut': checkout, 'checkIn': checkin, 'geoId': geoid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_hotels(checkin: str, geoid: str, checkout: str, adults: int=None, sort: str=None, rooms: int=None, deals: str=None, type: str=None, is_class: str=None, neighborhood: str=None, distfrom: str=None, distfrommaxdistance: str=None, pricemax: int=None, pricemin: int=None, pagenumber: int=1, childrenages: str=None, brand: str=None, rating: int=None, amenity: str=None, healthsafety: str=None, style: str=None, currencycode: str='USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    checkin: Checkin Date
Format: **YYYY-MM-DD**
        geoid: Pass in the **geoId** of the location retrieved from the **Search Location** API from the **Hotels** collection.
        checkout: Checkout Date
Format: **YYYY-MM-DD**
        pagenumber: Page number. The default page number is 1.
        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"
    querystring = {'checkIn': checkin, 'geoId': geoid, 'checkOut': checkout, }
    if adults:
        querystring['adults'] = adults
    if sort:
        querystring['sort'] = sort
    if rooms:
        querystring['rooms'] = rooms
    if deals:
        querystring['deals'] = deals
    if type:
        querystring['type'] = type
    if is_class:
        querystring['class'] = is_class
    if neighborhood:
        querystring['neighborhood'] = neighborhood
    if distfrom:
        querystring['distFrom'] = distfrom
    if distfrommaxdistance:
        querystring['distFromMaxDistance'] = distfrommaxdistance
    if pricemax:
        querystring['priceMax'] = pricemax
    if pricemin:
        querystring['priceMin'] = pricemin
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if childrenages:
        querystring['childrenAges'] = childrenages
    if brand:
        querystring['brand'] = brand
    if rating:
        querystring['rating'] = rating
    if amenity:
        querystring['amenity'] = amenity
    if healthsafety:
        querystring['healthSafety'] = healthsafety
    if style:
        querystring['style'] = style
    if currencycode:
        querystring['currencyCode'] = currencycode
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_location(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    query: Name of the location where the **Hotel** is situated.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchLocation"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_hotel_details(is_id: str, checkin: str, checkout: str, adults: int=None, rooms: int=None, childrenages: str=None, currency: str='USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    id: Pass in the hotel id as **id**, which can be retrieved from **Search Hotels** API from **Hotels** collection.
        checkin: Checkin Date
Format: **YYYY-MM-DD**
        checkout: CheckOut Date
Format: **YYYY-MM-DD**
        adults: Number of adult guests (with age 18 and over)
        rooms: Number of rooms required.
        childrenages: Number of children (with age between 0 and 17)
Example:
If 1st child's age is 11 months and 2nd child's age is 10 years, then the parameter should be passed as [0,10]
        currency: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/hotels/getHotelDetails"
    querystring = {'id': is_id, 'checkIn': checkin, 'checkOut': checkout, }
    if adults:
        querystring['adults'] = adults
    if rooms:
        querystring['rooms'] = rooms
    if childrenages:
        querystring['childrenAges'] = childrenages
    if currency:
        querystring['currency'] = currency
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_hotels_by_location(latitude: str, checkin: str, checkout: str, longitude: str, pagenumber: int=1, currencycode: str='USD', rooms: int=None, childrenages: str=None, adults: int=None, type: str=None, amenity: str=None, healthsafety: str=None, deals: str=None, rating: int=None, style: str=None, is_class: str=None, distfrommaxdistance: str=None, distfrom: str=None, pricemin: int=None, pricemax: int=None, brand: str=None, neighborhood: str=None, sort: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    latitude: Pass in the **geoId** of the location retrieved from the **Search Location** API from the **Hotels** collection.
        checkin: Checkin Date
Format: **YYYY-MM-DD**
        checkout: Checkout Date
Format: **YYYY-MM-DD**
        pagenumber: Page number. The default page number is 1.
        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotelsByLocation"
    querystring = {'latitude': latitude, 'checkIn': checkin, 'checkOut': checkout, 'longitude': longitude, }
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if currencycode:
        querystring['currencyCode'] = currencycode
    if rooms:
        querystring['rooms'] = rooms
    if childrenages:
        querystring['childrenAges'] = childrenages
    if adults:
        querystring['adults'] = adults
    if type:
        querystring['type'] = type
    if amenity:
        querystring['amenity'] = amenity
    if healthsafety:
        querystring['healthSafety'] = healthsafety
    if deals:
        querystring['deals'] = deals
    if rating:
        querystring['rating'] = rating
    if style:
        querystring['style'] = style
    if is_class:
        querystring['class'] = is_class
    if distfrommaxdistance:
        querystring['distFromMaxDistance'] = distfrommaxdistance
    if distfrom:
        querystring['distFrom'] = distfrom
    if pricemin:
        querystring['priceMin'] = pricemin
    if pricemax:
        querystring['priceMax'] = pricemax
    if brand:
        querystring['brand'] = brand
    if neighborhood:
        querystring['neighborhood'] = neighborhood
    if sort:
        querystring['sort'] = sort
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def rental_reviews(rentalid: str, page: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    rentalid: Get **rentalId** from **Rental Search** API in **Vacation Rentals** collection.
        page: Page number. The default page number is 1.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/rentals/rentalReviews"
    querystring = {'rentalId': rentalid, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def rental_rates(rentalid: str, startdate: str, adults: int, enddate: str, currencycode: str='USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    rentalid: Get **rentalId** from **Rental Search** API in **Vacation Rentals** collection.
        startdate: Checkin Date
Format: YYYY-MM-DD
        adults: The number of guests.
        enddate: Checkout Date
Format: YYYY-MM-DD
        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/rentals/rentalRates"
    querystring = {'rentalId': rentalid, 'startDate': startdate, 'adults': adults, 'endDate': enddate, }
    if currencycode:
        querystring['currencyCode'] = currencycode
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_filters(destinationairportcode: str, sourceairportcode: str, date: str, classofservice: str, itinerarytype: str, returndate: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    destinationairportcode: Destination **airportCode**. The **airportCode** can be extracted from the **Search Airport** API in the **Flights** collection.
        sourceairportcode: Source **airportCode**. The **airportCode** can be extracted from the **Search Airport** API in the **Flights** collection.

        date: **Departure** or **Travel date**.
Format: **YYYY-MM-DD**
        classofservice: Traveller cabin class.
        itinerarytype: Pass **itineraryType** as **ONE_WAY** for **one way** and **ROUND_TRIP** for **return flight**.
        returndate: **Return date**.
Format: **YYYY-MM-DD**
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/flights/getFilters"
    querystring = {'destinationAirportCode': destinationairportcode, 'sourceAirportCode': sourceairportcode, 'date': date, 'classOfService': classofservice, 'itineraryType': itinerarytype, }
    if returndate:
        querystring['returnDate'] = returndate
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_restaurants(locationid: str, page: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    locationid: **locationId** of the place got from **Search Restaurant Location** in **Restaurants collection**.

        page: Page number. The default page number is 1.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchRestaurants"
    querystring = {'locationId': locationid, }
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_flights(numadults: int, sortorder: str, date: str, numseniors: int, sourceairportcode: str, destinationairportcode: str, classofservice: str, itinerarytype: str, pagenumber: int=1, returndate: str=None, childages: str=None, searchhash: str=None, searchid: str=None, nearby: str=None, pageloaduid: str=None, currencycode: str='USD', nonstop: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    numadults: Number of Adults (Ages between 18-64 years)
Default Value: 1
        sortorder: Sort by parameter
        date: **Departure** or **Travel date**.
Format: **YYYY-MM-DD**
        numseniors: Number of Seniors (with age 65 and over)
Default Value: 1
        sourceairportcode: Source **airportCode**. The **airportCode** can be extracted from the **Search Airport** API in the **Flights** collection.

        destinationairportcode: Destination **airportCode**. The **airportCode** can be extracted from the **Search Airport** API in the **Flights** collection.
        classofservice: Traveller cabin class.
        itinerarytype: Pass **itineraryType** as **ONE_WAY** for **one way** and **ROUND_TRIP** for **return flight**.
        returndate: **Return date**.
Format: **YYYY-MM-DD**
        childages: Pass Children age in the form of Array (Ages between 2-12 years)
Eg: [2, 10]
        searchhash: Pass **searchHash** from the previous API call to get a complete response.

        searchid: Pass **searchId** from the previous API call to get a complete response.

        nearby: Include nearby airports
        pageloaduid: Pass **pageLoadUid** from the previous API call to get a complete response.

        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        nonstop: Prefer nonstop
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"
    querystring = {'numAdults': numadults, 'sortOrder': sortorder, 'date': date, 'numSeniors': numseniors, 'sourceAirportCode': sourceairportcode, 'destinationAirportCode': destinationairportcode, 'classOfService': classofservice, 'itineraryType': itinerarytype, }
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if returndate:
        querystring['returnDate'] = returndate
    if childages:
        querystring['childAges'] = childages
    if searchhash:
        querystring['searchHash'] = searchhash
    if searchid:
        querystring['searchId'] = searchid
    if nearby:
        querystring['nearby'] = nearby
    if pageloaduid:
        querystring['pageLoadUid'] = pageloaduid
    if currencycode:
        querystring['currencyCode'] = currencycode
    if nonstop:
        querystring['nonstop'] = nonstop
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_rental_cars_location(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    query: Name of the location where you want to Rent the Car.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/rentals/searchLocation"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def rental_details(rentalid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    rentalid: Get **rentalId** from **Rental Search** API in **Vacation Rentals** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/rentals/rentalDetails"
    querystring = {'rentalId': rentalid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_flights_multicity(sortorder: str, classofservice: str, legs: str, pageloaduid: str=None, currencycode: str='USD', searchid: str=None, searchhash: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    sortorder: Sort by parameter
        classofservice: Traveller cabin class.
        legs: The legs must contain the origin, destination and date in object format and must be passed in an array.
EXAMPLE:
[
{'sourceAirportCode':'BOS','destinationAirportCode':'LON','date':'2022-12-18'},{'sourceAirportCode':'LON','destinationAirportCode':'BOS','date':'2022-12-26'},
…
]
**Note**: If there are multiple stops, there should be more leg objects on the board.
        pageloaduid: Pass **pageLoadUid** from the previous API call to get a complete response.

        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        searchid: Pass **searchId** from the previous API call to get a complete response.

        searchhash: Pass **searchHash** from the previous API call to get a complete response.

        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlightsMultiCity"
    querystring = {'sortOrder': sortorder, 'classOfService': classofservice, 'legs': legs, }
    if pageloaduid:
        querystring['pageLoadUid'] = pageloaduid
    if currencycode:
        querystring['currencyCode'] = currencycode
    if searchid:
        querystring['searchId'] = searchid
    if searchhash:
        querystring['searchHash'] = searchhash
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_currency(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/getCurrency"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def test_api(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API is to test if server is up and running"
    
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/test"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def rental_search(arrival: str, sortorder: str, geoid: str, departure: str, page: int=1, currencycode: str='USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    arrival: Checkin Date
Format: YYYY-MM-DD
        sortorder: Sort by parameter
        geoid: Get geoId of the place from Rental Search API from the Vacation Rentals collection.
        departure: Checkout Date
Format: YYYY-MM-DD
        page: Page number. The default page number is 1.
        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/rentals/rentalSearch"
    querystring = {'arrival': arrival, 'sortOrder': sortorder, 'geoId': geoid, 'departure': departure, }
    if page:
        querystring['page'] = page
    if currencycode:
        querystring['currencyCode'] = currencycode
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_cruises_details(seoname: str, shipid: str, currencycode: str='USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    seoname: **seoName** can be retrieved from **Search Cruises** API and **Get Cruises Quick Links** API from the **Cruises collection**.
        shipid: **shipId** can be retrieved from **Search Cruises** API and **Get Cruises Quick Links** API from the **Cruises collection**.
        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/cruises/getCruisesDetails"
    querystring = {'seoName': seoname, 'shipId': shipid, }
    if currencycode:
        querystring['currencyCode'] = currencycode
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_cruises(order: str, destinationid: str, currencycode: str='USD', departuredate: str=None, page: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    order: Order by parameter
        destinationid: **destinationId** can be retrieved from **Get Cruises Location** API from the **Cruises collection**.
        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        departuredate: Departure Date
Format: **YYYY-MM**
        page: Page number. The default page number is 1.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/cruises/searchCruises"
    querystring = {'order': order, 'destinationId': destinationid, }
    if currencycode:
        querystring['currencyCode'] = currencycode
    if departuredate:
        querystring['departureDate'] = departuredate
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_cruises_quick_links(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/cruises/getCruisesQuickLinks"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_cruises_location(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/cruises/getLocation"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_vacation_rental_location(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    query: Name of the location where you want to search for **Vacation Rentals**.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/rentals/searchLocation"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_restaurant_details(restaurantsid: str, currencycode: str='USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    restaurantsid: Get id from **search restaurant** API
        currencycode: **currencyCode** can be retrieved from **Get Currency** API from **Configs** collection.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/getRestaurantDetails"
    querystring = {'restaurantsId': restaurantsid, }
    if currencycode:
        querystring['currencyCode'] = currencycode
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_restaurant_location(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    query: Name of the location where the **Restaurant** is situated.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/restaurant/searchLocation"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_airport(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "-"
    query: Name of the location where the **Airport** is situated.
        
    """
    url = f"https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchAirport"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

