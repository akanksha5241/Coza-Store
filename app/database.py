import sqlite3
import os

def get_db_connection():
    db_path = "users.db"
    print("📂 Connecting to DB at:", os.path.abspath(db_path))
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def create_user_table():
    conn = get_db_connection()
    print("🛠️ Creating users table if not exists...")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_contacts_table():
    conn = get_db_connection()
    print("🛠️ Creating contacts table if not exists...")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_user_table()
    create_contacts_table()
