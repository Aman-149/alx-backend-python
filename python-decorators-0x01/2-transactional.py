#!/usr/bin/env python3
import sqlite3
import functools
from datetime import datetime
def transaction(func):
    """Decorator that manages database transactions (commit/rollback)."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = kwargs.get("conn") or (args[0] if args else None)

        if not isinstance(conn, sqlite3.Connection):
            raise ValueError("A sqlite3 connection must be passed as the first argument or 'conn' keyword.")

        try:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Transaction started.")
            result = func(*args, **kwargs)
            conn.commit()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Transaction committed.")
            return result
        except Exception as e:
            conn.rollback()
            print(f"[ERROR] Transaction rolled back due to: {e}")
            raise
    return wrapper
@transaction
def add_user(conn, name):
    """Insert a new user into the database."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name) VALUES (?);", (name,))
    return cursor.lastrowid


if __name__ == "__main__":]
    conn = sqlite3.connect("users.db")

    try:
        user_id = add_user(conn, "Amanuel")
        print("Inserted user ID:", user_id)
    finally:
        conn.close()
