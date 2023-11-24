import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def summarize_recipe(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Summarize the recipe in a short text."
    id: The id of the recipe to summarize.
        
    """
    url = f"https://webknox-recipes.p.rapidapi.com/recipes/{is_id}/summary"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webknox-recipes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def extract_recipe_data(url: str, forceextraction: bool=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Extract recipe data from a recipe blog or Web page."
    url: The URL of the recipe page.
        forceextraction: If true, the extraction will be triggered no matter whether we know the recipe already. Use that only if information is missing as this operation is slower.
        
    """
    url = f"https://webknox-recipes.p.rapidapi.com/recipes/extract"
    querystring = {'url': url, }
    if forceextraction:
        querystring['forceExtraction'] = forceextraction
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webknox-recipes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def compute_daily_meal_plan(timeframe: str='day', targetcalories: int=2000, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Compute a meal plan for a day."
    timeframe: For one day or a complete week, allowed values are "day" and "week".
        targetcalories: The target number of calories per day.
        
    """
    url = f"https://webknox-recipes.p.rapidapi.com/recipes/mealplans/generate"
    querystring = {}
    if timeframe:
        querystring['timeFrame'] = timeframe
    if targetcalories:
        querystring['targetCalories'] = targetcalories
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webknox-recipes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def quick_answer(q: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Answer a nutrition related natural language question."
    q: The nutrition-related question.
        
    """
    url = f"https://webknox-recipes.p.rapidapi.com/recipes/quickAnswer"
    querystring = {'q': q, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webknox-recipes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def find_similar_recipes(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Find recipes which are similar to the given one."
    id: The id of the source recipe to which similar recipes should be found.
        
    """
    url = f"https://webknox-recipes.p.rapidapi.com/recipes/{is_id}/similar"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webknox-recipes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def recipe_information(is_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get information about a recipe."
    id: The id of the recipe.
        
    """
    url = f"https://webknox-recipes.p.rapidapi.com/recipes/{is_id}/information"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webknox-recipes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def search_recipes(query: str, offset: int=0, number: int=10, type: str='main course', cuisine: str='italian', diet: str='vegetarian', intolerances: str='egg, gluten', excludeingredients: str='coconut', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search recipes in natural language."
    query: The (natural language) search query.
        offset: The number of results to skip (between 0 and 900).
        number: The number of results to return (between 0 and 100).
        type: The type of the recipes. One of the following: main course, side dish, dessert, appetizer, salad, bread, breakfast, soup, beverage, sauce, or drink.
        cuisine: The cuisine(s) of the recipes. One or more (comma separated) of the following: african, chinese, japanese, korean, vietnamese, thai, indian, british, irish, french, italian, mexican, spanish, middle eastern, jewish, american, cajun, southern, greek, german, nordic, eastern european, caribbean, or latin american.
        diet: The diet to which the recipes must be compliant. Possible values are: pescetarian, lacto vegetarian, ovo vegetarian, vegan, and vegetarian.
        intolerances: A comma-separated list of intolerances. All found recipes must not have ingredients that could cause problems for people with one of the given tolerances. Possible values are: dairy, egg, gluten, peanut, sesame, seafood, shellfish, soy, sulfite, tree nut, and wheat.
        excludeingredients: An comma-separated list of ingredients or ingredient types that must not be contained in the recipes.
        
    """
    url = f"https://webknox-recipes.p.rapidapi.com/recipes/search"
    querystring = {'query': query, }
    if offset:
        querystring['offset'] = offset
    if number:
        querystring['number'] = number
    if type:
        querystring['type'] = type
    if cuisine:
        querystring['cuisine'] = cuisine
    if diet:
        querystring['diet'] = diet
    if intolerances:
        querystring['intolerances'] = intolerances
    if excludeingredients:
        querystring['excludeIngredients'] = excludeingredients
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webknox-recipes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def find_by_ingredients(ingredients: str, number: str='5', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Find recipes that use as many of the given ingredients as possible and have as little as possible missing ingredients."
    ingredients: A comma-separated list of ingredients that the recipes should contain.
        number: The maximal number of recipes to return (default = 5).
        
    """
    url = f"https://webknox-recipes.p.rapidapi.com/recipes/findByIngredients"
    querystring = {'ingredients': ingredients, }
    if number:
        querystring['number'] = number
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webknox-recipes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def autocomplete_ingredient_search(query: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Autocomplete a search for an ingredient."
    query: The query - a partial of complete ingredient name.
        
    """
    url = f"https://webknox-recipes.p.rapidapi.com/food/ingredients/autocomplete"
    querystring = {'query': query, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "webknox-recipes.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

