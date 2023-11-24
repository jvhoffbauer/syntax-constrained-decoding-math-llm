import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def user_guide_detail(guideid: str, next_max_id: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user guide detail by guide id."
    
    """
    url = f"https://instagram203.p.rapidapi.com/userguidedetail/{guideid}/{next_max_id}"
    querystring = {}
    if next_max_id:
        querystring['next_max_id'] = next_max_id
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_information(username: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user info by username."
    
    """
    url = f"https://instagram203.p.rapidapi.com/userinfo/{username}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_highlights_list(userid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user highlights list by user id."
    
    """
    url = f"https://instagram203.p.rapidapi.com/userhighlightslist/{userid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_tv_channel(count: int, userid: int, end_cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user tv channel by user id."
    count: Range from 1 to 50
        end_cursor: Pagination cursor.
To get next batch of data, paste here **end_cursor** value that you have received in previous request response.
        
    """
    url = f"https://instagram203.p.rapidapi.com/usertv/{userid}/{count}/{end_cursor}"
    querystring = {}
    if end_cursor:
        querystring['end_cursor'] = end_cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_tagged_posts(userid: str, end_cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user tagged posts by user id."
    
    """
    url = f"https://instagram203.p.rapidapi.com/usertagpost/{userid}/{end_cursor}"
    querystring = {}
    if end_cursor:
        querystring['end_cursor'] = end_cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_stories(userid: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user stories by user id."
    
    """
    url = f"https://instagram203.p.rapidapi.com/userstories/{userid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_followers(count: int, userid: int, end_cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user followers by user id."
    count: Range from 1 to 100
        end_cursor: Pagination cursor.
To get next batch of data, paste here **end_cursor** value that you have received in previous request response.
        
    """
    url = f"https://instagram203.p.rapidapi.com/userfollowers/{userid}/{count}/{end_cursor}"
    querystring = {}
    if end_cursor:
        querystring['end_cursor'] = end_cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_posts(count: int, userid: int, end_cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user posts by user id."
    count: Range from 1 to 50
        end_cursor: Pagination cursor.
To get next batch of data, paste here **end_cursor** value that you have received in previous request response.
        
    """
    url = f"https://instagram203.p.rapidapi.com/userpost/{userid}/{count}/{end_cursor}"
    querystring = {}
    if end_cursor:
        querystring['end_cursor'] = end_cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_profile_picture(username: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user profile picture by username."
    
    """
    url = f"https://instagram203.p.rapidapi.com/userphoto/{username}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_contact_info(userid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user contact info by user id."
    
    """
    url = f"https://instagram203.p.rapidapi.com/usercontact/{userid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def userid(username: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user id by username"
    
    """
    url = f"https://instagram203.p.rapidapi.com/userid/{username}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def similar_users(userid: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get similar Instagram users by userid."
    
    """
    url = f"https://instagram203.p.rapidapi.com/usersimilaraccounts/{userid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_following(userid: int, count: int, end_cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user following by user id."
    count: Range from 1 to 100
        end_cursor: Pagination cursor.
To get next batch of data, paste here **end_cursor** value that you have received in previous request response.
        
    """
    url = f"https://instagram203.p.rapidapi.com/userfollowing/{userid}/{count}/{end_cursor}"
    querystring = {}
    if end_cursor:
        querystring['end_cursor'] = end_cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_guides(userid: int, count: int, end_cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user guides by user id."
    count: Range from 1 to 50
        end_cursor: Pagination cursor.
To get next batch of data, paste here **end_cursor** value that you have received in previous request response.
        
    """
    url = f"https://instagram203.p.rapidapi.com/userguides/{userid}/{count}/{end_cursor}"
    querystring = {}
    if end_cursor:
        querystring['end_cursor'] = end_cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def user_highlight_detail(highlightid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user highlight detail by highlight id."
    
    """
    url = f"https://instagram203.p.rapidapi.com/userhighlightdetail/{highlightid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def shortcode(shortcode: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Instagram shortcode special endpoint"
    
    """
    url = f"https://instagram203.p.rapidapi.com/ifshortcode/{shortcode}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def post_likes(count: int, shortcode: str, end_cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user post likes data by shortcode."
    count: Range from 1 to 50
        end_cursor: Pagination cursor.
To get next batch of data, paste here **end_cursor** value that you have received in previous request response.
        
    """
    url = f"https://instagram203.p.rapidapi.com/postlike/{shortcode}/{count}/{end_cursor}"
    querystring = {}
    if end_cursor:
        querystring['end_cursor'] = end_cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def post_comments(shortcode: str, end_cursor: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user post comments data by shortcode."
    end_cursor: Pagination cursor.
To get next batch of data, paste here end_cursor value that you have received in previous request response.

for example:
{\"server_cursor\": \"QVFCVWdxME1RejFmTlNmVjM5b1EwMXV3TkVzREpic1J0TUZ1MDdUOGpIWUsza0pTejF1dEZJV2dJcjNFcmpPZVhNWEZPR2h6UWNCNkdMd2tGRHI3NG1icWlyRDZGYl9ZZFhtNnpic3ZncEhraFE=\", \"is_server_cursor_inverse\": true}
        
    """
    url = f"https://instagram203.p.rapidapi.com/postcomment/{shortcode}/{end_cursor}"
    querystring = {}
    if end_cursor:
        querystring['end_cursor'] = end_cursor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def post_detail_data(shortcode: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get instagram user post detail by shortcode."
    shortcode: Instagram post shortcode.
        
    """
    url = f"https://instagram203.p.rapidapi.com/postinfo/{shortcode}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "instagram203.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

