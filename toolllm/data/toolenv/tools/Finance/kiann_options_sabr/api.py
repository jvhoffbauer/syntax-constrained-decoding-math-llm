import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def local_hist(ccy: str, ret: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This function pulls out the latest 5 time-stamp snapshot of the 3-degree polynomial calibrated parameters, for local-Volatility model across the strike and expiry axis.
		There are choices of either 'btc' or 'eth'.
		
		The  parameters can be seen in the header of x^3, x^2*y, x^1 * y^2, etc, ......... and intercept."
    
    """
    url = f"https://kiann_options_sabr.p.rapidapi.com/local_hist"
    querystring = {'ccy_': ccy, }
    if ret:
        querystring['ret_'] = ret
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiann_options_sabr.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def sabr_hist(ccy: str, ret: int=0, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This function pulls out the latest 5 time-stamp snapshot of the SABR calibrated parameters.
		There are choices of either 'btc' or 'eth'.
		
		The data returns, amongst, the time-to-expiry, the error-in-calibration (where error = sum[abs(target_vol - sabr_vol)]"
    
    """
    url = f"https://kiann_options_sabr.p.rapidapi.com/sabr_hist"
    querystring = {'ccy_': ccy, }
    if ret:
        querystring['ret_'] = ret
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiann_options_sabr.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def sabr_calib(ret: int, vols: str, time: int, k: str, beta: int, fwd: int, shift: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "A simplistic least-error fit to retrieve sabr parameters given arrays of (lognormal)vols and strikes. Note that, it does not explicitly calibrate to ATMF vols.
		
		Params as per below.
		params = {"fwd_" : 1655, "shift_": 0.0, "time_": 0.159, "beta" : 0.9, "k_": [strikes_], "vols_": [vols_], "ret_": 0}
		
		Note that in the (python) request.get, k_ should be of format [x1, x2, x3,........ ] where there is no "", similarly for [vols_]"
    
    """
    url = f"https://kiann_options_sabr.p.rapidapi.com/sabr_calib"
    querystring = {'ret_': ret, 'vols_': vols, 'time_': time, 'k_': k, 'beta': beta, 'fwd_': fwd, 'shift_': shift, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiann_options_sabr.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def sabr_norm(shift: int, method: int, time: int, fwd: int, k: int, alpha: int, beta: int, ret: int, rho: int, volvol: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This is the implementation of the SABR model (z-shift) under the normal volatility mode, with the parameters as follows:
		K_ : strike, fwd_ : forward, shift_ : z-shift, time_ : time-to-expiry, alpha : sabr alpha, beta : sabr beta, rho : sabr rho, volvol : sabr volvol
		method_ : internal mode for two modes of calibration. Default of 1
		ret_ : set of 0, to return proper json format"
    
    """
    url = f"https://kiann_options_sabr.p.rapidapi.com/sabr_Norm"
    querystring = {'shift_': shift, 'method_': method, 'time_': time, 'fwd_': fwd, 'K_': k, 'alpha': alpha, 'beta': beta, 'ret_': ret, 'rho': rho, 'volvol': volvol, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiann_options_sabr.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def sabr_log(method: int, time: int, alpha: int, fwd: int, beta: int, rho: int, ret: int, volvol: int, shift: int, k: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This is the implementation of the SABR model (z-shift) under the Lognormal volatility mode, with the parameters as follows:
		K_ : strike, fwd_ : forward, shift_ : z-shift, time_ : time-to-expiry, alpha : sabr alpha, beta : sabr beta, rho : sabr rho, volvol : sabr volvol
		method_ : internal mode for two modes of calibration. Default of 1
		ret_ : set of 0, to return proper json format"
    
    """
    url = f"https://kiann_options_sabr.p.rapidapi.com/sabr_log"
    querystring = {'method_': method, 'time_': time, 'alpha': alpha, 'fwd_': fwd, 'beta': beta, 'rho': rho, 'ret_': ret, 'volvol': volvol, 'shift_': shift, 'K_': k, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiann_options_sabr.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def funcone(x2: int, x1: int, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Testing function for the SABR module"
    
    """
    url = f"https://kiann_options_sabr.p.rapidapi.com/funcOne"
    querystring = {'x2': x2, 'x1': x1, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kiann_options_sabr.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

