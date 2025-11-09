#!/usr/bin/python3
"""0-stream_users.py
Generator that streams rows from the user_data table
"""

import seed


def stream_users():
    """Yields one user at a time from the user_data table"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()
