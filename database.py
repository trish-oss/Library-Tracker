import sqlite3
def connect():
    conn = sqlite3.connect("library.db")
    return conn
def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()
    database.create_table()