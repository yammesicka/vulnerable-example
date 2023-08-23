import sqlite3


def add(user_id: int) -> None:
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET points = points + 1 WHERE id = ?;", (user_id,))
    connection.commit()
    connection.close()
