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
