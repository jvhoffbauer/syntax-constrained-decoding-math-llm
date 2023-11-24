import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def retrieve_collection_offers_v2(slug: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint is used to get collection offers for a specified collection."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/v2/offers/collection/{slug}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieve_all_offers_v2(slug: str, next: str=None, limit: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get all open offers for a collection"
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/v2/offers/collection/{slug}/all"
    querystring = {}
    if next:
        querystring['next'] = next
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieve_all_listings_v2(slug: str, next: str=None, limit: int=100, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get all active listings for a collection"
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/v2/listings/collection/{slug}/all"
    querystring = {}
    if next:
        querystring['next'] = next
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieve_offers_v2(chain: str, limit: str='20', maker: str=None, taker: str=None, listed_after: str=None, order_direction: str=None, listed_before: str=None, asset_contract_address: str='0x4372f4d950d30c6f12c7228ade77d6cc019404c9', token_ids: str='309', order_by: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint is used to fetch the set of active offers on a given NFT for the Seaport contract."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/v2/orders/{chain}/seaport/offers"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if maker:
        querystring['maker'] = maker
    if taker:
        querystring['taker'] = taker
    if listed_after:
        querystring['listed_after'] = listed_after
    if order_direction:
        querystring['order_direction'] = order_direction
    if listed_before:
        querystring['listed_before'] = listed_before
    if asset_contract_address:
        querystring['asset_contract_address'] = asset_contract_address
    if token_ids:
        querystring['token_ids'] = token_ids
    if order_by:
        querystring['order_by'] = order_by
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def deprecated_retrieving_listings(asset_contract_address: str, token_id: str, limit: int=20, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Used to fetch active listings on a given asset."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/api/v1/asset/{asset_contract_address}/{token_id}/listings"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieve_trait_offers_v2(slug: str, type: str='tier', value: str='classy_1', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint is used to get all trait offers for a specified collection."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/v2/offers/collection/{slug}/traits"
    querystring = {}
    if type:
        querystring['type'] = type
    if value:
        querystring['value'] = value
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def deprecated_retrieving_offers(asset_contract_address: str, token_id: str, limit: int=20, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Used to fetch active offers for a given asset."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/api/v1/asset/{asset_contract_address}/{token_id}/offers"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def deprecated_retrieving_orders(include_bundled: bool=None, side: int=0, limit: int=20, listed_after: str=None, maker: str=None, owner: str=None, taker: str=None, order_by: str='created_date', asset_contract_address: str='0x4372f4d950d30c6f12c7228ade77d6cc019404c9', payment_token_address: str=None, is_english: bool=None, bundled: bool=None, listed_before: int=1644800000, token_ids: str=None, sale_kind: int=0, token_id: str='309', order_direction: str='desc', offset: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "How to fetch orders from the OpenSea system."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/wyvern/v1/orders"
    querystring = {}
    if include_bundled:
        querystring['include_bundled'] = include_bundled
    if side:
        querystring['side'] = side
    if limit:
        querystring['limit'] = limit
    if listed_after:
        querystring['listed_after'] = listed_after
    if maker:
        querystring['maker'] = maker
    if owner:
        querystring['owner'] = owner
    if taker:
        querystring['taker'] = taker
    if order_by:
        querystring['order_by'] = order_by
    if asset_contract_address:
        querystring['asset_contract_address'] = asset_contract_address
    if payment_token_address:
        querystring['payment_token_address'] = payment_token_address
    if is_english:
        querystring['is_english'] = is_english
    if bundled:
        querystring['bundled'] = bundled
    if listed_before:
        querystring['listed_before'] = listed_before
    if token_ids:
        querystring['token_ids'] = token_ids
    if sale_kind:
        querystring['sale_kind'] = sale_kind
    if token_id:
        querystring['token_id'] = token_id
    if order_direction:
        querystring['order_direction'] = order_direction
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieve_listings_v2(chain: str, limit: str='20', asset_contract_address: str='0x4372f4d950d30c6f12c7228ade77d6cc019404c9', maker: str=None, order_direction: str=None, token_ids: str='309', taker: str=None, listed_before: str=None, order_by: str=None, listed_after: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint is used to fetch the set of active listings on a given NFT for the Seaport contract."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/v2/orders/{chain}/seaport/listings"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if asset_contract_address:
        querystring['asset_contract_address'] = asset_contract_address
    if maker:
        querystring['maker'] = maker
    if order_direction:
        querystring['order_direction'] = order_direction
    if token_ids:
        querystring['token_ids'] = token_ids
    if taker:
        querystring['taker'] = taker
    if listed_before:
        querystring['listed_before'] = listed_before
    if order_by:
        querystring['order_by'] = order_by
    if listed_after:
        querystring['listed_after'] = listed_after
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieving_a_collection(collection_slug: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Used for retrieving more in-depth information about individual collections, including real time statistics like floor price."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/api/v1/collection/{collection_slug}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieving_collection_stats(collection_slug: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Use this endpoint to fetch stats for a specific collection, including realtime floor price statistics"
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/api/v1/collection/{collection_slug}/stats"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieving_bundles(asset_contract_addresses: str=None, limit: int=1, token_ids: int=None, on_sale: bool=None, asset_contract_address: str=None, offset: int=0, owner: str='0x842858c0093866abd09a363150fb540d97e78223', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Bundles are groups of items for sale on OpenSea. You can buy them all at once in one transaction, and you can create them without any transactions or gas, as long as you've already approved the assets inside."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/api/v1/bundles"
    querystring = {}
    if asset_contract_addresses:
        querystring['asset_contract_addresses'] = asset_contract_addresses
    if limit:
        querystring['limit'] = limit
    if token_ids:
        querystring['token_ids'] = token_ids
    if on_sale:
        querystring['on_sale'] = on_sale
    if asset_contract_address:
        querystring['asset_contract_address'] = asset_contract_address
    if offset:
        querystring['offset'] = offset
    if owner:
        querystring['owner'] = owner
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieving_collections(limit: int=20, asset_owner: str='0x2bf699087a0d1d67519ba86f960fecd80d59c4d7', offset: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The `/collections` endpoint provides a list of all the collections supported and vetted by OpenSea. To include all collections relevant to a user (including non-whitelisted ones), set the owner param.
		
		Each collection in the returned area has an attribute called primary_asset_contracts with info about the smart contracts belonging to that collection. For example, ERC-1155 contracts maybe have multiple collections all referencing the same contract, but many ERC-721 contracts may all belong to the same collection (dapp).
		
		You can also use this endpoint to find which dapps an account uses, and how many items they own in each - all in one API call!"
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/api/v1/collections"
    querystring = {}
    if limit:
        querystring['limit'] = limit
    if asset_owner:
        querystring['asset_owner'] = asset_owner
    if offset:
        querystring['offset'] = offset
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieving_assets(owner: str=None, order_direction: str='desc', asset_contract_address: str=None, limit: int=20, collection_slug: str=None, cursor: str=None, token_ids: int=None, asset_contract_addresses: str=None, collection: str='ongakucraft', include_orders: bool=None, collection_editor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "To retrieve assets from our API, call the `/assets` endpoint with the desired filter parameters.
		
		Auctions created on OpenSea don't use an escrow contract, which enables gas-free auctions and allows users to retain ownership of their items while they're on sale. So this is just a heads up in case you notice some assets from opensea.io not appearing in the API."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/api/v1/assets"
    querystring = {}
    if owner:
        querystring['owner'] = owner
    if order_direction:
        querystring['order_direction'] = order_direction
    if asset_contract_address:
        querystring['asset_contract_address'] = asset_contract_address
    if limit:
        querystring['limit'] = limit
    if collection_slug:
        querystring['collection_slug'] = collection_slug
    if cursor:
        querystring['cursor'] = cursor
    if token_ids:
        querystring['token_ids'] = token_ids
    if asset_contract_addresses:
        querystring['asset_contract_addresses'] = asset_contract_addresses
    if collection:
        querystring['collection'] = collection
    if include_orders:
        querystring['include_orders'] = include_orders
    if collection_editor:
        querystring['collection_editor'] = collection_editor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieving_a_contract(asset_contract_address: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Used to fetch more in-depth information about an contract asset."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/api/v1/asset_contract/{asset_contract_address}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieving_events(collection_slug: str=None, auction_type: str=None, asset_contract_address: str='0x4372f4d950d30c6f12c7228ade77d6cc019404c9', token_id: int=309, collection_editor: str=None, occurred_after: int=None, cursor: str=None, account_address: str=None, occurred_before: int=1644800000, only_opensea: bool=None, event_type: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The `/events` endpoint provides a list of events that occur on the assets that OpenSea tracks. The "event_type" field indicates what type of event it is (transfer, successful auction, etc)."
    
    """
    url = f"https://opensea-data-query.p.rapidapi.com/api/v1/events"
    querystring = {}
    if collection_slug:
        querystring['collection_slug'] = collection_slug
    if auction_type:
        querystring['auction_type'] = auction_type
    if asset_contract_address:
        querystring['asset_contract_address'] = asset_contract_address
    if token_id:
        querystring['token_id'] = token_id
    if collection_editor:
        querystring['collection_editor'] = collection_editor
    if occurred_after:
        querystring['occurred_after'] = occurred_after
    if cursor:
        querystring['cursor'] = cursor
    if account_address:
        querystring['account_address'] = account_address
    if occurred_before:
        querystring['occurred_before'] = occurred_before
    if only_opensea:
        querystring['only_opensea'] = only_opensea
    if event_type:
        querystring['event_type'] = event_type
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "opensea-data-query.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

