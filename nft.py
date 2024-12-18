from typing import Dict

from config import NFT_CONTRACT_ADDRESS
from ton_integration import send_ton


# Mint an NFT using a metadata URL
def mint_nft(owner_address: str, metadata_url: str) -> Dict:
    response = send_ton(
        from_address=NFT_CONTRACT_ADDRESS,
        private_key="your_private_key",
        to_address=owner_address,
        amount=0  # Assuming no TON transfer is needed for minting
    )
    return response
