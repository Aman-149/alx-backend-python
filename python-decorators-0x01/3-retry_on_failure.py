
#!/usr/bin/env python3
import sqlite3
import functools
import time
from datetime import datetime

def retry(attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Attempt {attempt}/{attempts}...")
                    return func(*args, **kwargs)
                except sqlite3.OperationalError as e:
                    print(f"[WARNING] Database error: {e}")
                    if attempt == attempts:
                        print("[ERROR] All retry attempts failed. Raising exception.")
                        raise
                    print(f"Retrying in {delay} seconds...\n")
                    time.sleep(delay)
        return wrapper
    return decorator

