#!/usr/bin/env python3
import sqlite3
import functools
from datetime import datetime

def cache_results(func):
    """
    Decorator that caches results of database queries
    based on the query string and parameters.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Use the query as the cache key
        query = kwargs.get("query") or (args[1] if len(args) > 1 else None)

        if query is None:
            raise ValueError("A SQL query must be provided for caching.")

        key = query.strip()

        # Check if result is cached
        if key in cache:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Returning cached result for query: {query}")
            return cache[key]

        # Execute the actual function
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Caching new result for query: {query}")
        result = func(*args, **kwargs)

        # Store in cache
        cache[key] = result
        return result

    return wrapper
@cache_results
def fetch_users(conn, query):
    """Fetch users with caching enabled."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    conn = sqlite3.connect("users.db")

    q = "SELECT * FROM users;"

    # First call — hits database
    users1 = fetch_users(conn, query=q)
    print(users1)

    # Second call — returns cached data
    users2 = fetch_users(conn, query=q)
    print(users2)

    conn.close()

