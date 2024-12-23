from dotenv import load_dotenv, find_dotenv
import os

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")


TON_API_URL = os.getenv("TON_API_URL")
TON_API_KEY = os.getenv("TON_API_KEY")

JETTON_CONTRACT_ADDRESS = os.getenv("JETTON_CONTRACT_ADDRESS")
NFT_CONTRACT_ADDRESS = os.getenv("NFT_CONTRACT_ADDRESS")

