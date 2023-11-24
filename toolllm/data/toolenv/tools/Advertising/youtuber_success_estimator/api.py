import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def estimate(channeltype: str, channelname: str='chrispirillo', channelid: str='UChQl2YkLt3dj-KDyGUBzcHw', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Submit a YouTube `channelId` value along with the `channelType` as query param values appended to the endpoint for getting back the estimated video view performance of the submitted channel.
		
		## Example
		This submits a request for the estimated 30 day video view performance of the YouTube channel with that unique `channelId` value provided in the query param
		
		`GET /api/v0/dmt_estimator?channelId=UChQl2YkLt3dj-KDyGUBzcHw&channelType=youtube`
		
		## FAQ
		
		Q. Does the DMT Channel Estimator support other platforms like TikTok?
		A. This is currently planned and in development - if you have ideas for other platforms you'd like to be supported feel free to reach out!
		
		Q.  What is the accuracy of the estimations?
		A. This estimator has been tested in dozens of real-life campaigns with clients spending 6-7 figures on each influencer native ad campaign, totaling out in a median margin of error of 10%. Not bad!
		
		We will say that while most channels have a certain degree of predictability in terms of performance, more popular *and* less frequently posting channels are outliers that the estimator will only be so accurate in estimating.
		
		Q. So no guarantees? How should I use this?
		A. Use it like the creators of the API have: as a way to understand baseline performance of a given influencer's channel and how you can back out of that with your own campaign's goals to a pricing number that makes sense.
		
		Q. Is there an offering for this API to integrate *directly* into my application?
		A. Yes, feel free to reach out and we can discuss more custom integrations including callback url support
		
		Q. Can I reach out if I am interested in doing a YouTube or broader influencer campaign activation?
		A. Yes, feel free to reach out and we can make a recommendation to you: [Best of Bold Agency](https://www.bestofbold.com/?utm_source=dmt-estimator)
		
		Q. What is the SLA for fixing bugs?
		A. ASAP! We dont have one much more official than that, we are focused availability and making sure the predictions are as accurate as possible
		
		Q. Will you expose the prediction model?
		A. No plans to do this for now, if you have ideas for prediction models or if and how you would like to incorporate your own, feel free to reach out!"
    channelname: Lookup a channel projection by the given name of the channel. Either channelName or channelId is required
        channelid: Lookup the channel projection by the unique id provided by the channel's host platform (for example: YouTube, TikTok, Twitch). Either channelId or channelName is required
        
    """
    url = f"https://youtuber-success-estimator.p.rapidapi.com/api/v0/analytics/creators/estimator"
    querystring = {'channelType': channeltype, }
    if channelname:
        querystring['channelName'] = channelname
    if channelid:
        querystring['channelId'] = channelid
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "youtuber-success-estimator.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

