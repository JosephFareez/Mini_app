const tg = window.Telegram.WebApp;
tg.expand();

const walletInfoDiv = document.getElementById("wallet-info");
const tasksDiv = document.getElementById("tasks");
const airdropStatusDiv = document.getElementById("airdrop-status");

document.getElementById("connect-wallet").addEventListener("click", async () => {
    const result = await fetch("/connect-wallet");
    const walletData = await result.json();
    document.getElementById("wallet-info").innerHTML = `
        <p>Wallet: ${walletData.address}</p>
        <p>Balance: ${walletData.balance} TON</p>
    `;
});

document.getElementById("add-points").addEventListener("click", async () => {
    const result = await fetch("/add-points", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ user_id: 12345, points: 10 })
    });
    const data = await result.json();
    alert(`New points balance: ${data.new_balance}`);
});

document.getElementById("airdrop").addEventListener("click", async () => {
    const result = await fetch("/airdrop", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            user_id: 12345,
            conversion_rate: 0.01,
            wallet_address: "ton://test_wallet"
        })
    });
    const data = await result.json();
    document.getElementById("airdrop-status").innerHTML = `<p>${data.message} - ${data.tokens} tokens sent.</p>`;
});
