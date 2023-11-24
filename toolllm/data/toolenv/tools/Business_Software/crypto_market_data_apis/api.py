import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def get_specific_rate(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get exchange rates between pair of requested assets pointing at a specific or current time."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/exchange-rates/btc/usd"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def latest_data(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get latest trades from all symbols up to 1 hour ago. Latest data is always returned in time descending order."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def latest_data_by_base_asset(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get latest trades from a specific base asset up to 1 hour ago. Latest data is always returned in time descending order."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/baseAsset/5b1ea92e584bf50020130612/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def latest_data_by_exchange_assets_pair(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get latest trades from a specific assets pair (exp. BTC / USD) in a specific exchange up to 1 hour ago. Latest data is always returned in time descending order."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/baseAsset/5b1ea92e584bf50020130612/quoteAsset/5b1ea92e584bf50020130615/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def historical_data(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get history transactions from specific symbol, returned in time ascending order. If no start & end time is defined when calling the endpoint, your data results will be provided 24 hours back, by default."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/5bfc329f9c40a100014dc5a7/history?period"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def historical_data_by_exchange(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get history transactions from specific exchange, returned in time ascending order. If no start & end time is defined when calling the endpoint, your data results will be provided 24 hours back, by default."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/exchange/5b1ea9d21090c200146f7362/history"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def historical_data_by_asset_pair(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get history transactions from specific assets pair (exp. BTC/USD), returned in time ascending order. If no start & end time is defined when calling the endpoint, your data results will be provided 24 hours back, by default."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/baseAsset/5b1ea92e584bf50020130612/quoteAsset/5b1ea92e584bf50020130615/history"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_chain_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "General information about a blockchain is available by GET-ing the base resource"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/info"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_block_height_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Height endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/blocks/1454902"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_latest_block_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Latest Block Endpoint gives you detail information for the latest block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/blocks/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_address_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The default Address Endpoint strikes a general information about addresses."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/address/2N6HeA8vi3LieVEpqz5ZBdcYzXpzTR55sT4"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_multisig_address_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Multisig Address Endpoint strikes a general information about a single address that is involved in multisignature addresses."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/address/mho4jHBcrNCncKt38trJahXakuaBnS7LK5/multisig"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_address_transactions_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Address Transactions Endpoint returns all information available about a particular address, including an array of complete transactions."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/address/msDJCunwFgiEhCpmPywoGzsbDpBQDbqLnA/transactions"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_get_wallet_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a Wallet or HDWallet based on its WALLET_NAME."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/wallets/wallet_name"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_list_wallets_hd_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a string array ($NAMEARRAY) of active wallet names (both normal ор HD) under the token you queried. You can then query detailed information on individual wallets (via their names) by leveraging the Get Wallet Endpoint.  Get Wallet Endpoint"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/wallets/hd"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_get_hd_wallet_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a WHDWallet based on its WALLET_NAME."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/wallets/hd/wallet"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_transaction_index_by_block_hash_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transaction Index by Block Endpoint returns detailed information about a list of transactions. The endpoint is useable both with block height and block hash. index and limit query parameters might also be used, as their default values are, as follows: 0, 1. Therefore, if none is specified the returned object will be the first transaction (the coinbase transaction) included in the block."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/txs/block/00000000000000000008b7233b8abb1519d0a1bc6579e209955539c303f3e6b1"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_unconfirmed_transactions_list_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Unconfirmed Transactions Endpoint returns an array of the latest transactions relayed by nodes in a blockchain that haven’t been included in any blocks."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/txs"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_webhook_list(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this resource you can list all web hooks that you have created."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/hooks"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_chain_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "General information about a blockchain is available by GET-ing the base resource"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/info"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_latest_block_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Latest Block Endpoint gives you detail information for the latest block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/blocks/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_address_transactions_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Address Transactions Endpoint returns all information available about a particular address, including an array of complete transactions."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/address/msDJCunwFgiEhCpmPywoGzsbDpBQDbqLnA/transactions"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_address_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The default Address Endpoint strikes a general information about addresses."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/address/2N6HeA8vi3LieVEpqz5ZBdcYzXpzTR55sT4"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_multisig_address_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Multisig Address Endpoint strikes a general information about a single address that is involved in multisignature addresses."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/address/mho4jHBcrNCncKt38trJahXakuaBnS7LK5/multisig"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_list_payments_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "To list your currently active payment forwarding addresses, you can use this endpoint."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/payments"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_list_of_past_forward_payments_by_users(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "To list your currently active payment forwarding addresses, you can use this endpoint."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/payments/history"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_webhook_list(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Using this resource you can list all web hooks that you have created."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/hooks"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_latest_block_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Latest Block Endpoint gives you detail information for the latest block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/blocks/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_block_height_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Height endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/blocks/3816116"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_chain_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "General information about a blockchain is available by GET-ing the base resource"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/info"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_block_hash_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Hash endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/blocks/0x79230d974f6cea8c11cc2f3a58c2b811313af17a2f7391de6665502910d4d383"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_address_info_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The default Address Endpoint strikes a balance between speed of response and data on Addresses. It returns information about the balance (in ETH) and transactions of a specified address."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/address/0x5b3457a50d39348ac15bef60e7f44a1941fe6502"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_transaction_by_address_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transactions By Address Endpoint returns all transactions specified by the query params: index and limit; The maxim value of limit is 50. The value in the returned transactions in WEI."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/address/0xc4618e88a2be9e6901019625ac5b627715d66422/transactions"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def transaction_hash_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transaction Hash Endpoint returns detailed information about a given transaction based on its hash."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/txs/hash/0x5d41df69ee87f712e76ee5f4dd6c0ccbec114b9d871340b7e2b34bf6d8d26c2c"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_transaction_index_endpoint_by_index_limit_block_number(endpoint: str, index: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transaction Index Endpoint by Index, Limit and Block Number returns detailed information about transactions for the block height defined, starting from the index defined up to the limit defined . In the example above index is 0 and limit is 4, therefore the response will be an array of 4 transactions starting from index 0. The highest number for the limit is 50."
    endpoint: endpoint
        index: index
        
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/txs/block/7178641?index"
    querystring = {'endpoint': endpoint, 'index': index, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_transaction_index_endpoint_by_block_hash(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transaction Index Endpoint by Block Hash returns detailed information about a given transaction based on its index and block hash."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/txs/block/0x0d13e81c01de31060a2830bb53761ef29ac5c4e5c1d43e309ca9a101140e394c/79"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_pending_transactions_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Pending Transactions Endpoint makes a call to the EVM and returns all pending transactions. The response might be limited if you lack credits."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/txs/pending"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_queued_transactions_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Queued Transactions Endpoint makes a call to the EVM and returns all queued transactions. The response might be limited if you lack credits."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/txs/queued"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_transactions_fee_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Transactions Fee Endpoint gives information about the gas price for the successfull transactions included in the last 1500 blocks. min shows the lowest gas price, max is the highest and average - the average gas price. recommended is the gas price that we consider as the one that corresponds to a cheap and fast execution. However, it is only a suggestion and should be used at users' sole discretion. All gas prices are in Gwei."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/txs/fee"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_estimate_gas_smart_contract_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint retuns the average gas price and gas limit set by the Ethereum Blockchain. At this point for all kinds of deployments the json result will be as follows:"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/contracts/gas"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_get_token_balance(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "In the request url you should provide the address you want to observe and the contract address that created the token. After sending the request you will receive a json object with the name of the token, the amount and its symbol."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/tokens/0x7857af2143cb06ddc1dab5d7844c9402e89717cb/0x40f9405587B284f737Ef5c4c2ecEA1Fa8bfAE014/balance"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_get_address_token_transfers(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "In the request url you should provide the address you want to observe. The response will be a json object with a list of all token transactions for the specified address (in DESC order)."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/tokens/address/0x2b5634c42055806a59e9107ed44d43c426e58258"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_list_of_forward_payments_by_users(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "If the request is successful, you’ll receive a JSON (see the response body) and an HTTP Status Code 200."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/payments"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_list_of_past_forward_payments_by_users(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "If the request is successful, you’ll receive a JSON (see the response body) and an HTTP Status Code 200."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/payments/history"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_list_webhook_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List WebHook Endpoint provides a list with the webhooks for a given user id."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/hooks"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_chain_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "General information about a blockchain is available by GET-ing the base resource"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/info"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_block_height_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Height endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/blocks/3816116"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_latest_block_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Latest Block Endpoint gives you detail information for the latest block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/blocks/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_address_info_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The default Address Endpoint strikes a balance between speed of response and data on Addresses. It returns information about the balance (in ETH) and transactions of a specified address."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/address/0x5b3457a50d39348ac15bef60e7f44a1941fe6502"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_transaction_by_address_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transactions By Address Endpoint returns all transactions specified by the query params: index and limit; The maxim value of limit is 50. The value in the returned transactions in WEI."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/address/0xc4618e88a2be9e6901019625ac5b627715d66422/transactions"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_nonce_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Nonce Endpoint returns the current nonce of the specified address."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/address/0xbB9d3A371b6e1dd468161C0DF12492867CC594dB/nonce"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_transaction_index_endpoint_by_block_number(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transaction Index Endpoint by Block Number returns detailed information about a given transaction based on its index and block height."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/txs/block/7178641/10"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_transaction_index_endpoint_by_block_hash(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transaction Index Endpoint by Block Hash returns detailed information about a given transaction based on its index and block hash."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/txs/block/0x359f5e1ca72207db464193ec14b7051413292e6156856a393897ccde7805bce9/10"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_pending_transactions_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Pending Transactions Endpoint makes a call to the EVM and returns all pending transactions. The response might be limited if you lack credits."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/txs/pending"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_queued_transactions_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Queued Transactions Endpoint makes a call to the EVM and returns all queued transactions. The response might be limited if you lack credits."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/txs/queued"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_get_token_balance(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "In the request url you should provide the address you want to observe and the contract address that created the token. After sending the request you will receive a json object with the name of the token, the amount and its symbol."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/tokens/0x7857af2143cb06ddc1dab5d7844c9402e89717cb/0x40f9405587B284f737Ef5c4c2ecEA1Fa8bfAE014/balance"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_get_address_token_transfers(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "In the request url you should provide the address you want to observe. The response will be a json object with a list of all token transactions for the specified address (in DESC order)."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/tokens/address/0x2b5634c42055806a59e9107ed44d43c426e58258"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_list_webhook_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "List WebHook Endpoint provides a list with the webhooks for a given user id."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/hooks"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_ropsten_chain_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "General information about a blockchain is available by GET-ing the base resource"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/ropsten/info"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_ropsten_block_height_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Hash endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/ropsten/blocks/0xf76556c7517446ecebb89747167125c823d68b617f3dabd02e646ea5dcb328b0"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_all_periods(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get full list of, supported by us, time periods available for requesting OHLCV data."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/ohlcv/periods"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ohlcv_latest_data(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get OHLCV latest time-series data for requested symbol and period, returned in time descending order."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/ohlcv/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ohlcv_historical_data(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get OHLCV time-series data for requested symbol and period, returned in time ascending order."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/ohlcv/history/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_all_exchanges(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a detailed list of all supported exchanges provided by our system."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/exchanges"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_exchange_details(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a detailed information for a single supported exchange provided by our system by ID."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/exchanges/5b4f16b96ab304001a484223"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_all_assets(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get detailed list of all associated assets."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/assets"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_all_symbols(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get detailed information for a specific asset."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/mappings"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_symbol_details(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get a detailed information for a specific symbol mapping."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/mappings/5bfc325c9c40a100014db8ff"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_current_rates(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get exchange rates between pair of requested assets pointing at a specific or current time."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/exchange-rates/USD"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_specific_rate_in_a_specific_exchange(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "URI not found. Check the documentation."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/exchange/5b1ea9d21090c200146f7362/USD/ETH"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_all_current_rates_in_a_specific_exchange(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Error 404."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/exchange-rates/exchange/5b1ea92e584bf50020130615"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def latest_data_by_exchange(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get latest trades from a specific exchange up to 1 hour ago. Latest data is always returned in time descending order."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/exchange/5b1ea9d21090c200146f7362/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def latest_data_by_assets_pair(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get latest trades from a specific assets pair (exp. BTC / USD) up to 1 hour ago. Latest data is always returned in time descending order."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/baseAsset/5b1ea92e584bf50020130612/quoteAsset/5b1ea92e584bf50020130615/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def latest_data_by_symbol(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get latest trades from a specific symbol up to 1 hour ago. Latest data is always returned in time descending order."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/5bfc329f9c40a100014dc5a7/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def historical_data_by_base_asset(timeend: str, timestart: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get history transactions from specific base asset, returned in time ascending order. If no start & end time is defined when calling the endpoint, your data results will be provided 24 hours back, by default."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/baseAsset/5b1ea92e584bf50020130612/history?"
    querystring = {'timeEnd': timeend, 'timeStart': timestart, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def historical_data_by_exchange_assets_pair(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Get history transactions from specific assets pair (exp. BTC/USD) in a specific exchange, returned in time ascending order. If no start & end time is defined when calling the endpoint, your data results will be provided 24 hours back, by default."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/trades/exchange/5b1ea9d21090c200146f7362/baseAsset/5b1ea92e584bf50020130612/quoteAsset/5b1ea92e584bf50020130615/history"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_block_hash_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Hash endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/blocks/00000000000000cf46a1522895ceb7e66a8f9b5430a97b39c36d912904d6a8b7"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_list_wallets_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " You can then query detailed information on individual wallets (via their names) by leveraging the Get Wallet Endpoint."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/wallets"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_testnet_transaction_txid_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transaction Txid Endpoint returns detailed information about a given transaction based on its id."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/testnet/txs/txid/00000000000000000008b7233b8abb1519d0a1bc6579e209955539c303f3e6b1"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_block_height_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Height endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/blocks/546903"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_get_hd_wallet_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a WHDWallet based on its WALLET_NAME."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/wallets/hd/wallet"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_list_wallets_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    " You can then query detailed information on individual wallets (via their names) by leveraging the Get Wallet Endpoint."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/wallets"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_get_wallet_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This endpoint returns a Wallet or HDWallet based on its WALLET_NAME."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/wallets/wallet_name"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_list_of_past_forward_payments_by_users(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "To list your currently active payment forwarding addresses, you can use this endpoint."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/payments/history"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_list_payments_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "To list your currently active payment forwarding addresses, you can use this endpoint."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/btc/mainnet/payments"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def bitcoin_mainnet_block_hash_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Hash endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/btc/mainnet/blocks/0000000000000000001ca87bd09c2fc80a0ef3966c6473553b118583e0a73381"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_transaction_index_endpoint_by_block_number(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Transaction Index Endpoint by Block Number returns detailed information about a given transaction based on its index and block height."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/txs/block/7178641/10"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_rinkeby_block_hash_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Hash endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/rinkeby/blocks/0x79230d974f6cea8c11cc2f3a58c2b811313af17a2f7391de6665502910d4d383"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_mainnet_nonce_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "The Nonce Endpoint returns the current nonce of the specified address."
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/mainnet/address/0xbB9d3A371b6e1dd468161C0DF12492867CC594dB/nonce"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_ropsten_latest_block_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Latest Block Endpoint gives you detail information for the latest block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/ropsten/blocks/latest"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def ethereum_ropsten_block_height_endpoint(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Block Height endpoint gives you detail information for particular block in the blockchain"
    
    """
    url = f"https://crypto-market-data-apis.p.rapidapi.com/bc/eth/ropsten/blocks/3816116"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "crypto-market-data-apis.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

