import requests

TON_API_URL = "https://testnet.toncenter.com/api/v2/jsonRPC"
TON_API_KEY = "ВАШ_API_КЛЮЧ"

def get_balance(wallet_address):
    headers = {
        "Authorization": f"Bearer {TON_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "id": "1",
        "jsonrpc": "2.0",
        "method": "getAddressBalance",
        "params": {
            "address": wallet_address
        }
    }
    response = requests.post(TON_API_URL, headers=headers, json=payload)
    return response.json()
