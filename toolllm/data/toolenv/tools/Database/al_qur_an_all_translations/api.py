import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_surah(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "give digits in URL from 1 to 114 and get surah with different translations for now we are giving only two languages,
		but we are working on adding more soon.
		![](https://go4quiz.com/wp-content/uploads/List-of-114-Surahs-go4quiz.jpg)"
    
    """
    url = f"https://al-qur-an-all-translations.p.rapidapi.com/getSurah/{is_id}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "al-qur-an-all-translations.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

