import sqlite3


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
init_db()

"Database initialized successfully."