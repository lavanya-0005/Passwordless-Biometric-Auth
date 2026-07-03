import sqlite3
import os

DB_PATH = "database/users.db"

os.makedirs("database", exist_ok=True)


def create_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            voice_features TEXT,
            face_encoding TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            method TEXT,
            status TEXT,
            login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()