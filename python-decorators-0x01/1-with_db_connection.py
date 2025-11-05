
#!/usr/bin/env python3
import sqlite3
import functools
from datetime import datetime

def with_connection(func):
    """Decorator that automatically manages database connection and cursor."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Database connection opened.")
            
            # Pass the cursor into the decorated function
            result = func(cursor, *args, **kwargs)
            
            conn.commit()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Transaction committed.")
            return result
        except Exception as e:
            if conn:
                conn.rollback()
                print(f"[ERROR] Transaction rolled back due to: {e}")
            raise
        finally:
            if conn:
                conn.close()
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Database connection closed.")
    return wrapper


@with_connection
def fetch_all_users(cursor):
    """Fetch all users using an auto-managed database connection."""
    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()


if __name__ == "__main__":
    users = fetch_all_users()
    print(users)
