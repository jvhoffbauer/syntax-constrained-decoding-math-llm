import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def entities_search(q: str, mkt: str='en-us', safesearch: str=None, responsefilter: str=None, responseformat: str=None, setlang: str=None, cc: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get entities and places results for a given query."
    q: The user's search term.
        mkt: The market where the results come from. You are strongly encouraged to always specify the market, if known. Specifying the market helps Bing route the request and return an appropriate and optimal response. This parameter and the cc query parameter are mutually exclusive—do not specify both.
        safesearch: A filter used to filter adult content. Off: Return webpages with adult text, images, or videos. Moderate: Return webpages with adult text, but not adult images or videos. Strict: Do not return webpages with adult text, images, or videos. The default is Moderate. If the request comes from a market that Bing's adult policy requires that safeSearch is set to Strict, Bing ignores the safeSearch value and uses Strict. If you use the site: query operator, there is the chance that the response may contain adult content regardless of what the safeSearch query parameter is set to. Use site: only if you are aware of the content on the site and your scenario supports the possibility of adult content.
        responsefilter: A comma-delimited list of answers to include in the response. If you do not specify this parameter, the response includes all search answers for which there's relevant data.
        responseformat: The media type to use for the response. The following are the possible case-insensitive values: JSON, JSONLD. The default is JSON. If you specify JSONLD, the response body includes JSON-LD objects that contain the search results.
        setlang: The language to use for user interface strings. Specify the language using the ISO 639-1 2-letter language code. For example, the language code for English is EN. The default is EN (English). Although optional, you should always specify the language. Typically, you set setLang to the same language specified by mkt unless the user wants the user interface strings displayed in a different language. This parameter and the Accept-Language header are mutually exclusive; do not specify both. A user interface string is a string that's used as a label in a user interface. There are few user interface strings in the JSON response objects. Also, any links to Bing.com properties in the response objects apply the specified language.
        cc: A 2-character country code of the country where the results come from. This API supports only the United States market. If you specify this query parameter, it must be set to us. If you set this parameter, you must also specify the Accept-Language header. Bing uses the first supported language it finds from the languages list, and combine that language with the country code that you specify to determine the market to return results for. If the languages list does not include a supported language, Bing finds the closest language and market that supports the request, or it may use an aggregated or default market for the results instead of a specified one. You should use this query parameter and the Accept-Language query parameter only if you specify multiple languages; otherwise, you should use the mkt and setLang query parameters. This parameter and the mkt query parameter are mutually exclusive—do not specify both.
        
    """
    url = f"https://bing-entity-search.p.rapidapi.com/entities"
    querystring = {'q': q, }
    if mkt:
        querystring['mkt'] = mkt
    if safesearch:
        querystring['SafeSearch'] = safesearch
    if responsefilter:
        querystring['ResponseFilter'] = responsefilter
    if responseformat:
        querystring['ResponseFormat'] = responseformat
    if setlang:
        querystring['SetLang'] = setlang
    if cc:
        querystring['cc'] = cc
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "bing-entity-search.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

