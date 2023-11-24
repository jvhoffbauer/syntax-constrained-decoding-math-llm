import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def recommendation_trends(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns Recommendation Trends."
    symbol: i.e: TSLA
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/recommendation"
    querystring = {'symbol': symbol, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def summary_details(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a summary detailed of any public stock"
    symbol: i.e: TSLA
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/summarydetails"
    querystring = {'symbol': symbol, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def simple_summary_of_the_stocks(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a Simple Summary of the Stocks"
    symbol: i.e: TSLA
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/summaryprofile"
    querystring = {'symbol': symbol, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def full_stock_price(period: str, symbol: str, to: str, is_from: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a stock price."
    
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/price"
    querystring = {'period': period, 'symbol': symbol, 'to': to, 'from': is_from, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def upgrade_downgrade_history(to: str, is_from: str, symbol: str, period: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a Upgrade Downgrade History."
    to: Date format: yyyy-mm-dd
        from: Date format: yyyy-mm-dd
        symbol: ticker... i.e: TSLA
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/udhistory"
    querystring = {'to': to, 'from': is_from, 'symbol': symbol, }
    if period:
        querystring['period'] = period
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def calendar_events(to: str, is_from: str, symbol: str, period: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Calendar Events of a particular stock"
    to: Date format: yyyy-mm-dd
        from: Date format: yyyy-mm-dd
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/calendarEvents"
    querystring = {'to': to, 'from': is_from, 'symbol': symbol, }
    if period:
        querystring['period'] = period
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def earnings(to: str, is_from: str, symbol: str, period: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns the company earnings."
    to: Date format: yyyy-mm-dd
        from: Date format: yyyy-mm-dd
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/earnings"
    querystring = {'to': to, 'from': is_from, 'symbol': symbol, }
    if period:
        querystring['period'] = period
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def balansheet_financials(is_from: str, to: str, symbol: str, period: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a company/ stock financials"
    from: Date
        to: Date
        symbol: i.e: TSLA
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/financials"
    querystring = {'from': is_from, 'to': to, 'symbol': symbol, }
    if period:
        querystring['period'] = period
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def conversion_rates(conversion: str, period: str, interval: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns conversion rates for any currency."
    conversion: Values Accepted:
eur-usd, usd-jpy, gbp-usd, usd-chf, aud-usd, usd-cad, nzd-usd, eur-jpy, eur-chf, eur-gbp, gbp-jpy, chf-jpy, aud-jpy, eur-aud, eur-cad, aud-cad, cad-jpy, nzd-jpy, aud-nzd, gbp-cad, gbp-nzd, gbp-aud, usd-hkd, usd-sgd, usd-try, usd-mxn, usd-zar, usd-inr, usd-cnh, usd-idr, usd-thb, usd-php, usd-myr, usd-vnd, usd-krw, usd-sar, usd-aed, usd-qar, usd-omr, usd-bhd, usd-kes, usd-egp, usd-ngn, usd-ghs, usd-xaf, usd-xof, usd-zmw, usd-ugx, usd-tzs, usd-mad, usd-dzd, usd-tnd, usd-lyd, usd-mru, usd-bsd, usd-bbd, usd-jmd, usd-xcd, usd-awg, usd-bob, usd-crc, usd-dop, usd-gtq, usd-hnl, usd-htg, usd-jpy-otc, eur-usd-otc, usd-cny-otc, usd-chf-otc, usd-huf, usd-pen, usd-ils, usd-ars, usd-clp, usd-cop, usd-pab, usd-pyg, usd-uyu, usd-ves, usd-brl, usd-rub, usd-uaa, usd-kzt, usd-azn, usd-gea, usd-try-otc, usd-byn, usd-uah, usd-mnt, usd-uzs, usd-gel, usd-mzn, usd-xdr, xpt-usd, xpd-usd, xau-usd, xag-usd
        period: String: Period of time, window size. Default P1M (1 month). Valid values: P1D, P1W, P1M, P3M, P6M, P1Y, P5Y, MAX.
        interval: Interval between results. Default P1D (1 day). Valid values: PT1M, PT5M, PT15M, PT30M, PT1H, PT5H, P1D, P1W, P1M.
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/investp"
    querystring = {'conversion': conversion, 'period': period, }
    if interval:
        querystring['interval'] = interval
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def yh_historical(edate: str, sdate: str, ticker: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns the history of a public stock."
    edate: // End Date
        sdate: // Start Date
format: yyyyy-mm-dd
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/yhfhistorical"
    querystring = {'edate': edate, 'sdate': sdate, 'ticker': ticker, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def summary_detail(ticker: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns full detail of any public stock"
    ticker: i.e: TSLA
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/yhf"
    querystring = {'ticker': ticker, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_price(ticker: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint retrieves a price with details for any public stock."
    ticker: i.e: TSLA
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/yhprice"
    querystring = {'ticker': ticker, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def currency_converter(to: str, amount: str, is_from: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Looking for a fast and reliable currency converter? Our API endpoint has got you covered! With just a few lines of code, you can easily integrate our endpoint into your application and start converting currencies in no time. Say goodbye to the hassle of manual calculations and let our endpoint handle it all for you. 
		
		Try it out today and experience the convenience and efficiency of our currency converter API endpoint."
    to: i.e: JPY
        from: i.e: USD
        
    """
    url = f"https://yh-finance-complete.p.rapidapi.com/convert"
    querystring = {'to': to, 'amount': amount, 'from': is_from, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

