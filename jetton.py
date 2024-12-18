from typing import Dict

from config import JETTON_CONTRACT_ADDRESS
from ton_integration import send_ton


# Mint Jettons to a wallet
def mint_jetton(owner_address: str, amount: float) -> Dict:
    response = send_ton(
        from_address=JETTON_CONTRACT_ADDRESS,
        private_key="your_private_key",
        to_address=owner_address,
        amount=amount
    )
    return response
