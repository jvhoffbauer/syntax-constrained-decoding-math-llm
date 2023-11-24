import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def fetch_async_content(threadid: str, promptid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Provide async prompt and threadid to fetch content.
		This endpoint is Free and you are allowed to pull it once every 2 seconds to fetch your content."
    
    """
    url = f"https://adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com/v1/adcopyai/fetchContent/"
    querystring = {'threadId': threadid, 'promptId': promptid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def api_key_validation(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint is used only to validate API Keys, it simply returns a status of 200 and a message of 'OK'. 
		The use of this endpoint is Free, and is useful for server-to-server FREE API validation."
    
    """
    url = f"https://adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com/v1/seo/validateApi"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_10_ad_descriptions_generator_25_seconds(describeproductorservice: str, url: str, specialoffer: str='3 months Free Trial', calltoaction: str='Get Started!', keywordstoexclude: str='Example keyword', mostimportantkeywords: str='facebook ads, google ads, adwords', exampledescriptions: str="Great advertising optimization doesn't have to be that expensive. Try madgicx.com for free. 100+ AI Audiences, 7 Automation Tactics, 7-Day free trial and creative intelligence inside. Live Chat Support. Schedule A Demo. View Our Pricing Details. 7-Day Free Trial.", toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get relevant & Complint Google Ad descriptions for SEM and PPC marketers, created by SEM Experts. Results include 10+ ad descriptions, and are based on user inputs as well as A.I. Intelligence based on OpenAI's engine. 
		
		**Detailed description:**
		The Descriptions generator endpoint uses advanced prompt engineering to analyze user inputs in the form of URL, subject, and important keywords to create high-quality ad descriptions that are tailored to the product or service being advertised. By leveraging the advanced capabilities of OpenAI's ChatGPT engine, the endpoint is able to deliver top-of-the-line ad descriptions that are optimized for relevance, clarity, and engagement.
		
		**Detailed Technical Documentation:**
		The Descriptions generator endpoint of AdCopy AI can be accessed through a GET request, with the following query parameters:
		
		**subject:** Required. A string of between 10 and 60 characters, which represents the "value proposition" of the product or service being advertised. The user is advised to provide keywords in a comma-delimited format.
		
		**url:** Required. A string that represents the URL of a page that describes the product or service being advertised. The API will fetch the content from the page and extract relevant keywords to help generate quality ads.
		
		**mostImportantKeywords:** Optional. A string of up to 100 characters, representing the most important keywords about the ad group being advertised. The presence of these keywords in the resulting content is not guaranteed.
		
		**language:** Optional. A string that represents the target audience's language in ISO-2 format (e.g. EN, IT, ES, etc.). The field is currently in alpha testing and may not provide results in the requested language.
		
		**country:** Optional. A string that represents the target audience's country in ISO-2 format (e.g. US, CA, IT, etc.). The field is currently in alpha testing and may not provide country-specific content.
		
		**exampleDescriptions:** Optional. A string of at most 200 characters, representing example descriptions that the user may provide to fine-tune the results.
		
		The endpoint will return up to 10 ad descriptions that are tailored to the product or service being advertised. The descriptions will be optimized for relevance, clarity, and engagement, leveraging the advanced capabilities of OpenAI's ChatGPT engine and Significat Prompt Optimization  for your specific ad and product  or service requirement.
		
		Try it now, for free."
    
    """
    url = f"https://adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com/v1/seo/adsGenerator/descriptions/"
    querystring = {'describeProductOrService': describeproductorservice, 'url': url, }
    if specialoffer:
        querystring['specialOffer'] = specialoffer
    if calltoaction:
        querystring['callToAction'] = calltoaction
    if keywordstoexclude:
        querystring['keywordsToExclude'] = keywordstoexclude
    if mostimportantkeywords:
        querystring['mostImportantKeywords'] = mostimportantkeywords
    if exampledescriptions:
        querystring['exampleDescriptions'] = exampledescriptions
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_20_ad_headlines_generator_25_seconds(describeproductorservice: str, url: str, specialoffer: str='3 months Free Trial', calltoaction: str='Get Started!', mostimportantkeywords: str='facebook ads, google ads, adwords', keywordstoexclude: str='Example keyword', exampleheadlines: str='Tired of Overpriced Platforms? - This Software is like a Team', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get relevant & Complint Google Ad headlines for SEM and PPC marketers, created by SEM Experts. Results include 10+ ad headlines, and are based on user inputs as well as A.I. Intelligence based on OpenAI's engine. 
		
		**Detailed description:**
		The Headlines generator endpoint uses advanced prompt engineering to analyze user inputs in the form of URL, subject, and important keywords to create high-quality ad headlines that are tailored to the product or service being advertised. By leveraging the advanced capabilities of OpenAI's ChatGPT engine, the endpoint is able to deliver top-of-the-line ad headlines that are optimized for relevance, clarity, and engagement.
		
		**Detailed Technical Documentation:**
		The Headlines generator endpoint of AdCopy AI can be accessed through a GET request, with the following query parameters:
		
		**subject:** Required. A string of between 10 and 60 characters, which represents the "value proposition" of the product or service being advertised. The user is advised to provide keywords in a comma-delimited format.
		
		**url:** Required. A string that represents the URL of a page that describes the product or service being advertised. The API will fetch the content from the page and extract relevant keywords to help generate quality ads.
		
		**mostImportantKeywords:** Optional. A string of up to 100 characters, representing the most important keywords about the ad group being advertised. The presence of these keywords in the resulting content is not guaranteed.
		
		**language:** Optional. A string that represents the target audience's language in ISO-2 format (e.g. EN, IT, ES, etc.). The field is currently in alpha testing and may not provide results in the requested language.
		
		**country:** Optional. A string that represents the target audience's country in ISO-2 format (e.g. US, CA, IT, etc.). The field is currently in alpha testing and may not provide country-specific content.
		
		**exampleHeadlines:** Optional. A string of at most 200 characters, representing example headlines that the user may provide to fine-tune the results.
		
		The endpoint will return up to 10 ad headlines that are tailored to the product or service being advertised. The headlines will be optimized for relevance, clarity, and engagement, leveraging the advanced capabilities of OpenAI's ChatGPT engine and Significat Prompt Optimization."
    
    """
    url = f"https://adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com/v1/seo/adsGenerator/headlines"
    querystring = {'describeProductOrService': describeproductorservice, 'url': url, }
    if specialoffer:
        querystring['specialOffer'] = specialoffer
    if calltoaction:
        querystring['callToAction'] = calltoaction
    if mostimportantkeywords:
        querystring['mostImportantKeywords'] = mostimportantkeywords
    if keywordstoexclude:
        querystring['keywordsToExclude'] = keywordstoexclude
    if exampleheadlines:
        querystring['exampleHeadlines'] = exampleheadlines
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ad_generator_20_head_and_10_desc_1_min(describeproductorservice: str, url: str, specialoffer: str='3 months Free Trial', exampleheadlines: str='Automate Facebook & Google Ads', calltoaction: str='Get Started!', mostimportantkeywords: str='facebook ads, google ads, adwords', exampledescriptions: str="Great advertising optimization doesn't have to be that expensive. Try madgicx.com for free", keywordstoexclude: str='Example keyword', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a relevant & Compliant Google Ad, for SEM and PPC marketers, created by SEM Experts. Result includes 10+ ad descriptions &  20+ headlines, and  is based on user inputs as well as A.I. Intelligence based on OpenAI's engine. 
		
		**Detailed description:**
		The Full Ad generator endpoint combines the power of the headlines AI generator with the descriptions AI generator to generator a full set of Google Ad Dynamic Search Ad consisting of 4 descriptions and 15 headlines ( though we provide more so you could pick and choose the best ones ). 
		
		This API endpoint uses advanced prompt engineering to analyze user inputs in the form of URL, subject, and important keywords to create high-quality ad descriptions that are tailored to the product or service being advertised. By leveraging the advanced capabilities of OpenAI's ChatGPT engine, the endpoint is able to deliver top-of-the-line ad descriptions that are optimized for relevance, clarity, and engagement.
		
		**Detailed Technical Documentation:**
		Combined the Descriptions & Headlines generator endpoint of AdCopy AI into a single GET request, with the following query parameters:
		
		**subject:** Required. A string of between 10 and 60 characters, which represents the "value proposition" of the product or service being advertised. The user is advised to provide keywords in a comma-delimited format.
		
		**url:** Required. A string that represents the URL of a page that describes the product or service being advertised. The API will fetch the content from the page and extract relevant keywords to help generate quality ads.
		
		**mostImportantKeywords:** Optional. A string of up to 100 characters, representing the most important keywords about the ad group being advertised. The presence of these keywords in the resulting content is not guaranteed.
		
		**language:** Optional. A string that represents the target audience's language in ISO-2 format (e.g. EN, IT, ES, etc.). The field is currently in alpha testing and may not provide results in the requested language.
		
		**country:** Optional. A string that represents the target audience's country in ISO-2 format (e.g. US, CA, IT, etc.). The field is currently in alpha testing and may not provide country-specific content.
		
		**exampleDescriptions:** Optional. A string of at most 200 characters, representing example descriptions that the user may provide to fine-tune the results.
		
		**exampleHeadlines:** Optional. A string of at most 200 characters, representing example headlines that the user may provide to fine-tune the results.
		
		The endpoint will return at least 10 ad descriptions and at least 20 headlines that are tailored to the product or service being advertised. 
		
		The Headlines & Descriptions will be optimized for relevance, clarity, and engagement, leveraging the advanced capabilities of OpenAI's ChatGPT engine and Significat Prompt Optimization for your specific ad and product  or service requirement.
		
		Try it now, for free."
    
    """
    url = f"https://adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com/v1/seo/adsGeneratorFull/"
    querystring = {'describeProductOrService': describeproductorservice, 'url': url, }
    if specialoffer:
        querystring['specialOffer'] = specialoffer
    if exampleheadlines:
        querystring['exampleHeadlines'] = exampleheadlines
    if calltoaction:
        querystring['callToAction'] = calltoaction
    if mostimportantkeywords:
        querystring['mostImportantKeywords'] = mostimportantkeywords
    if exampledescriptions:
        querystring['exampleDescriptions'] = exampledescriptions
    if keywordstoexclude:
        querystring['keywordsToExclude'] = keywordstoexclude
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "adcopy-ai-google-ads-ai-text-generation.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

