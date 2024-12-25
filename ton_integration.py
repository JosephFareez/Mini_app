import requests

from config import TON_API_URL, TON_API_KEY


import requests

def get_wallet_balance(wallet_address):
    print(f"Запрос баланса для кошелька {wallet_address}")
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
    try:
        response = requests.post(TON_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if "result" in data:
            return data["result"]
        else:
            print(f"Ошибка в ответе API: {data}")
            return "0"
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе баланса: {e}")
        return "Ошибка запроса"



def send_ton(to_address, amount):
    response = requests.post(
        TON_API_URL,
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": "sendTransaction",
            "params": {
                "to": to_address,
                "amount": amount
            }
        },
        headers={"Authorization": f"Bearer {TON_API_KEY}"}
    )
    response.raise_for_status()
    return response.json()


def mint_token(wallet_address, metadata_url):
    # Запрос к смарт-контракту для минтинга NFT
    response = requests.post(
        TON_API_URL,
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": "mintNFT",
            "params": {
                "to": wallet_address,
                "metadata": metadata_url
            }
        },
        headers={"Authorization": f"Bearer {TON_API_KEY}"}
    )
    response.raise_for_status()
    return response.json()
