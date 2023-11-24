import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def sms_mt_send_sms_get(password: str, encoding: str, subaccountid: str, destination: str, body: str, source: str, scheduleddatetime: str, umid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Send a SMS message using Wavecell HTTP GET"
    password: Your Wavecell Password
        encoding: The encoding format of the message
        subaccountid: Your Wavecell Sub Account ID
        destination: The destination phone number (MSISDN) to send to. This must be in international format without "+" such as 33123456789. 33 is the country code and 123456789 is the mobile number
        body: The message text
        source: This is the sender Id the message will appear from, TPOA. Only available on agreed routes with your account manager.
        accountid: Your Wavecell Account ID
        scheduleddatetime: Specify this if you wish to schedule your message up to 7 days in advance, to be specified in UTC Time. Specify this parameter blank if you do not want to schedule your message. SET 0 IF NOT REQUIRED
        
    """
    url = f"https://wavecell.p.rapidapi.com/Send.asmx/SendMT"
    querystring = {'password': password, 'encoding': encoding, 'subaccountid': subaccountid, 'destination': destination, 'body': body, 'source': source, 'scheduleddatetime': scheduleddatetime, 'umid': umid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wavecell.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_delivery_status(accountid: str, subaccountid: str, password: str, umid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This API should be used to retrieve the current delivery status of a message sent using Wavecell."
    accountid: Your Wavecell Accountid
        subaccountid: Your Wavecell subaccountid
        password: Your Wavecell password
        umid: The Unique Message ID of the SMS for which you want to retrieve the delivery status
        
    """
    url = f"https://wavecell.p.rapidapi.com/getDLRApi.asmx/SMSDLR"
    querystring = {'AccountID': accountid, 'Subaccountid': subaccountid, 'Password': password, 'umid': umid, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "wavecell.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

