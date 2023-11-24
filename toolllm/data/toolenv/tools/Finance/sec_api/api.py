import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_fundamentals(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "get company fundamentals data as listed in SEC filings from historic or current date ranges. Includes data for: 
		Symbol, Start, End, Filed, Form, Revenue, Net Income, Comprehensive Income, EPS, Diluted EPS, Shares, Diluted, Shares, Assets, Current Assets, Liabilities, Current Liabilities, Stockholders Equity, Operating Activities, Investing, Activities, Financing Activities."
    
    """
    url = f"https://sec-api2.p.rapidapi.com/SEC_API"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "sec-api2.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

