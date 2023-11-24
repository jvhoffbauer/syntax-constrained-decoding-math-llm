import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def retrieveaattachmentdetails(checkattachmentid: str, checkid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " Retrieve details of existing attachment.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>checkId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the check.</p>
		  </td></tr>
		 <tr>
		  <td><b>checkAttachmentId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the check attachment.</p>
		  </td></tr>
		</tbody>
		</table>
		
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/checks/{checkid}/attachments/{checkattachmentid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrievevoucherbycheckid(checkid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Details of an existing voucher. It can be retrieve by passing checkId as well as retrieve directly by passing voucherId.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>checkId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the check to retrieve associated voucher.</p>
		  </td></tr>
		</tbody>
		</table>"
    
    """
    url = f"https://ocw.p.rapidapi.com/checks/{checkid}/voucher"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveallchecks(page: str, term: str, perpage: str, status: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List all check records
		
		<b>Query parameters</b>
		<table>
		 <tr>
		  <td><b>perPage</b></td>
		    <td><p> Number of records that you want to receive in the response,By default 10 records will be 
		          listed</p></td>
		   </tr>
		  <tr>
		  <td><b>page</b></td>
		   <td><p> For navigating through pages ,By default first page will be listed</p> </td>
		  </tr>
		  <tr>
		    <td><b>term</b></td>
		    <td><p> Filter records by using any keywords</p></td>
		   </tr>
		 <tr>
		    <td><b>status</b></td>
		    <td><p>Filter records by using check status ,Eg:<code>voided</code> , <code>mailed</code> <code>refunded</code><code>emailed</code><code>eprinted</code><code>printed</code>
		      </p></td>
		   </tr>
		</tbody>
		</table>
		
		
		
		"
    page: By default first page will be listed
        term: Filter records by using any keywords
        perpage: Number of records that you want to receive in the response,By default 10 records will be listed
        status: Filter record by using check status 
        
    """
    url = f"https://ocw.p.rapidapi.com/checks"
    querystring = {'page': page, 'term': term, 'perPage': perpage, 'status': status, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveacheck(checkid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Details of an existing check.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>checkId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the check to retrieved.</p>
		  </td></tr>
		</tbody>
		</table>"
    
    """
    url = f"https://ocw.p.rapidapi.com/checks/{checkid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveallcustomfromaddresses(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List of all custom from address records.
		
		<b>Query parameters</b>
		<table>
		 <tr>
		  <td><b>perPage</b></td>
		    <td><p> Number of records that you want to receive in the response,By default 10 records will be 
		          listed</p></td>
		   </tr>
		  <tr>
		  <td><b>page</b></td>
		   <td><p> For navigating through pages ,By default first page will be listed</p> </td>
		  </tr>
		</table>
		
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/customFromAddresses"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveacustomtoaddress(customtoaddressid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Details of custom to address.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>customToAddressId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the Custom to address to be retrieve.</p>
		  </td></tr>
		</tbody>
		</table>
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/customToAddresses/{customtoaddressid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveallcustomtoaddresses(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List of all custom to address records
		
		
		<b>Query parameters</b>
		<table>
		 <tr>
		  <td><b>perPage</b></td>
		    <td><p> Number of records that you want to receive in the response,By default 10 records will be 
		          listed</p></td>
		   </tr>
		  <tr>
		  <td><b>page</b></td>
		   <td><p> For navigating through pages ,By default first page will be listed</p> </td>
		  </tr>
		 
		</tbody>
		</table>
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/customToAddresses"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveallpayees(term: str, perpage: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List all payee records.
		
		<b>Query parameters</b>
		<table>
		 <tr>
		  <td><b>perPage</b></td>
		    <td><p> Number of records that you want to receive in the response,By default 10 records will be 
		          listed</p></td>
		   </tr>
		  <tr>
		  <td><b>page</b></td>
		   <td><p> For navigating through pages ,By default first page will be listed</p> </td>
		  </tr>
		  <tr>
		    <td><b>term</b></td>
		    <td><p> Filter records by using any keywords</p></td>
		   </tr>
		</tbody>
		</table>
		"
    term: Filter records by using any keywords
        perpage: Number of records that you want to receive in the response,By default 10 records will be listed
        page: By default first page will be listed
        
    """
    url = f"https://ocw.p.rapidapi.com/payees"
    querystring = {'term': term, 'perPage': perpage, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveapayee(payeeid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Details of an existing payee.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>payeeId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the payee to retrieve</p>
		  </td></tr>
		</tbody>
		</table>"
    
    """
    url = f"https://ocw.p.rapidapi.com/payees/{payeeid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveacustomfromaddress(customfromaddressid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Details of custom from address.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>customFromAddressId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the Custom from address to be retrieved.</p>
		  </td></tr>
		</tbody>
		</table>
		
		
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/customFromAddresses/{customfromaddressid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveallattachmentsdetails(checkid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve all attachments of a existing check.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>checkId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the check.</p>
		  </td></tr>
		</tbody>
		</table>
		
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/checks/{checkid}/attachments"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveallmailattachments(checkid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List of all mail attachments on a check,This attachments will include when create mail with this check.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>checkId</b></td>
		  <td><b>Required</b>    
		        <p> Id of the Check.</p>
		  </td></tr>
		</tbody>
		</table>
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/mailchecks/{checkid}/attachments"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveallmailoptions(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve all available mail options,including shipping types,Paper types and Inform types,You can use this data to create mail check."
    
    """
    url = f"https://ocw.p.rapidapi.com/mailchecks/mailingOptions"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrievevoucher(voucherid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Details of an existing voucher. It can be retrieve by passing checkId as well as retrieve directly by passing voucherId.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>voucherId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the voucher to be retrieved.</p>
		  </td></tr>
		</tbody>
		</table>
		
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/vouchers/{voucherid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getstatus(checkid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://ocw.p.rapidapi.com/ach/{checkid}/status"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveallbankaccounts(page: str, term: str, perpage: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List all bank account records.
		
		<b>Query parameters</b>
		<table>
		 <tr>
		  <td><b>perPage</b></td>
		    <td><p> Number of records that you want to receive in the response,By default 10 records will be 
		          listed</p></td>
		   </tr>
		  <tr>
		  <td><b>page</b></td>
		   <td><p> For navigating through pages ,By default first page will be listed</p> </td>
		  </tr>
		  <tr>
		    <td><b>term</b></td>
		    <td><p> Filter records by using any keywords</p></td>
		   </tr>
		</tbody>
		</table>
		
		"
    page: By default first page will be listed
        term: Filter records by using any keywords
        perpage: Number of records that you want to receive in the response,By default 10 records will be listed
        
    """
    url = f"https://ocw.p.rapidapi.com/bankAccounts"
    querystring = {'page': page, 'term': term, 'perPage': perpage, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveabankaccount(bankaccountid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Details of an existing bank account.
		
		<b>Path parameters</b>
		<table>
		 <tr>
		  <td><b>bankAccountId</b></td>
		  <td><b>Required</b>    
		        <p> The id of the Bank account to be retrieved.</p>
		  </td></tr>
		</tbody>
		</table>
		
		
		
		
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/bankAccounts/{bankaccountid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getallstatus(checkid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://ocw.p.rapidapi.com/ach/{checkid}/statusAll"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrieveallcategories(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List of all category records.
		
		
		<b>Query parameters</b>
		<table>
		 <tr>
		  <td><b>perPage</b></td>
		    <td><p> Number of records that you want to receive in the response,By default 10 records will be 
		          listed</p></td>
		   </tr>
		  <tr>
		  <td><b>page</b></td>
		   <td><p> For navigating through pages ,By default first page will be listed</p> </td>
		  </tr>
		  <tr>
		    <td><b>term</b></td>
		    <td><p> Filter records by using any keywords</p></td>
		   </tr>
		</tbody>
		</table>
		"
    
    """
    url = f"https://ocw.p.rapidapi.com/categories"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def retrievecustomerbankaccount(customerbankaccountid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve customer bank account"
    
    """
    url = f"https://ocw.p.rapidapi.com/getpaid-by-form/bank-account/{customerbankaccountid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getcustomerdetails(customerid: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://ocw.p.rapidapi.com/getpaid-by-form/customer/{customerid}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def getallshorturl(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " "
    
    """
    url = f"https://ocw.p.rapidapi.com/getpaid-by-form/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "ocw.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

