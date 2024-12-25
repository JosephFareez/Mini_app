import requests

from config import TON_API_KEY, TON_API_URL

if not TON_API_KEY:
	raise ValueError("TON_API_KEY не задан. Проверьте переменные окружения или файл config.py.")

if not TON_API_URL:
	raise ValueError("TON_API_URL не задан. Проверьте переменные окружения или файл config.py.")


# Получение баланса кошелька
import requests

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
		response.raise_for_status()  # Ensures that any status code other than 2xx raises an exception
		data = response.json()

		# Log the full response to see the structure
		print("API Response:", data)

		if "result" in data:
			balance = data["result"].get("balance", 0)  # Default to 0 if "balance" isn't present
			print(f"Balance (nanotons): {balance}")
			return balance / 1e9  # Convert nanotons to TON
		else:
			print(f"Ошибка в ответе API: {data}")
			return 0  # Return 0 if there's no "result" field
	except requests.exceptions.RequestException as e:
		print(f"Ошибка при запросе баланса: {e}")
		return "Ошибка запроса"  # Return a string error message


# Отправка токенов (TON)
def send_ton(to_address, amount):
	print(f"Отправка {amount} TON на адрес {to_address}")
	headers = {
		"Authorization": f"Bearer {TON_API_KEY}",
		"Content-Type": "application/json"
	}
	payload = {
		"jsonrpc": "2.0",
		"id": 1,
		"method": "sendTransaction",
		"params": {
			"to": to_address,
			"amount": amount
		}
	}
	try:
		response = requests.post(TON_API_URL, headers=headers, json=payload)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.RequestException as e:
		print(f"Ошибка при отправке TON: {e}")
		return {"error": str(e)}


# Минтинг токенов (NFT)
def mint_token(wallet_address, metadata_url):
	print(f"Минтинг токена для {wallet_address} с метаданными {metadata_url}")
	headers = {
		"Authorization": f"Bearer {TON_API_KEY}",
		"Content-Type": "application/json"
	}
	payload = {
		"jsonrpc": "2.0",
		"id": 1,
		"method": "mintNFT",
		"params": {
			"to": wallet_address,
			"metadata": metadata_url
		}
	}
	try:
		response = requests.post(TON_API_URL, headers=headers, json=payload)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.RequestException as e:
		print(f"Ошибка при минтинге токена: {e}")
		return {"error": str(e)}


# Тестовые вызовы
if __name__ == "__main__":
	wallet_address = "ton://test_wallet_address"
	metadata_url = "https://example.com/metadata.json"

	# Получение баланса
	balance = get_wallet_balance(wallet_address)
	print(f"Баланс: {balance}")

	# Отправка TON
	send_result = send_ton(wallet_address, 10)
	print(f"Результат отправки: {send_result}")

	# Минтинг токена
	mint_result = mint_token(wallet_address, metadata_url)
	print(f"Результат минтинга: {mint_result}")
