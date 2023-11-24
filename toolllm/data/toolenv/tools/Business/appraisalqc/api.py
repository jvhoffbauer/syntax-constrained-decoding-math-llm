import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def validationreport(ordernumber: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The API returns the XML validation report of the Appraisal Report uploaded"
    ordernumber: OrderNumber of the uploaded PDF file for which validation report needs to be displayed
        
    """
    url = f"https://appraisalqc1.p.rapidapi.com/mls/v1/AppraisalValidation/getValidationReport"
    querystring = {'OrderNumber': ordernumber, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "appraisalqc1.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

