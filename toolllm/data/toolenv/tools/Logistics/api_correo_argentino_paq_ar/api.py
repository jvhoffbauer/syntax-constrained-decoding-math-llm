import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def precio(altocm: int, anchocm: int, profundidadcm: int, entrega: str, pesopaquetekg: int, tipo: str, codigopostaldestino: str, iva: str, codigopostalorigen: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "API MiCorreo ePaq - Correo Argentino
		
		Precio
		
		Token:"Solicitar mas info por Email"
		Contacto:"info@dapipro.com"
		Endpoint: "https://ca.dapipro.com/precio""
    entrega: D = Domicilio
S = Sucursal
        tipo: CP = Envio Clasico
EP = Envio Expreso
        iva: 1 = Precio con iva
0 = Precio sin iva
        
    """
    url = f"https://api-correo-argentino-paq-ar.p.rapidapi.com/precio/{codigopostalorigen}/{codigopostaldestino}/{iva}/{tipo}/{entrega}/{pesopaquetekg}/{altocm}/{anchocm}/{profundidadcm}"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "api-correo-argentino-paq-ar.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

