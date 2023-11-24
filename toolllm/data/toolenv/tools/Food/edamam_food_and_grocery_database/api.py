import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def api_food_database_v2_parser(nutrients_water: str=None, nutrients_k: str=None, nutrients_sugar_added: str=None, nutrients_fibtg: str=None, nutrients_vitk1: str=None, nutrients_thia: str=None, nutrients_folac: str=None, nutrients_sugar: str=None, nutrients_vitc: str=None, nutrients_ribf: str=None, nutrients_chocdf_net: str=None, nutrients_chocdf: str=None, nutrients_vitd: str=None, ingr: str=None, nutrition_type: str='cooking', nutrients_foldfe: str=None, nutrients_tocpha: str=None, nutrients_mg: str=None, nutrients_chole: str=None, nutrients_fat: str=None, nutrients_procnt: str=None, nutrients_fe: str=None, category: str='[
  "generic-foods"
]', nutrients_fatrn: str=None, calories: str=None, upc: str=None, nutrients_vitb6a: str=None, nutrients_fams: str=None, nutrients_enerc_kcal: str=None, nutrients_fasat: str=None, nutrients_na: str=None, nutrients_p: str=None, nutrients_fapu: str=None, nutrients_ca: str=None, nutrients_vitb12: str=None, nutrients_zn: str=None, health: str='[
  "alcohol-free"
]', nutrients_nia: str=None, brand: str=None, nutrients_vita_rae: str=None, nutrients_folfd: str=None, nutrients_sugar_alcohol: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The parser access point handles text search for foods as well as filters for the foods like presence specific nutrient content or exclusion of allergens. <ul> <li>Search for a phrase or keyword using NLP to get food entities from it.</li> <li> Get basic nutrition facts and ingredients for each food </li> <li> Search for food by given nutrient quantity for 28 nutrients </li> <li> Search for foods within a given brand </li> <li> With the build in food-logging context it allows for requests which do not contain quantity and suggest expected quantities for them. </li> </ul>
		 
		 <b>Access Point:</b> https://api.edamam.com/api/food-database/v2/parser"
    nutrients_water: Water. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_k: Potassium, K. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_sugar_added: Sugars, added. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_fibtg: Fiber, total dietary. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_vitk1: Vitamin K (phylloquinone). Unit: µg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_thia: Thiamin. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_folac: Folic acid. Unit: µg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_sugar: Sugars, total. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_vitc: Vitamin C, total ascorbic acid. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_ribf: Riboflavin. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_chocdf_net: Carbohydrates (net). Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_chocdf: Carbohydrate, by difference. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_vitd: Vitamin D (D2 + D3). Unit: µg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        ingr: A keyword search parameter to be found in the food name. <b>REQUIRED</b> if 'upc' <b>and</b> 'brand' are not specified. <b>NOT REQUIRED</b> if 'brand' is specified. <b>DO NOT POPULATE</b> if 'upc' is specified.
        nutrition_type: Select between cooking and food logging processor.
        nutrients_foldfe: Folate, DFE. Unit: µg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_tocpha: Vitamin E (alpha-tocopherol). Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_mg: Magnesium. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_chole: Cholesterol. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br>See calcium for an example for how to fill in the range.
        nutrients_fat: Total lipid (fat). Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_procnt: Protein. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_fe: Iron, Fe. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        category: Categories
        nutrients_fatrn: Fatty acids, total trans. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        calories: The format is calories=RANGE where RANGE is replaced by the value in kcal. RANGE is in one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative integer numbers. The + symbol needs to be properly encoded. Examples: “calories=100-300” will return all recipes with which have between 100 and 300 kcal per serving.
        upc: Valid UPC, EAN, or PLU code. <b>REQUIRED</b> if neither 'ingr' <b>nor</b> 'brand' are specified. <b>DO NOT POPULATE</b> otherwise.
        nutrients_vitb6a: Vitamin B6. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_fams: Fatty acids, total monounsaturated. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_enerc_kcal: Energy. Unit: kcal. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_fasat: Fatty acids, total saturated. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_na: Sodium, Na. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_p: Phosphorus, P. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_fapu: Fatty acids, total polyunsaturated. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_ca: Calcium, Ca. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> For example: nutrients[CA]=50+ means minimum 50mg calcium, where ‘50+’ has to be properly encoded as ‘50%2B’ nutrients[FAT]=30 means maximum 30g fat and nutrients[FE]=5-10 means iron between 5mg and 10mg inclusive
        nutrients_vitb12: Vitamin B12. Unit: µg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_zn: Zinc, Zn. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        health: Health label
        nutrients_nia: Niacin. Unit: mg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        brand: A keyword search parameter to be found in the food's brand. <b>REQUIRED</b> if 'ingr' <b>and</b> 'upc' are not specified. <b>NOT REQUIRED</b> if 'ingr' is specified. <b>DO NOT POPULATE</b> if 'upc' is specified.
        nutrients_vita_rae: Vitamin A, RAE. Unit: µg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_folfd: Folate (food). Unit: µg. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        nutrients_sugar_alcohol: Sugar alcohols. Unit: g. Input the range which is one of MIN+, MIN-MAX or MAX, where MIN and MAX are non-negative floating point numbers. <br> <br> See calcium for an example for how to fill in the range.
        
    """
    url = f"https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"
    querystring = {}
    if nutrients_water:
        querystring['nutrients[WATER]'] = nutrients_water
    if nutrients_k:
        querystring['nutrients[K]'] = nutrients_k
    if nutrients_sugar_added:
        querystring['nutrients[SUGAR.added]'] = nutrients_sugar_added
    if nutrients_fibtg:
        querystring['nutrients[FIBTG]'] = nutrients_fibtg
    if nutrients_vitk1:
        querystring['nutrients[VITK1]'] = nutrients_vitk1
    if nutrients_thia:
        querystring['nutrients[THIA]'] = nutrients_thia
    if nutrients_folac:
        querystring['nutrients[FOLAC]'] = nutrients_folac
    if nutrients_sugar:
        querystring['nutrients[SUGAR]'] = nutrients_sugar
    if nutrients_vitc:
        querystring['nutrients[VITC]'] = nutrients_vitc
    if nutrients_ribf:
        querystring['nutrients[RIBF]'] = nutrients_ribf
    if nutrients_chocdf_net:
        querystring['nutrients[CHOCDF.net]'] = nutrients_chocdf_net
    if nutrients_chocdf:
        querystring['nutrients[CHOCDF]'] = nutrients_chocdf
    if nutrients_vitd:
        querystring['nutrients[VITD]'] = nutrients_vitd
    if ingr:
        querystring['ingr'] = ingr
    if nutrition_type:
        querystring['nutrition-type'] = nutrition_type
    if nutrients_foldfe:
        querystring['nutrients[FOLDFE]'] = nutrients_foldfe
    if nutrients_tocpha:
        querystring['nutrients[TOCPHA]'] = nutrients_tocpha
    if nutrients_mg:
        querystring['nutrients[MG]'] = nutrients_mg
    if nutrients_chole:
        querystring['nutrients[CHOLE]'] = nutrients_chole
    if nutrients_fat:
        querystring['nutrients[FAT]'] = nutrients_fat
    if nutrients_procnt:
        querystring['nutrients[PROCNT]'] = nutrients_procnt
    if nutrients_fe:
        querystring['nutrients[FE]'] = nutrients_fe
    if category:
        querystring['category'] = category
    if nutrients_fatrn:
        querystring['nutrients[FATRN]'] = nutrients_fatrn
    if calories:
        querystring['calories'] = calories
    if upc:
        querystring['upc'] = upc
    if nutrients_vitb6a:
        querystring['nutrients[VITB6A]'] = nutrients_vitb6a
    if nutrients_fams:
        querystring['nutrients[FAMS]'] = nutrients_fams
    if nutrients_enerc_kcal:
        querystring['nutrients[ENERC_KCAL]'] = nutrients_enerc_kcal
    if nutrients_fasat:
        querystring['nutrients[FASAT]'] = nutrients_fasat
    if nutrients_na:
        querystring['nutrients[NA]'] = nutrients_na
    if nutrients_p:
        querystring['nutrients[P]'] = nutrients_p
    if nutrients_fapu:
        querystring['nutrients[FAPU]'] = nutrients_fapu
    if nutrients_ca:
        querystring['nutrients[CA]'] = nutrients_ca
    if nutrients_vitb12:
        querystring['nutrients[VITB12]'] = nutrients_vitb12
    if nutrients_zn:
        querystring['nutrients[ZN]'] = nutrients_zn
    if health:
        querystring['health'] = health
    if nutrients_nia:
        querystring['nutrients[NIA]'] = nutrients_nia
    if brand:
        querystring['brand'] = brand
    if nutrients_vita_rae:
        querystring['nutrients[VITA_RAE]'] = nutrients_vita_rae
    if nutrients_folfd:
        querystring['nutrients[FOLFD]'] = nutrients_folfd
    if nutrients_sugar_alcohol:
        querystring['nutrients[Sugar.alcohol]'] = nutrients_sugar_alcohol
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def auto_complete(q: str, limit: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Edamam provides a convenient autocomplete functionality which can be implemented for use when searching for ingredients. Just send in the current query as the "q" parameter and the number of suggestions you wish to receive as the "limit" parameter. 
		 
		 <b>Access Point:</b> https://api.edamam.com/auto-complete"
    q: Query text. For example q=chi. This or the r parameter are required
        limit: response limit
        
    """
    url = f"https://edamam-food-and-grocery-database.p.rapidapi.com/auto-complete"
    querystring = {'q': q, }
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

