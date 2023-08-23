import sqlite3


def vulnerable(limit: int = 10) -> list[tuple[str, int]]:
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT username, points FROM users ORDER BY points DESC LIMIT {limit};")
        leaderboard = cursor.fetchall()
    except Exception:
        return []
    else:
        return leaderboard
    finally:
        connection.close()


def secure(limit: int = 10) -> list[tuple[str, int]]:
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT username, points FROM users ORDER BY points DESC LIMIT ?;", (limit,))
    leaderboard = cursor.fetchall()
    connection.close()
    return leaderboard
