import sqlite3


def user(username: str, password: str) -> bool:
    try:
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?);", (username, password))
        connection.commit()
        connection.close()
        return True
    except sqlite3.IntegrityError:
        return False
