# TON MiniApp Project

This project is a Telegram MiniApp that integrates with the TON blockchain to provide features such as wallet management, token issuance (Jettons), and NFT creation. It supports TON-compatible wallets, including the Telegram Wallet, and can be extended to integrate with platforms like OKX.

---

## Features

- **TON Wallet Integration**: Connect and manage TON-compatible wallets.
- **Token Management**: Issue and interact with TON Jettons.
- **NFT Creation**: Mint and manage NFTs using the TIP-4 standard.
- **Database**: Store user and transaction data with SQLite.
- **Extendability**: Built with modular components to allow for future integrations.

---

## Project Structure

```
ton_mini_app/
├── bot.py              # Main Telegram bot logic
├── config.py           # Configuration and API keys
├── ton_integration.py  # TON API interaction
├── jetton.py           # Token (Jetton) management
├── nft.py              # NFT creation and management
├── requirements.txt    # Dependencies
├── database.py         # Database initialization and queries
└── README.md           # Project documentation
```

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- Access to the Telegram Bot API
- TON API Key from [TON Center](https://toncenter.com/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Joseph861020/Mini_app.git
   cd ton-mini-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the project:
   - Rename `.env_example` to `.env`.
   - Add your API keys and contract addresses to `.env`.

4. Initialize the database:
   ```bash
   python -c "import database; database.init_db()"
   ```

5. Run the bot:
   ```bash
   python bot.py
   ```

---

## Usage

### Telegram Commands

- `/start`: Register and connect your TON wallet.
- `/balance`: Check your TON wallet balance.
- `/mint_jetton`: Issue Jettons to a connected wallet.
- `/mint_nft`: Mint a new NFT using metadata.

### TON Wallet Integration
The bot uses deep links (`ton://`) to interact with TON wallets such as the Telegram Wallet and Tonkeeper.

---

## Key Components

### `config.py`
Loads API keys and contract addresses from the `.env` file:
```python
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TON_API_URL = os.getenv("TON_API_URL")
TON_API_KEY = os.getenv("TON_API_KEY")
JETTON_CONTRACT_ADDRESS = os.getenv("JETTON_CONTRACT_ADDRESS")
NFT_CONTRACT_ADDRESS = os.getenv("NFT_CONTRACT_ADDRESS")
```

### `ton_integration.py`
Handles communication with the TON blockchain:
- **`get_wallet_balance`**: Fetches the balance of a given wallet address.
- **`send_ton`**: Sends TON tokens to a specified address.

### `jetton.py`
Manages token issuance and transfers:
- **`mint_jetton`**: Issues Jettons to a user’s wallet.

### `nft.py`
Facilitates NFT creation:
- **`mint_nft`**: Mints NFTs with metadata hosted on IPFS.

### `database.py`
Handles SQLite database operations:
- **`init_db`**: Initializes the database schema.
- **`add_user`**: Registers a new user with wallet details.

---

## Extending the Project

### Additional Wallets
Integrate other TON-compatible wallets such as Tonkeeper or MyTonWallet using their APIs or deep link protocols.

### NFT Marketplace
Build an NFT marketplace on top of this platform to allow users to trade their minted NFTs.

### Security Enhancements
- Use encrypted storage for private keys.
- Implement OAuth2 for user authentication.

---

## Dependencies

- `telethon`: For Telegram bot interaction.
- `requests`: For API communication.
- `sqlite3`: For database management.
- `python-dotenv`: For environment variable management.

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contribution
Contributions are welcome! Fork the repository and submit a pull request with your changes.

