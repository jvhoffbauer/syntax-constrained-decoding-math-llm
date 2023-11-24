import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def take_screenshot(targeturl: str, proxystate: str=None, proxycountry: str=None, clickdelay: int=500, fullpage: str=None, removables: str=None, clickcount: int=1, hastouch: str=None, clickselector: str=None, isfullyloaded: str=None, clickbutton: str=None, pageheight: int=1024, ismobile: str=None, pagewidth: int=1024, islandscape: str=None, devicescalefactor: int=1, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "collect all parameteres, load the webpage and take screenshot at the end.
		This API save on a S3 bucket and return the url."
    targeturl: Website url
        fullpage: take screenshot of the entire website page, from header to footer
        removables: remove divs/html by selector
        hastouch: Specify if the viewport supports touch events.
        clickselector: This method fetches an element with selector, scrolls it into view if needed, and then uses Page.mouse to click in the center of the element. If there's no element matching selector, the method throws an error.
        isfullyloaded: consider navigation to be finished when there are no more than 0 network connections for at least 500 ms. 
Than take screenshot
        clickbutton: Mouse button to be used, left click or right click etc
        pageheight: Set browser page height
        ismobile: Whether the meta viewport tag is taken into account.
        pagewidth: Set browser page width
        islandscape: Specifies if the viewport is in landscape mode.
        devicescalefactor: Specify device scale factor.
        
    """
    url = f"https://screenshot-maker.p.rapidapi.com/browser/screenshot/_take"
    querystring = {'targetUrl': targeturl, }
    if proxystate:
        querystring['proxyState'] = proxystate
    if proxycountry:
        querystring['proxyCountry'] = proxycountry
    if clickdelay:
        querystring['clickDelay'] = clickdelay
    if fullpage:
        querystring['fullpage'] = fullpage
    if removables:
        querystring['removables'] = removables
    if clickcount:
        querystring['clickCount'] = clickcount
    if hastouch:
        querystring['hasTouch'] = hastouch
    if clickselector:
        querystring['clickSelector'] = clickselector
    if isfullyloaded:
        querystring['isFullyLoaded'] = isfullyloaded
    if clickbutton:
        querystring['clickButton'] = clickbutton
    if pageheight:
        querystring['pageHeight'] = pageheight
    if ismobile:
        querystring['isMobile'] = ismobile
    if pagewidth:
        querystring['pageWidth'] = pagewidth
    if islandscape:
        querystring['isLandScape'] = islandscape
    if devicescalefactor:
        querystring['deviceScaleFactor'] = devicescalefactor
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "screenshot-maker.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

