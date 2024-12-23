from typing import Dict

import requests

from config import NFT_CONTRACT_ADDRESS, TON_API_URL, TON_API_KEY
from ton_integration import send_ton


# Mint an NFT using a metadata URL
def mint_nft(owner_address: str, metadata_url: str) -> Dict:
    response = send_ton(
        wallet_address=owner_address,
        amount=0  # Assuming no TON transfer is needed for minting
    )
    return response

def mint_nft_via_contract(owner_address: str, metadata_url: str) -> Dict:
    response = requests.post(TON_API_URL, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "sendTransaction",
        "params": {
            "to": NFT_CONTRACT_ADDRESS,
            "amount": 0,
            "data": {
                "owner_address": owner_address,
                "metadata_url": metadata_url
            }
        }
    }, headers={"Authorization": f"Bearer {TON_API_KEY}"})
    response.raise_for_status()
    return response.json()
