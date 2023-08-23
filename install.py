import sqlite3


def database():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        points INTEGER DEFAULT 0
    );
    ''')

    users = [
        ('admin', 'admin123'),
        ('john', 'password123'),
        ('alice', 'securepass'),
    ]

    cursor.executemany('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?);', users)

    connection.commit()
    connection.close()

    print("Database setup completed with", len(users), "users.")


if __name__ == '__main__':
    database()
