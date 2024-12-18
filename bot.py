from typing import Optional

from telethon import TelegramClient, events

from config import API_ID, API_HASH, BOT_TOKEN
from database import init_db, add_user
from jetton import mint_jetton
from nft import mint_nft
from ton_integration import get_wallet_balance

# Initialize the Telegram bot
bot = TelegramClient("ton_bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)


# Command: /start
@bot.on(events.NewMessage(pattern="/start"))
async def start(event) -> None:
    user_id: int = event.sender_id
    username: str = event.sender.username or "Anonymous"
    wallet_address: str = "ton://connect"  # Placeholder for wallet integration
    add_user(user_id, username, wallet_address)
    await event.respond(f"Welcome, {username}! Your TON wallet address: {wallet_address}")


# Command: /balance
@bot.on(events.NewMessage(pattern="/balance"))
async def balance(event) -> None:
    wallet_address: str = "your_wallet_address"  # Fetch from the database
    balance: Optional[float] = get_wallet_balance(wallet_address)
    if balance is not None:
        await event.respond(f"Your wallet balance: {balance} TON")
    else:
        await event.respond("Could not fetch wallet balance.")


# Command: /mint_jetton
@bot.on(events.NewMessage(pattern="/mint_jetton"))
async def mint_jetton_command(event) -> None:
    amount: float = 100  # Example: mint 100 Jettons
    result = mint_jetton("user_wallet_address", amount)
    await event.respond(f"Jettons minted successfully: {result}")


# Command: /mint_nft
@bot.on(events.NewMessage(pattern="/mint_nft"))
async def mint_nft_command(event) -> None:
    metadata_url: str = "ipfs://your_metadata_hash"
    result = mint_nft("user_wallet_address", metadata_url)
    await event.respond(f"NFT created successfully: {result}")


# Run the bot
if __name__ == "__main__":
    init_db()
    bot.run_until_disconnected()
