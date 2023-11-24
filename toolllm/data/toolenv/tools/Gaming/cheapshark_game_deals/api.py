import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def stores_info(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a full list of store IDs and names, a flag specifying if store is active, and an array of image/logo sizes (relative URLs)"
    
    """
    url = f"https://cheapshark-game-deals.p.rapidapi.com/stores"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def manage_alerts(email: str, action: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Send an email containing a link to manage your alerts."
    email: Any valid email address
        action: The action to take on the price alert, set to `manage`
        
    """
    url = f"https://cheapshark-game-deals.p.rapidapi.com/alerts"
    querystring = {'email': email, 'action': action, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_of_games(title: str='batman', exact: int=0, limit: int=60, steamappid: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a list of games that contain a given title or matches steamAppID. Response includes the cheapest current deal for each game."
    title: Search for a game by title
        exact: Default `0`

Flag to allow only exact string match for `title` parameter
        limit: Default `60`

The maximum number of games to return, up to `60`
        steamappid: Search for a game by Steam’s AppID - e.g. http://store.steampowered.com/app/35140/
        
    """
    url = f"https://cheapshark-game-deals.p.rapidapi.com/games"
    querystring = {}
    if title:
        querystring['title'] = title
    if exact:
        querystring['exact'] = exact
    if limit:
        querystring['limit'] = limit
    if steamappid:
        querystring['steamAppID'] = steamappid
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_of_deals(lowerprice: int=0, steamrating: int=0, title: str='batman', steamappid: str=None, desc: bool=None, output: str='json', steamworks: bool=None, sortby: str='Deal Rating', aaa: bool=None, pagesize: int=60, exact: bool=None, upperprice: int=50, pagenumber: int=0, onsale: bool=None, metacritic: int=0, storeid: str='1,2,3', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a paged list of deals matching any number of criteria, all the filtering parameters are optional.
		
		The deal object is what drives most of what you see on the site. They are price + metadata properties for games for a given store. All dealID’s are encoded on the server. On your website/app, you will use the redirect page to link users to a specific deal:
		
		> https://www.cheapshark.com/redirect?dealID={id}
		
		**Important Note**: The redirect page is not an API endpoint and is not designed for automated access. It is purely a way to link your end users to deals.
		
		The deal rating property provides a quick way to compare how 'good' a deal is. It is normalized on a scale from 0 to 10."
    lowerprice: Default `0`

Only returns deals with a price *greater than* this value
        steamrating: Minimum Steam reviews rating for a game
        title: Looks for the string contained anywhere in the game name
        steamappid: Look for deals on specific games, comma separated list of Steam App ID
        desc: Default `0`

Determines sort direction
        output: Option to output deals in `RSS` format (overrides page number/size to `0`/`100`)
        steamworks: Default `0`

Flag to include only deals that redeem on Steam (best guess, depends on store support)
        sortby: Criteria to sort the list by, possible values -

- Deal Rating
- Title
- Savings
- Price
- Metacritic
- Reviews
- Release
- Store
- recent
        aaa: Default `0`

Flag to include only deals with retail price > `$29`
        pagesize: The size of pages returned, default and maximum value is `60`
        exact: Default `0`

Flag to allow only exact string match for `title` parameter
        upperprice: Only returns deals with a price* less than or equal to` this value (`50` acts the same as no limit)
        pagenumber: The requested page number, 0 indexed, default of `0`
        onsale: Default `0`

Flag to include only games that are currently on sale
        metacritic: Minimum Metacritic rating for a game
        storeid: Comma separated list of store ID's to filter on, omit for deals from any store
        
    """
    url = f"https://cheapshark-game-deals.p.rapidapi.com/deals"
    querystring = {}
    if lowerprice:
        querystring['lowerPrice'] = lowerprice
    if steamrating:
        querystring['steamRating'] = steamrating
    if title:
        querystring['title'] = title
    if steamappid:
        querystring['steamAppID'] = steamappid
    if desc:
        querystring['desc'] = desc
    if output:
        querystring['output'] = output
    if steamworks:
        querystring['steamworks'] = steamworks
    if sortby:
        querystring['sortBy'] = sortby
    if aaa:
        querystring['AAA'] = aaa
    if pagesize:
        querystring['pageSize'] = pagesize
    if exact:
        querystring['exact'] = exact
    if upperprice:
        querystring['upperPrice'] = upperprice
    if pagenumber:
        querystring['pageNumber'] = pagenumber
    if onsale:
        querystring['onSale'] = onsale
    if metacritic:
        querystring['metacritic'] = metacritic
    if storeid:
        querystring['storeID'] = storeid
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def game_lookup(is_id: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Gets info for a specific game. Response includes a list of all deals associated with the game."
    id: An existing gameID
        
    """
    url = f"https://cheapshark-game-deals.p.rapidapi.com/games"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def edit_alert(action: str, email: str, gameid: int, price: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Set or remove a price alert."
    action: The action to take on the price alert (`set` or `delete`)
        email: Any valid email address
        gameid: An existing gameID
        price: The price to wait for, only required when using `set` value for `action` parameter
        
    """
    url = f"https://cheapshark-game-deals.p.rapidapi.com/alerts"
    querystring = {'action': action, 'email': email, 'gameID': gameid, 'price': price, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def deal_lookup(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get info for a specific deal. Response includes game info, any cheaper current deals, and the cheapest historical price. As elsewhere, dealID is encoded"
    id: An Encoded Deal ID
        
    """
    url = f"https://cheapshark-game-deals.p.rapidapi.com/deals"
    querystring = {'id': is_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

