import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_social_timestamps_15m(social: str, timestamp: str='24h', tickers: str='PLTR,BTC-USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a ticker and capture the total posts, comments, likes, impressions over a specified timeframe. Each timeframe is grouped by time intervals specified below."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-timestamps/15m"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if tickers:
        querystring['tickers'] = tickers
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_alerts(notificationtypes: str='financial-news', tickers: str='TSLA,AMZN', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for alert notifications that identify changes in trading (price & volume), financial, & company news/announcement activities for a given stock or cryptocurrency."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-alerts"
    querystring = {}
    if notificationtypes:
        querystring['notificationTypes'] = notificationtypes
    if tickers:
        querystring['tickers'] = tickers
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_content(tickers: str, limit: int=10, extended: str='false', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Content Articles
		Search for the latest Utradea generated articles that cover analysis, commentary, & due dilligence for a given stock or cryptocurrency."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-content"
    querystring = {'tickers': tickers, }
    if limit:
        querystring['limit'] = limit
    if extended:
        querystring['extended'] = extended
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_notifications(tickers: str, social: str, timestamp: str, limit: int=10, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Social Sentiment Notifications
		Search for notifications that identify changes in social media activity for a given stock or cryptocurrency on Twitter, StockTwits, and Reddit."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-notifications"
    querystring = {'tickers': tickers, 'social': social, 'timestamp': timestamp, }
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_timestamps_4h(social: str, timestamp: str='24h', tickers: str='PLTR,BTC-USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a ticker and capture the total posts, comments, likes, impressions over a specified timeframe. Social Activity is grouped by 4 hour intervals"
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-timestamps/4h"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if tickers:
        querystring['tickers'] = tickers
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_sentiment_trending_bullish(social: str, timestamp: str='24h', iscrypto: str='false', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for top 50 trending bullish stocks/crypto symbols on Twitter/StockTwits."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-sentiment-trending/bullish"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_stats_influencers(social: str, iscrypto: str='false', timestamp: str='24h', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a stock or cryptocurrency's sentiment statistics from posts generated on Twitter or Stocktwits by user post category (influencers,spam,bot)."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-stats/influencers"
    querystring = {'social': social, }
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if timestamp:
        querystring['timestamp'] = timestamp
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_stats_spam(social: str, iscrypto: str='false', limit: str='10', timestamp: str='24h', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a stock or cryptocurrency's sentiment statistics from posts generated on Twitter or Stocktwits by user post category (influencers,spam,bot)."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-stats/spam"
    querystring = {'social': social, }
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if limit:
        querystring['limit'] = limit
    if timestamp:
        querystring['timestamp'] = timestamp
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_stats_bots(social: str, limit: str='10', iscrypto: str='false', timestamp: str='24h', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a stock or cryptocurrency's sentiment statistics from posts generated on Twitter or Stocktwits by user post category (influencers,spam, bot)."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-stats/bots"
    querystring = {'social': social, }
    if limit:
        querystring['limit'] = limit
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if timestamp:
        querystring['timestamp'] = timestamp
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_sentiment_change_bearish(social: str, limit: str='10', timestamp: str='24h', iscrypto: str='false', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for top 50 trending stocks or crypto symbols on social media with the greatest change in bullish or bearish sentiment on Twitter/StockTwits."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-sentiment-change/bearish"
    querystring = {'social': social, }
    if limit:
        querystring['limit'] = limit
    if timestamp:
        querystring['timestamp'] = timestamp
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_sentiment_change_bullish(social: str, timestamp: str='24h', iscrypto: str='false', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for top 50 trending stocks or crypto symbols on social media with the greatest change in bullish or bearish sentiment on Twitter/StockTwits."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-sentiment-change/bullish"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_sentiment_trending_bearish(social: str, limit: str='10', timestamp: str='24h', iscrypto: str='false', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for top 50 trending bearish stocks/crypto symbols on Twitter/StockTwits."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-sentiment-trending/bearish"
    querystring = {'social': social, }
    if limit:
        querystring['limit'] = limit
    if timestamp:
        querystring['timestamp'] = timestamp
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_filtered_feed(social: str, tickers: str='PLTR,BTC-USD', limit: str='10', timestamp: str='24h', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search posts from Twitter or StockTwits that mention specified tickers. In the additional feeds provided, Utradea filters posts on your behalf based on our spam criteria and returns posts that reaches 10,000+ impressions."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-filtered-feed"
    querystring = {'social': social, }
    if tickers:
        querystring['tickers'] = tickers
    if limit:
        querystring['limit'] = limit
    if timestamp:
        querystring['timestamp'] = timestamp
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_feed(social: str, limit: str='10', timestamp: str='24h', tickers: str='PLTR,BTC-USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search posts from Twitter or StockTwits that mention specified tickers. In the additional feeds provided, Utradea filters posts on your behalf based on our spam criteria and returns posts that reaches 10,000+ impressions."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-feed"
    querystring = {'social': social, }
    if limit:
        querystring['limit'] = limit
    if timestamp:
        querystring['timestamp'] = timestamp
    if tickers:
        querystring['tickers'] = tickers
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_change_impressions(social: str, timestamp: str='24h', limit: str='10', iscrypto: str='false', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search the top 50 tickers trending on social media with the greatest change in impressions."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-change/impressions"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if limit:
        querystring['limit'] = limit
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_change_posts(social: str, timestamp: str='24h', iscrypto: str='false', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search the top 50 tickers trending on social media with the greatest change in posts."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-change/posts"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_trending_impressions(social: str, iscrypto: str='false', timestamp: str='24h', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search the top 50 tickers trending on social media by impressions."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-trending/impressions"
    querystring = {'social': social, }
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if timestamp:
        querystring['timestamp'] = timestamp
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_trending_likes(social: str, timestamp: str='24h', iscrypto: str='false', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search the top 50 tickers trending on social media by likes."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-trending/likes"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_trending_comments(social: str, iscrypto: str='false', timestamp: str='24h', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search the top 50 tickers trending on social media by comments."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-trending/comments"
    querystring = {'social': social, }
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if timestamp:
        querystring['timestamp'] = timestamp
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_trending_posts(social: str, timestamp: str='24h', iscrypto: str='false', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search the top 50 tickers trending on social media by posts."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-trending/posts"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if iscrypto:
        querystring['isCrypto'] = iscrypto
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_moving_averages_1m(tickers: str, social: str, limit: str='10', timestamp: str='24h', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a ticker and capture the moving average of posts, comments, likes, and impressions within a specified timeframe. The recorded social moving average is grouped by monthly intervals."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-moving-averages/1m"
    querystring = {'tickers': tickers, 'social': social, }
    if limit:
        querystring['limit'] = limit
    if timestamp:
        querystring['timestamp'] = timestamp
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_moving_averages_2w(social: str, tickers: str, timestamp: str='24h', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a ticker and capture the moving average of posts, comments, likes, and impressions within a specified timeframe. The recorded social moving average is grouped by 2-week intervals."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-moving-averages/2w"
    querystring = {'social': social, 'tickers': tickers, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_moving_averages_1w(social: str, tickers: str, limit: str='10', timestamp: str='24h', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a ticker and capture the moving average of posts, comments, likes, and impressions within a specified timeframe. The recorded social moving average is grouped by 1 week intervals."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-moving-averages/1w"
    querystring = {'social': social, 'tickers': tickers, }
    if limit:
        querystring['limit'] = limit
    if timestamp:
        querystring['timestamp'] = timestamp
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_moving_averages_72h(tickers: str, social: str, timestamp: str='24h', limit: str='10', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a ticker and capture the moving average of posts, comments, likes, and impressions within a specified timeframe. The recorded social moving average is grouped by 72-hour intervals."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-moving-averages/72h"
    querystring = {'tickers': tickers, 'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if limit:
        querystring['limit'] = limit
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_timestamps_1d(social: str, timestamp: str='24h', tickers: str='PLTR,BTC-USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a ticker and capture the total posts, comments, likes, impressions over a specified timeframe. Social activity is grouped by 1 day intervals"
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-timestamps/1d"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if tickers:
        querystring['tickers'] = tickers
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_timestamps_1h(social: str, timestamp: str='24h', tickers: str='PLTR,BTC-USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a ticker and capture the total posts, comments, likes, impressions over a specified timeframe. Social activity is grouped by 1-hour intervals"
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-timestamps/1h"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if tickers:
        querystring['tickers'] = tickers
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_timestamps_30m(social: str, timestamp: str='24h', tickers: str='PLTR,BTC-USD', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Search for a ticker and capture the total posts, comments, likes, impressions over a specified timeframe. Social activity is grouped in 30 min intervals."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-timestamps/30m"
    querystring = {'social': social, }
    if timestamp:
        querystring['timestamp'] = timestamp
    if tickers:
        querystring['tickers'] = tickers
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_social_list(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a list of tickers across social media platforms: Twitter, StockTwits, and Reddit. These are tickers that are currently mentioned across each platform. 
		Use these tickers to query the remaining endpoints."
    
    """
    url = f"https://finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com/get-social-list"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "finance-social-sentiment-for-twitter-and-stocktwits.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

