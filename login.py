from dataclasses import dataclass
import sqlite3


@dataclass
class User:
    id: int
    name: str
    password: str
    points: int


def vulnerable(username: str, password: str) -> User | None:
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "';"
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()
    if result:
        return User(*result)
    return None


def secure(username: str, password: str) -> User | None:
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username=? AND password=?;"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    connection.close()
    if result:
        return User(*result)
    return None
