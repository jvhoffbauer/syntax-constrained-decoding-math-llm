import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def search_for_chapters_containing_terms(first_book: str, term1: str, text_mode: str='ends', term4: str=None, second_book: str=None, term_filter_operator: str='and', term2: str='light', term3: str=None, word_search_mode: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Takes term(s) and returns chapters  that contain term(s). Terms are not case sensitive.  Books, operators etc. are NOT CASE SENSITIVE.
		
		**   ONLY SEARCHES 2 BOOKS   (NO RANGE FUNCTION) **"
    text_mode: MODES:    'full',   'blank',    'first',   'vowels',  'misc',   'ends', 

(Not case sensitive)
        term_filter_operator: OPERATORS: 'and'  'or'

(Not Case Sensitive)
        
    """
    url = f"https://bible-memory-verse-flashcard.p.rapidapi.com/search_term/chapters"
    querystring = {'first_book': first_book, 'term1': term1, }
    if text_mode:
        querystring['text_mode'] = text_mode
    if term4:
        querystring['term4'] = term4
    if second_book:
        querystring['second_book'] = second_book
    if term_filter_operator:
        querystring['term_filter_operator'] = term_filter_operator
    if term2:
        querystring['term2'] = term2
    if term3:
        querystring['term3'] = term3
    if word_search_mode:
        querystring['word_search_mode'] = word_search_mode
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "bible-memory-verse-flashcard.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_term_chapter_address_summary(first_book: str, term1: str, term_filter_operator: str='and', term4: str=None, term5: str=None, second_book: str='revelation', word_search_mode: bool=None, term2: str='fire', term3: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a summary for chapter addresses that contain term criteria
		
		**  CAN SEARCH A RANGE OF BOOKS.  
		(first_book = 'matthew' , second_book = 'john' MEANS ENDPOINT SEARCHES  'matthew'  'mark'  'luke' 'john')    **"
    term_filter_operator: OPERATORS: 'and'  'or'

(Not Case Sensitive)
        
    """
    url = f"https://bible-memory-verse-flashcard.p.rapidapi.com/search_term/chapter_summary"
    querystring = {'first_book': first_book, 'term1': term1, }
    if term_filter_operator:
        querystring['term_filter_operator'] = term_filter_operator
    if term4:
        querystring['term4'] = term4
    if term5:
        querystring['term5'] = term5
    if second_book:
        querystring['second_book'] = second_book
    if word_search_mode:
        querystring['word_search_mode'] = word_search_mode
    if term2:
        querystring['term2'] = term2
    if term3:
        querystring['term3'] = term3
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "bible-memory-verse-flashcard.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_term_verse_address_summary(first_book: str, term1: str, term5: str=None, term3: str='iron', term4: str=None, term2: str='silver', term_filter_operator: str='or', word_search_mode: bool=None, second_book: str='job', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Returns a summary for verse addresses that contain term criteria.
		
		**  CAN SEARCH A RANGE OF BOOKS.  
		(first_book = 'matthew' , second_book = 'john' MEANS ENDPOINT SEARCHES  'matthew'  'mark'  'luke' 'john')    **"
    term_filter_operator: OPERATORS: 'and'  'or'

(Not Case Sensitive)
        
    """
    url = f"https://bible-memory-verse-flashcard.p.rapidapi.com/search_term/verse_summary"
    querystring = {'first_book': first_book, 'term1': term1, }
    if term5:
        querystring['term5'] = term5
    if term3:
        querystring['term3'] = term3
    if term4:
        querystring['term4'] = term4
    if term2:
        querystring['term2'] = term2
    if term_filter_operator:
        querystring['term_filter_operator'] = term_filter_operator
    if word_search_mode:
        querystring['word_search_mode'] = word_search_mode
    if second_book:
        querystring['second_book'] = second_book
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "bible-memory-verse-flashcard.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_for_verses_containing_terms(word_search_mode: bool, first_book: str, term_filter_operator: str, term1: str, text_mode: str='full', term2: str=None, term4: str=None, second_book: str='numbers', term3: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Takes term(s) and returns verses that contain term(s). Terms are not case sensitive. 
		Books, operators etc. are NOT CASE SENSITIVE
		
		**  CAN SEARCH A RANGE OF BOOKS.  
		(first_book = 'matthew' , second_book = 'john' MEANS ENDPOINT SEARCHES  'matthew'  'mark'  'luke' 'john')    **"
    first_book: 1ST / book name IN POSSIBLE VERSE SEQUENCE
        term_filter_operator: OPERATORS: 'and'  'or'

(Not Case Sensitive)
        text_mode: MODES:    'full',   'blank',    'first',   'vowels',  'misc',   'ends', 

(Not case sensitive)
        second_book: 2nd / last book IN POSSIBLE VERSE SEQUENCE.

(IF first_book='matthew', second_book='acts'  MEANS results FROM 
'matthew', 'mark', 'luke', 'john', 'acts')
        
    """
    url = f"https://bible-memory-verse-flashcard.p.rapidapi.com/search_term/verses"
    querystring = {'word_search_mode': word_search_mode, 'first_book': first_book, 'term_filter_operator': term_filter_operator, 'term1': term1, }
    if text_mode:
        querystring['text_mode'] = text_mode
    if term2:
        querystring['term2'] = term2
    if term4:
        querystring['term4'] = term4
    if second_book:
        querystring['second_book'] = second_book
    if term3:
        querystring['term3'] = term3
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "bible-memory-verse-flashcard.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_term_count_occurrences_of_terms_found_in_text(term1: str, first_book: str, second_book: str='numbers', term5: str=None, term7: str=None, term2: str=None, term6: str=None, term4: str=None, term3: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Return number of term criteria occurrences in chosen book(s)
		
		**  CAN SEARCH A RANGE OF BOOKS.  
		(first_book = 'matthew' , second_book = 'john' MEANS ENDPOINT SEARCHES  'matthew'  'mark'  'luke' 'john')    **"
    
    """
    url = f"https://bible-memory-verse-flashcard.p.rapidapi.com/search_term/counter"
    querystring = {'term1': term1, 'first_book': first_book, }
    if second_book:
        querystring['second_book'] = second_book
    if term5:
        querystring['term5'] = term5
    if term7:
        querystring['term7'] = term7
    if term2:
        querystring['term2'] = term2
    if term6:
        querystring['term6'] = term6
    if term4:
        querystring['term4'] = term4
    if term3:
        querystring['term3'] = term3
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "bible-memory-verse-flashcard.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_verses(text_mode: str, book_name: str, verse_num1: int=1, chapter: int=1, verse_num2: int=5, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Takes parameters and returns requested verses"
    text_mode: MODES:    'full',   'blank',    'first',   'vowels',  'misc',   'ends', 

(Not case sensitive)
        verse_num1: 1ST / starting verse IN POSSIBLE VERSE SEQUENCE
        verse_num2: Last verse of a possible sequence of verses [EX: IF verse_num1=1 and verse_num2=10
means verses  1,2,3,4,5,6,7,8,9, 10 WILL BE RETURNED]
        
    """
    url = f"https://bible-memory-verse-flashcard.p.rapidapi.com/get_verses"
    querystring = {'text_mode': text_mode, 'book_name': book_name, }
    if verse_num1:
        querystring['verse_num1'] = verse_num1
    if chapter:
        querystring['chapter'] = chapter
    if verse_num2:
        querystring['verse_num2'] = verse_num2
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "bible-memory-verse-flashcard.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_chapter(book_name: str, chapter: int=1, text_mode: str='vowels', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Takes parameters and returns one chapter for chosen bookname"
    text_mode: MODES:    'full',   'blank',    'first',   'vowels',   'misc',   'ends', 

(Not case sensitive)
        
    """
    url = f"https://bible-memory-verse-flashcard.p.rapidapi.com/get_chapter"
    querystring = {'book_name': book_name, }
    if chapter:
        querystring['chapter'] = chapter
    if text_mode:
        querystring['text_mode'] = text_mode
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "bible-memory-verse-flashcard.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

