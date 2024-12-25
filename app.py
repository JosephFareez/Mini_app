import requests
from flask import Flask, flash, jsonify, redirect, render_template, request, url_for

from config import TON_API_KEY, TON_API_URL
from database import add_user_points, get_user_points, verify_task
from ton_integration import get_wallet_balance, mint_token, send_ton

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Для flash-сообщений


# Главная страница
@app.route("/")
def index():
	wallet_address = "ton://test_wallet_address"  # Мок-адрес кошелька
	balance = get_wallet_balance(wallet_address)
	points = get_user_points("12345")  # Пример ID пользователя
	return render_template("index.html", wallet_address=wallet_address, balance=balance, points=points)


# Добавление баллов
@app.route("/add-points", methods=["POST"])
def add_points():
	user_id = request.form.get("user_id")
	points = int(request.form.get("points", 0))
	new_balance = add_user_points(user_id, points)
	flash(f"Баллы успешно добавлены. Новый баланс: {new_balance}.", "success")
	return redirect(url_for("index"))


# Проверка выполнения заданий
@app.route("/verify-task", methods=["POST"])
def verify_task_route():
	task_id = request.form.get("task_id")
	user_id = request.form.get("user_id")
	if verify_task(user_id, task_id):
		flash("Задание выполнено! Баллы начислены.", "success")
	else:
		flash("Задание не выполнено.", "error")
	return redirect(url_for("index"))


# Airdrop токенов
@app.route("/airdrop", methods=["POST"])
def airdrop():
	user_id = request.form.get("user_id")
	conversion_rate = float(request.form.get("conversion_rate", 0.01))
	wallet_address = request.form.get("wallet_address")

	points = get_user_points(user_id)
	tokens = points * conversion_rate
	result = send_ton(wallet_address, tokens)
	return render_template("result.html", message="Airdrop успешен", tokens=tokens, result=result)


@app.route("/tasks")
def tasks():
	task_list = [
		{"description": "Подписка на Telegram-канал", "status": "Completed"},
		{"description": "Подписка на Twitter", "status": "Pending"},
		{"description": "Публикация сторис", "status": "Pending"},
	]
	return render_template("tasks.html", tasks=task_list)


@app.route("/mint-token", methods=["POST"])
def mint_token_route():
	user_id = request.form.get("user_id")
	metadata_url = request.form.get("metadata_url")
	wallet_address = request.form.get("wallet_address")

	result = mint_token(wallet_address, metadata_url)
	flash("NFT успешно создан!", "success")
	return redirect(url_for("index"))


@app.route("/mint-nft", methods=["GET", "POST"])
def mint_nft():
	if request.method == "POST":
		# Получение данных из формы
		ton_address = request.form.get("ton_address")
		metadata_url = request.form.get("metadata_url")

		# Проверка ввода
		if not ton_address or not metadata_url:
			return "TON-адрес и Metadata URL обязательны", 400

		# Вызов функции минтинга
		try:
			result = mint_token(ton_address, metadata_url)
			return jsonify(result)  # Возвращает JSON-ответ с результатом минтинга
		except Exception as e:
			return f"Ошибка при минтинге NFT: {str(e)}", 500
	else:
		# Если запрос GET, показываем форму
		return render_template("mint_form.html")  # Здесь "mint_form.html" должен содержать форму выше

@app.route('/check-balance/<wallet_address>')
def check_balance(wallet_address):
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
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=80)
