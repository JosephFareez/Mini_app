import sqlite3

users = {}  # Пример базы данных в памяти
tasks = {"123": {"description": "Подписка на канал", "completed": False}}


def get_user_points(user_id):
	return users.get(user_id, 0)


def add_user_points(user_id, points):
	users[user_id] = users.get(user_id, 0) + points
	return users[user_id]


def verify_task(user_id, task_id):
	if tasks.get(task_id) and not tasks[task_id]["completed"]:
		tasks[task_id]["completed"] = True
		add_user_points(user_id, 10)  # Пример награды
		return True
	return False


def init_db() -> None:
	conn = sqlite3.connect("data.db")
	cursor = conn.cursor()
	cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            wallet_address TEXT
        )
    """)
	cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            amount REAL,
            status TEXT
        )
    """)
	conn.commit()
	conn.close()


def add_user(user_id: int, username: str, wallet_address: str) -> None:
	conn = sqlite3.connect("data.db")
	cursor = conn.cursor()
	cursor.execute("INSERT INTO users (id, username, wallet_address) VALUES (?, ?, ?)",
	               (user_id, username, wallet_address))
	conn.commit()
	conn.close()
