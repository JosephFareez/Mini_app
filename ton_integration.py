from typing import Optional, Dict

import requests

from config import TON_API_URL, TON_API_KEY


# Get wallet balance from TON blockchain
def get_wallet_balance(address: str) -> Optional[float]:
    payload: Dict = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAddressInformation",
        "params": {"address": address},
    }
    headers: Dict = {"X-API-KEY": TON_API_KEY}
    response = requests.post(TON_API_URL, json=payload, headers=headers)
    data = response.json()
    if "result" in data:
        return float(data["result"]["balance"]) / 10 ** 9  # Convert to TON
    return None


# Send TON from one wallet to another
def send_ton(from_address: str, private_key: str, to_address: str, amount: float) -> Dict:
    payload: Dict = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "sendTransaction",
        "params": {
            "from": from_address,
            "to": to_address,
            "amount": int(amount * 10 ** 9),  # Convert to smallest unit
            "key": private_key
        }
    }
    headers: Dict = {"X-API-KEY": TON_API_KEY}
    response = requests.post(TON_API_URL, json=payload, headers=headers)
    return response.json()
