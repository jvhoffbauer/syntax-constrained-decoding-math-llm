import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_fste_mib_stocks_last_dividend_date(page: int=1, size: int=10, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get Last Dividend Date"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/lastDivDate"
    querystring = {}
    if page:
        querystring['page'] = page
    if size:
        querystring['size'] = size
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def custom(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get the best GC"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/custom"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_last_judgement(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Judgments from other banks"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/lastJudgment"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_rating_0_4(size: int=10, lt: int=4, gt: int=3, order: str='asc', page: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by ranking (analysis from Borsa Italiana)
		A sortable/filterable FSTE MIB stock ranking from Borsa Italiana.
		All stocks are presented with the rating value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/rating"
    querystring = {}
    if size:
        querystring['size'] = size
    if lt:
        querystring['lt'] = lt
    if gt:
        querystring['gt'] = gt
    if order:
        querystring['order'] = order
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_included_stocks(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get all included stocks with their ISIN code"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_medium_tendency(order: str='asc', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by medium tendency (analysis from Il Sole 24 Ore)
		A sortable/filterable FSTE MIB stock medium tendency from Il Sole 24 Ore.
		All stocks are presented with the medium tendency value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/mediumTendency"
    querystring = {}
    if order:
        querystring['order'] = order
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_short_tendency(order: str='asc', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by short tendency (analysis from Il Sole 24 Ore)
		A sortable/filterable FSTE MIB stock short tendency from Il Sole 24 Ore.
		All stocks are presented with the short tendency value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/shortTendency"
    querystring = {}
    if order:
        querystring['order'] = order
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_rsi_from_milano_finanza(page: int=1, lt: int=60, order: str='asc', size: int=10, gt: int=20, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by RSI (analysis from Milano Finanza)
		A sortable/filterable FSTE MIB stock RSI from Milano Finanza.
		All stocks are presented with the RSI value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/rsi"
    querystring = {}
    if page:
        querystring['page'] = page
    if lt:
        querystring['lt'] = lt
    if order:
        querystring['order'] = order
    if size:
        querystring['size'] = size
    if gt:
        querystring['gt'] = gt
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_rsi_from_borsa_italiana(order: str='asc', gt: int=20, size: int=10, lt: int=60, page: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by RSI (analysis from Borsa Italiana)
		A sortable/filterable FSTE MIB stock RSI from Borsa Italiana.
		All stocks are presented with the RSI value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/rsi"
    querystring = {}
    if order:
        querystring['order'] = order
    if gt:
        querystring['gt'] = gt
    if size:
        querystring['size'] = size
    if lt:
        querystring['lt'] = lt
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_performance_1m(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by performance (analysis from Borsa Italiana)
		A sortable/filterable FSTE MIB stock performance from Borsa Italiana.
		All stocks are presented with the performance value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/perf1M"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_performance_6m(lt: int=60, gt: int=20, size: int=10, page: int=1, order: str='desc', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by performance (analysis from Borsa Italiana)
		A sortable/filterable FSTE MIB stock performance from Borsa Italiana.
		All stocks are presented with the performance value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/perf6M"
    querystring = {}
    if lt:
        querystring['lt'] = lt
    if gt:
        querystring['gt'] = gt
    if size:
        querystring['size'] = size
    if page:
        querystring['page'] = page
    if order:
        querystring['order'] = order
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_ranking(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by RANKING (analysis from Milano Finanza)
		A sortable/filterable FSTE MIB stock ranking from Borsa Italiana.
		All stocks are presented with the ranking value and the relative source."
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/mfRanking"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_risk_evaluation(order: str='desc', page: int=1, lt: int=60, size: int=10, gt: int=20, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by risk evaluation (analysis from Milano Finanza)
		A sortable/filterable FSTE MIB stock ranking from Milano Finanza.
		All stocks are presented with the risk value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/mfRisk"
    querystring = {}
    if order:
        querystring['order'] = order
    if page:
        querystring['page'] = page
    if lt:
        querystring['lt'] = lt
    if size:
        querystring['size'] = size
    if gt:
        querystring['gt'] = gt
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_real_time_fste_mib_stock_analysis(isin: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Query by stock ISIN code and get real time stock technical analysis. 
		The system surfs the most important online media to gather data like: RSI, supports, resistances, ratings, evaluations, tendency, and risk. Data will be provided with relative sources."
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/analysis/{isin}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_last_dividend_amount(order: str='asc', gt: int=0, lt: int=5, size: int=10, page: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by last dividend amount (analysis from Milano Finanza)
		A sortable/filterable FSTE MIB stock last dividend amount from Milano Finanza.
		All stocks are presented with the last dividend amount value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/lastDiv"
    querystring = {}
    if order:
        querystring['order'] = order
    if gt:
        querystring['gt'] = gt
    if lt:
        querystring['lt'] = lt
    if size:
        querystring['size'] = size
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_last_dividend_yield(order: str='asc', gt: int=0, lt: int=5, size: int=10, page: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by last dividend yield (analysis from Milano Finanza)
		A sortable/filterable FSTE MIB stock last dividend yield from Borsa Italiana.
		All stocks are presented with the last dividend yield value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/divYield"
    querystring = {}
    if order:
        querystring['order'] = order
    if gt:
        querystring['gt'] = gt
    if lt:
        querystring['lt'] = lt
    if size:
        querystring['size'] = size
    if page:
        querystring['page'] = page
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_performance_1y(page: int=1, size: int=10, lt: int=60, gt: int=20, order: str='asc', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by performance (analysis from Borsa Italiana)
		A sortable/filterable FSTE MIB stock performance from Borsa Italiana.
		All stocks are presented with the performance value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/perf1Y"
    querystring = {}
    if page:
        querystring['page'] = page
    if size:
        querystring['size'] = size
    if lt:
        querystring['lt'] = lt
    if gt:
        querystring['gt'] = gt
    if order:
        querystring['order'] = order
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_fste_mib_stocks_volatility(page: int=1, size: int=10, order: str='asc', lt: int=60, gt: int=20, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Rank Italy FSTE MIB stocks by volatility (analysis from Borsa Italiana)
		A sortable/filterable FSTE MIB stock volatility from Borsa Italiana.
		All stocks are presented with the volatility value and the relative source.
		Data is updated daily"
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/stocks/volatility"
    querystring = {}
    if page:
        querystring['page'] = page
    if size:
        querystring['size'] = size
    if order:
        querystring['order'] = order
    if lt:
        querystring['lt'] = lt
    if gt:
        querystring['gt'] = gt
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_real_time_fste_mib_stock_press_release(isin: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Query by stock ISIN code and get a real time press release.
		The system surfs the most important online media to provide you a complete set of links to the last news."
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/news/{isin}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_real_time_fste_mib_stock_informations(isin: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Query by stock ISIN code and get real-time stock informations.
		The system surfs the most important online media to gather data like: dividend date and amount, volatility, performance, minimun values and maximum values, contact informations, site and so on... Data will be provided with relative sources."
    
    """
    url = f"https://tradingradar.p.rapidapi.com/api/info/{isin}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "tradingradar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

