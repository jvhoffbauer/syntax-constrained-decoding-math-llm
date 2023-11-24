import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def trades(start: str, base: str, market_venue: str, symbol: str, end: str='2022-10-15T11:00:00', sort: str='asc', limit: int=100, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Trades endpoint available upon request"
    start: Start of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone
        base: The second or quote currency in the traded pair
        market_venue: The name of an exchange or a venue
        symbol: The first or base currency in the traded pair
        end: End of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone
        sort: The ordering of results: `asc` (from earliest to latest), `desc` (from latest to earliest)
        limit: Maximum number of records to return, max `10000`
        
    """
    url = f"https://cryptocurrency-financial-data.p.rapidapi.com/trades"
    querystring = {'start': start, 'base': base, 'market_venue': market_venue, 'symbol': symbol, }
    if end:
        querystring['end'] = end
    if sort:
        querystring['sort'] = sort
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cryptocurrency-financial-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def metrics_ohlcv_trial(market_venue: str, symbol: str, start: str, base: str, sort: str='asc', gran: str='1d', end: str='2023-01-09T10:05:00', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Limited coverage and availability for tests"
    market_venue: Available exchanges in trial: `BINANCE`, `COINBASE`, `KRAKEN`, `BITSTAMP`, `BITFINEX`
        symbol: Available symbols in trial: `BTC`, `ETH`, `ADA`, `XRP`
        start: Start of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone. **Should be within one month from the current timestamp**
        base: Available bases in trial: `BTC`, `USD`, `USDT`, `USDC`
        sort: The ordering of events: `asc` (from earliest to latest), `desc` (from latest to earliest) 
        gran: Available granularities: `1m`, `15m`, `1h`, `1d`
        end: End of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone
        
    """
    url = f"https://cryptocurrency-financial-data.p.rapidapi.com/metrics/ohlcv/trial"
    querystring = {'market_venue': market_venue, 'symbol': symbol, 'start': start, 'base': base, }
    if sort:
        querystring['sort'] = sort
    if gran:
        querystring['gran'] = gran
    if end:
        querystring['end'] = end
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cryptocurrency-financial-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def metrics_ohlcv_futures_trial(market_venue: str, base: str, start: str, symbol: str, expiration: str='MONTHLY', delivery_date: str='2022-10-28', sort: str='asc', gran: str='1m', end: str='2023-01-10T10:05:00', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Limited coverage and availability for tests"
    market_venue: Available exchanges in trial: `BINANCE`, `BITFINEX`, `HITBTC`, `KRAKEN`, `OKX`
        base: Available bases in trial: `BTC`, `USD`, `USDT`, `USDC`
        start: Start of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone. **Should be within one month from the current timestamp**
        symbol: Available symbols in trial: `BTC`, `ETH`, `ADA`, `XRP`
        expiration: The lifespan of a futures contract. Allowed values: `perpetual`(default), `weekly`, `quarterly`, `monthly`
        delivery_date: The last day when a future contract is valid - *YYYY-MM-DD*
        sort: The ordering of events: `asc` (from earliest to latest), `desc` (from latest to earliest) 
        gran: Available granularities: `1m`, `15m`, `1h`, `1d`
        end: End of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone
        
    """
    url = f"https://cryptocurrency-financial-data.p.rapidapi.com/metrics/ohlcv/futures/trial"
    querystring = {'market_venue': market_venue, 'base': base, 'start': start, 'symbol': symbol, }
    if expiration:
        querystring['expiration'] = expiration
    if delivery_date:
        querystring['delivery_date'] = delivery_date
    if sort:
        querystring['sort'] = sort
    if gran:
        querystring['gran'] = gran
    if end:
        querystring['end'] = end
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cryptocurrency-financial-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def metrics_ohlcv_pro(start: str, market_venue: str, base: str, symbol: str, sort: str='asc', end: str='2022-10-05T10:05:00', gran: str='1d', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Price and volume metrics for spot markets"
    start: Start of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone
        market_venue: The name of an exchange or a venue
        base: The second listed currency of a currency pair
        symbol: The first listed currency of a currency pair
        sort: The ordering of events: `asc` (from earliest to latest), `desc` (from latest to earliest) 
        end: End of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone
        gran: Available granularities: `1m`, `15m`, `1h`, `1d`
        
    """
    url = f"https://cryptocurrency-financial-data.p.rapidapi.com/metrics/ohlcv"
    querystring = {'start': start, 'market_venue': market_venue, 'base': base, 'symbol': symbol, }
    if sort:
        querystring['sort'] = sort
    if end:
        querystring['end'] = end
    if gran:
        querystring['gran'] = gran
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cryptocurrency-financial-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def trades_futures(market_venue: str, base: str, symbol: str, expiration: str='MONTHLY', end: str='2022-10-19T11:00:00', delivery_date: str='2022-10-28', limit: int=100, start: str='2022-10-11T10:00:00', sort: str='asc', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Derivatives contracts transactions"
    market_venue: The name of an exchange or a venue
        base: The second listed currency of a currency pair
        symbol: The first listed currency of a currency pair
        expiration: The lifespan of a futures contract. Allowed values: `perpetual`(default), `weekly`, `quarterly`, `monthly`
        end: End of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone
        delivery_date: The last day when a future contract is valid - *YYYY-MM-DD*
        limit: Maximum number of records to return, max `10000`
        start: Start of the requested time period, *%Y-%m-%dT%H:%M:%S* UTC timezone
        sort: The ordering of results: `asc` (from earliest to latest), `desc` (from latest to earliest)
        
    """
    url = f"https://cryptocurrency-financial-data.p.rapidapi.com/trades/futures"
    querystring = {'market_venue': market_venue, 'base': base, 'symbol': symbol, }
    if expiration:
        querystring['expiration'] = expiration
    if end:
        querystring['end'] = end
    if delivery_date:
        querystring['delivery_date'] = delivery_date
    if limit:
        querystring['limit'] = limit
    if start:
        querystring['start'] = start
    if sort:
        querystring['sort'] = sort
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cryptocurrency-financial-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def metadata(asset_type: str='spot', data_type: str='metrics', symbol: str='BTC', base: str='USDT', market_venue: str='BINANCE', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://cryptocurrency-financial-data.p.rapidapi.com/metadata"
    querystring = {}
    if asset_type:
        querystring['asset_type'] = asset_type
    if data_type:
        querystring['data_type'] = data_type
    if symbol:
        querystring['symbol'] = symbol
    if base:
        querystring['base'] = base
    if market_venue:
        querystring['market_venue'] = market_venue
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cryptocurrency-financial-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def metrics_ohlcv_futures_pro(start: str, market_venue: str, symbol: str, base: str, sort: str='asc', expiration: str='MONTHLY', delivery_date: str='2022-10-28', end: str='2022-10-05T10:05:00', gran: str='1d', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Price and volume metrics for futures markets"
    start: Start of the requested time period, UTC timezone
        market_venue: The name of exchange or venue
        symbol: The first listed currency of a currency pair
        base: The second listed currency of a currency pair
        sort: The ordering of events: `asc` (from earliest to latest), `desc` (from latest to earliest) 
        expiration: The lifespan of a futures contract. Allowed values: `perpetual`(default), `weekly`, `quarterly`, `monthly`
        delivery_date: The last day when a future contract is valid - *YYYY-MM-DD*
        end: End of the requested time period, UTC timezone
        gran: Available granularities: `1m`, `15m`, `1h`, `1d`
        
    """
    url = f"https://cryptocurrency-financial-data.p.rapidapi.com/metrics/ohlcv/futures"
    querystring = {'start': start, 'market_venue': market_venue, 'symbol': symbol, 'base': base, }
    if sort:
        querystring['sort'] = sort
    if expiration:
        querystring['expiration'] = expiration
    if delivery_date:
        querystring['delivery_date'] = delivery_date
    if end:
        querystring['end'] = end
    if gran:
        querystring['gran'] = gran
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cryptocurrency-financial-data.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

