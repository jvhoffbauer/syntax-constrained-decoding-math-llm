import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def language_identifier(text: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Recognizes the language in which a text is written. This module can distinguish several languages using language models and morphological structures."
    text: The input text for the module. This module will process the text you introduce in this field.
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/language_identifier"
    querystring = {'text': text, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def keyword_extractor(text: str, lang_input: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "It extracts the most relevant words from a text and ranks them according to their degree of relevance. For Spanish, English, Galician, and Portuguese."
    text: The input text for the module. This module will process the text you introduce in this field
        lang_input: Language in wich the text is written. Codes: en - english, es - spanish, pt - portuguese and gl - galician. Use: en, es, pt or gl
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/keyword_extractor"
    querystring = {'text': text, 'lang_input': lang_input, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def syntactic_analyzer(lang_input: str, output_type: str, text: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Gives the syntactic struture of a text using a dependency-based parser: DepPattern. All words of a text are structured in binary relations (dependencies). For Spanish, English, Galician, and Portuguese."
    lang_input: Language in wich the text is written. Code: en - english, es - spanish, pt - portuguese and gl - galician
        output_type: Type of output. Code (-a) Analyser, (-fa) Analyser with full representation, (-c) Corrector, (-conll) CoNLL
        text: This is the text you are goint to analyze or extract information.
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/syntactic_analyzer"
    querystring = {'lang_input': lang_input, 'output_type': output_type, 'text': text, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def named_entity_recognizer(text: str, lang_input: str, url: str='http://www.example.com', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "It extracts from a text Named Entities and classify them as persons, places, organizations, and miscelaneous."
    text: The input text for the module. This module will process the text you introduce in this field
        lang_input: Language in wich the text is written. Codes: en - english, es - spanish, pt - portuguese and gl - galician. Use: en, es, pt or gl
        url: If the input text is inside a website, like an article in a blog, you can insert the url in this field instead the input text above
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/named_entity_recognizer"
    querystring = {'text': text, 'lang_input': lang_input, }
    if url:
        querystring['url'] = url
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def triples_extractor(lang_input: str, text: str='Type or paste here the text you want to analyze', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "It extracts triples relations: OBJECT1 RELATION OBJECT2"
    lang_input: Language in wich the text is written. Code: en - english, es - spanish, pt - portuguese and gl - galician
        text: This is the text you are goint to analyze or extract information.
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/triples_extractor"
    querystring = {'lang_input': lang_input, }
    if text:
        querystring['text'] = text
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def summarizer(text: str, lang_input: str, output_size: int=20, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Create a summary or abstract from a text. You chouse the percentage of the summary: 10% abstract or 50% long summary."
    text: The input text of the module
        lang_input: Language in wich the text is written. Codes: en - english, es - spanish, pt - portuguese and gl - galician. Use: en, es, pt or gl
        output_size: The percentage of the output text. 20 means the summary will be composed by 20% of the sentences of the original text.
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/summarizer"
    querystring = {'text': text, 'lang_input': lang_input, }
    if output_size:
        querystring['output_size'] = output_size
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def verb_conjugator(text: str, lang_input: str, variety: str='pt_pt', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns the inflection of a verb, even verbs that don't exist, using the rules to conjugate it. For Galician, Spanish and Portuguese."
    text: Verb infinitive (Examples: tener (spanish), fazer (portuguese), facer (galician) )
        lang_input: Language in wich the text is written. Codes: en - english, es - spanish, pt - portuguese and gl - galician. Use: en, es, pt or gl
        variety: Only applies for portuguese. Language variety: pt_pt - "Eropeu com acordo ortográfico", pt_br "Brasileiro com Acordo Ortográfico", pt_pt_sao "Europeu sem Acordo Ortográfico" e pt_br_sao "Brasileiro sem Acordo Ortográfico"
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/conjugator"
    querystring = {'text': text, 'lang_input': lang_input, }
    if variety:
        querystring['variety'] = variety
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def tokenizer(text: str, lang_input: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Splits a text into words and phrases, including ambiguous separators like dots and colons."
    text: The input text for the module. This module will process the text you introduce in this field
        lang_input: Language in wich the text is written. Codes: en - english, es - spanish, pt - portuguese and gl - galician. Use: en, es, pt or gl
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/tokenizer"
    querystring = {'text': text, 'lang_input': lang_input, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def web_text_extractor(url: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "It extracts from a url the relevant text of the web. In a newspaper, it extract the article."
    url: Website to extract the main text
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/web_text_extractor"
    querystring = {'url': url, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def multiword_extractor(text: str, lang_input: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "It extracts the most relevant multiword terms from a text and ranked according to their degree of internal cohesion, for example: “mortgage rates”, “house price”, “building societies”, “price war”. For Spanish, English, Galician, and Portuguese."
    text: The input text for the module. This module will process the text you introduce in this field
        lang_input: Language in wich the text is written. Codes: en - english, es - spanish, pt - portuguese and gl - galician. Use: en, es, pt or gl
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/multiword_extractor"
    querystring = {'text': text, 'lang_input': lang_input, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def sentiment_analyzer(text: str, lang_input: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "It tells you whether it thinks the text you enter expresses positive sentiment, negative sentiment, or if it's neutral. It also gives you a quantitative weight of how intense is the sentiment. For Spanish, English, and Portuguese."
    text: The input text for the module. This module will process the text you introduce in this field
        lang_input: Language in wich the text is written. Codes: en - english, es - spanish, pt - portuguese and gl - galician. Use: en, es, pt or gl
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/sentiment_analyzer"
    querystring = {'text': text, 'lang_input': lang_input, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def part_of_speech_tagger(text: str, lang_input: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "I analyzes a text with by providing words with Part of Speech tags (e.g., noun, verb, preposition...), morphological features (singular, masculine...), and their lemmas (canonical form). For Spanish, English, Galician, and Portuguese."
    text: The input text for the module. This module will process the text you introduce in this field
        lang_input: Language in wich the text is written. Codes: en - english, es - spanish, pt - portuguese and gl - galician. Use: en, es, pt or gl
        
    """
    url = f"https://cilenisapi.p.rapidapi.com/pos_tagger"
    querystring = {'text': text, 'lang_input': lang_input, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "cilenisapi.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

