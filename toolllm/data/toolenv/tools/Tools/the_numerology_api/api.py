import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def subconscious_self_number(name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Subconscious Self Number endpoint calculates the subconscious self number based on the Pythagorean numerology method. The subconscious self number represents the quantity of represented numbers in a given name, indicating an individual's capabilities and tendencies in dealing with various situations."
    name: The name used to calculate the subconscious self number.
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/subconscious_number"
    querystring = {'name': name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def challenge_number(birth_year: int, birth_month: int, birth_day: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Challenge Number Calculator endpoint allows you to calculate various challenge numbers based on a given birth date. The challenge numbers represent specific aspects or challenges that an individual may face in their life."
    birth_year: The year of birth (integer)
        birth_month: The month of birth (integer)
        birth_day: The day of birth (integer)
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/challenge_number"
    querystring = {'birth_year': birth_year, 'birth_month': birth_month, 'birth_day': birth_day, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def phone_number_analyzer(phone_number: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Phone Number Analyzer endpoint analyzes a person's phone number and calculates its vibration energy based on numerology. It provides information about the overall vibration of the phone number and the minor numbers that make up the number."
    phone_number: The phone number to analyze.
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/analyze_phone"
    querystring = {'phone_number': phone_number, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def personality_number_calculator(first_name: str, middle_name: str, last_name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Personality Number Calculator endpoint calculates the Personality Number based on the consonants in a person's full name at birth. The Personality Number reflects certain personality traits and characteristics of an individual."
    first_name: **(required)**: The first name of the person.
        middle_name: **(required)**: The middle name of the person.
        last_name: **(required)**: The last name of the person.
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/personality_number"
    querystring = {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def heart_s_desire_soul_urge_number(first_name: str, last_name: str, middle_name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Heart's Desire Number endpoint calculates the Heart's Desire Number based on the vowels in a person's full name at birth. The Soul Urge Number reflects the innermost desires and motivations of an individual."
    first_name: **(required)**: The first name of the person.
        last_name: **(required)**: The last name of the person.
        middle_name: **(required)**: The middle name of the person.
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/heart_desire"
    querystring = {'first_name': first_name, 'last_name': last_name, 'middle_name': middle_name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def personal_year_number(prediction_year: int, birth_month: int, birth_day: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Personal Year Number Calculator endpoint calculates the personal year number based on the provided date of birth and prediction year. The personal year number provides insights into the energies and experiences that may influence an individual during a particular year. By understanding the personal year number, users can gain awareness and make informed decisions in various aspects of their lives."
    prediction_year: **(integer)**: The year for which the personal year number is calculated.
        birth_month: **(integer)**: The month of birth of the person.
        birth_day: **(integer)**: The day of birth of the person.

        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/personal_year"
    querystring = {'prediction_year': prediction_year, 'birth_month': birth_month, 'birth_day': birth_day, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def karmic_lessons_numbers(full_name: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint calculates the karmic lessons based on the provided full name. Karmic lessons represent the missing numbers in the name and provide insights into areas of personal growth and development. The endpoint returns the list of karmic lessons and their corresponding summaries."
    full_name: The full name to analyze for karmic lessons.
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/karmic_lessons"
    querystring = {'full_name': full_name, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def karmic_debt_number(day: int, year: int, month: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Calculates the Karmic Debt Number based on the provided birth date. Accepts query parameters for birth year, month, and day."
    day: **(integer)**: The day of birth.
        year: **(integer)**: The year of birth.
        month: **(integer)**: The month of birth.
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/karmic_debt"
    querystring = {'day': day, 'year': year, 'month': month, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def attitude_sun_number(birth_month: int, birth_day: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Attitude/Sun Number endpoint calculates the Attitude Number, also known as the Sun Number, which represents the initial impression or appearance we portray to others when they first meet us."
    birth_month: The numeric value of the birth month **(1-12)**
        birth_day: The numeric value of the birth day **(1-31)**
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/attitude_number"
    querystring = {'birth_month': birth_month, 'birth_day': birth_day, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def expression_destiny_number_calculator(last_name: str, first_name: str, middle_name: str='Doe', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Expression/Destiny Number Calculator endpoint calculates the Destiny Number based on a person's first name, middle name, and last name. It also provides information about the Destiny Number."
    last_name: The last name of the person.
        first_name: The first name of the person.
        middle_name: The middle name of the person **(optional)**.
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/destiny_number"
    querystring = {'last_name': last_name, 'first_name': first_name, }
    if middle_name:
        querystring['middle_name'] = middle_name
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def calculate_life_path_number_get(month: int, year: int, day: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Calculates the numerology number and provides information about the life path based on the given name and date of birth."
    month: **(integer)**: The month of birth.
        year: **(integer)**: The year of birth.
        day: **(integer)**: The day of birth.
        
    """
    url = f"https://the-numerology-api.p.rapidapi.com/life_path"
    querystring = {'month': month, 'year': year, 'day': day, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "the-numerology-api.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

