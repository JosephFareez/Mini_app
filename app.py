from flask import Flask, render_template, jsonify, request
from database import get_user_points, add_user_points
from ton_integration import send_ton, get_wallet_balance

app = Flask(__name__, static_folder="static", static_url_path="/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/connect-wallet")
def connect_wallet():
    try:
        wallet_address = "ton://test_wallet_address"
        balance = get_wallet_balance(wallet_address)
        return jsonify({"address": wallet_address, "balance": balance})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/tasks")
def tasks():
    user_id = request.args.get("user_id", 0)
    points = get_user_points(user_id)
    return jsonify({"points": points, "tasks": [
        {"description": "Subscribe to the Telegram channel", "status": "Completed"},
        {"description": "Follow on Twitter", "status": "Pending"}
    ]})

@app.route("/add-points", methods=["POST"])
def add_points():
    user_id = request.json.get("user_id")
    points = request.json.get("points", 0)
    print(f"Adding {points} points to user {user_id}")  # Log for debugging
    new_total = add_user_points(user_id, points)
    return jsonify({"new_balance": new_total})

@app.route("/airdrop", methods=["POST"])
def airdrop():
    user_id = request.json.get("user_id")
    conversion_rate = request.json.get("conversion_rate", 0.01)
    wallet_address = request.json.get("wallet_address")

    print(f"User {user_id} requesting airdrop of {conversion_rate} tokens to {wallet_address}")  # Log for debugging
    points = get_user_points(user_id)
    tokens = points * conversion_rate
    result = send_ton(wallet_address, tokens)

    return jsonify({"message": "Airdrop successful", "tokens": tokens, "result": result})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
