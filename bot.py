from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Импорт функций для работы с TON
from ton_integration import get_wallet_balance, mint_token


@app.route("/")
def index():
	wallet_address = "ton://test_wallet_address"  # Пример адреса
	balance = get_wallet_balance(wallet_address)
	points = 100  # Пример количества баллов
	return render_template("index.html", wallet_address=wallet_address, balance=balance, points=points)


@app.route("/add-points", methods=["POST"])
def add_points():
	user_id = request.form.get("user_id")
	points = request.form.get("points")
	# Здесь можно обновить баллы пользователя в базе данных
	return f"Баллы {points} добавлены для пользователя {user_id}!"


@app.route("/airdrop", methods=["POST"])
def airdrop():
	user_id = request.form.get("user_id")
	conversion_rate = request.form.get("conversion_rate")
	wallet_address = request.form.get("wallet_address")
	# Здесь можно реализовать логику airdrop
	return f"Airdrop отправлен на адрес {wallet_address} по курсу {conversion_rate}!"


@app.route("/mint-token", methods=["POST"])
def mint_nft():
	wallet_address = request.form.get("wallet_address")
	metadata_url = request.form.get("metadata_url")
	try:
		result = mint_token(wallet_address, metadata_url)
		return jsonify(result)
	except Exception as e:
		return f"Ошибка при минтинге NFT: {e}", 500


@app.route("/tasks")
def tasks():
	return render_template("tasks.html")
