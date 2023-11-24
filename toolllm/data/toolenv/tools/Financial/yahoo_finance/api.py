import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def news(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "returns latest news articles related to symbol passed as parameter"
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/news/{symbol}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def trend(symbl: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This reflects the insurance company's profits over given periods of time.
		This endpoint also gives **experts** & **AI supported predictions** about stock future behavior"
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/earnings-trend/{symbl}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def index(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Trend Analysis is a relatively straightforward quantitative demand forecasting technique that uses the historical relationship between the operational index (i.e. sales level) and the number of employees required by the organization (demand for labour) to forecast future requirements."
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/index-trend/{symbol}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def historic_data(symbol: str, interval: str, range: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "return historic data
		interval - The time interval between two data points. Can be 1m 2m 5m 15m 30m 60m 90m 1h 1d 5d 1wk 1mo 3mo
		range - The range for which the data is returned.
		
		for normal stocks :
		you can directly search by tickername:
		eg. tsla , msft , meta
		
		for crypt:
		try searching by ticker name followed by -USD.
		for bitcoin try : btc-usd"
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/historic/{symbol}/{interval}/{range}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def balance_sheet(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A **balance sheet** is a financial statement that communicates the so-called “book value” of an organization, as calculated by subtracting all of the company's liabilities and shareholder equity from its total assets."
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/balance-sheet/{symbol}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def price(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the Stock Price Information for the symbol passed as parameter
		
		for normal stocks :
		you can directly search by tickername:
		eg. tsla , msft , meta
		
		for crypt:
		try searching by ticker name followed by -USD.
		for bitcoin try : btc-usd
		for eth try : eth-usd
		for dogecoin try : doge-usd"
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/price/{symbol}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def esg(symb: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Simply explained, an ESG score is a measure of a company's exposure to long-term environmental, social, and governance risks that are often overlooked during traditional financial analyses."
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/esg-score/{symb}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def finance_analytics(symb: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API endpoint also returns **AI recommendation**
		Financial analysis refers to an assessment of the viability, stability, and profitability of a business, sub-business or project. It is performed by professionals who prepare reports using ratios and other techniques, that make use of information taken from financial statements and other reports."
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/finance-analytics/{symb}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def earnings(symb: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A company's earnings are its after-tax net income. This is the company's bottom line or its profits. Earnings are perhaps the single most important and most closely studied number in a company's financial statements.
		This API **also** returns **historical earnings**"
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/earnings/{symb}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def statistics(symbol: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Key Statistics are **important points of financial data that allow you to quickly view and ascertain transaction history**, as well as provide insight into donation trends. These statistics can be found both on the Dashboard as entire database summaries and on an individual basis at the top of each entity record."
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/key-statistics/{symbol}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search(symb: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "search for tickers with similar name"
    
    """
    url = f"https://yahoo-finance127.p.rapidapi.com/search/{symb}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

