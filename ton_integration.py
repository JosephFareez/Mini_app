import requests

from config import TON_API_URL, TON_API_KEY


def get_wallet_balance(wallet_address):
    response = requests.post(TON_API_URL, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAddressBalance",
        "params": {"address": wallet_address}
    }, headers={"Authorization": f"Bearer {TON_API_KEY}"})
    response.raise_for_status()
    return response.json().get("result", 0)


def send_ton(wallet_address, amount):
    response = requests.post(TON_API_URL, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "sendTransaction",
        "params": {
            "to": wallet_address,
            "amount": amount
        }
    }, headers={"Authorization": f"Bearer {TON_API_KEY}"})
    response.raise_for_status()
    return response.json()

