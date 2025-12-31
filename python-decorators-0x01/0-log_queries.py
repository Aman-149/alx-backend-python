#!/usr/bin/env python3
import sqlite3
import functools
from datetime import datetime
def log_queries(func):
    """Decorator that logs SQL queries executed by the decorated function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query argument if provided
        query = kwargs.get("query") or (args[0] if args else None)
        if query:
            print(f"[LOG] Executing SQL Query: {query}")
        else:
            print("[LOG] No SQL query found to execute.")
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    """Fetch all users from the database."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Example run (will log the query before executing)
if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users;")
    print(users)

