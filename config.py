from dotenv import load_dotenv, find_dotenv
import os

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("your_api_id")
API_HASH = os.getenv("your_api_hash")


TON_API_URL = os.getenv("https://toncenter.com/api/v2/jsonRPC")
TON_API_KEY = os.getenv("your_ton_api_key")

JETTON_CONTRACT_ADDRESS = os.getenv("your_jetton_contract_address")
NFT_CONTRACT_ADDRESS = os.getenv("your_nft_contract_address")

