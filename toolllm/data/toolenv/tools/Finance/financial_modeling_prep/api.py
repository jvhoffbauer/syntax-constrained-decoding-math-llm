import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def companies_balance_sheet_statements(symbol: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns companies balance sheet statements."
    symbol: symbol name
        
    """
    url = f"https://financial-modeling-prep.p.rapidapi.com/v3/balance-sheet-statement/{symbol}"
    querystring = {'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "financial-modeling-prep.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def companies_profile(symbol: str, apikey: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API returns companies profile (Price,Beta,Volume Average, Market Capitalisation, Last Dividend, 52 week range, stock price change, stock price change in percentage, Company Name, Exchange, Description, Industry,Sector,CEO,Website and image)."
    symbol: symbol names
        
    """
    url = f"https://financial-modeling-prep.p.rapidapi.com/v3/profile/{symbol}"
    querystring = {'apikey': apikey, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "financial-modeling-prep.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def stock_quote_price(symbol: str, apikey: str='rapidapi', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API returns stock price in real time"
    symbol: symbol names
        
    """
    url = f"https://financial-modeling-prep.p.rapidapi.com/v3/quote/{symbol}"
    querystring = {}
    if apikey:
        querystring['apikey'] = apikey
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "financial-modeling-prep.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def earning_call_transcript_api_premium(symbol: str, apikey: str, quarter: int=4, year: int=2020, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Analyzing Earnings Conference Call With NLP"
    symbol: symbol name
        
    """
    url = f"https://financial-modeling-prep.p.rapidapi.com/v3/earning_call_transcript/{symbol}"
    querystring = {'apikey': apikey, }
    if quarter:
        querystring['quarter'] = quarter
    if year:
        querystring['year'] = year
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "financial-modeling-prep.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def companies_cash_flow_statements(symbol: str, apikey: str='rapid_api', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns companies cash flow statements"
    symbol: symbol name
        
    """
    url = f"https://financial-modeling-prep.p.rapidapi.com/v3/cash-flow-statement/{symbol}"
    querystring = {}
    if apikey:
        querystring['apikey'] = apikey
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "financial-modeling-prep.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

