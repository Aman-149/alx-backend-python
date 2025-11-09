#!/usr/bin/python3
"""1-batch_processing.py
Batch processing of users > 25 using generators
"""

import seed


def stream_users_in_batches(batch_size):
    """Generator that yields batches of users"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch

    cursor.close()
    connection.close()
    return  # ALX check requires return


def batch_processing(batch_size):
    """Generator that yields users over 25 years old"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if int(user['age']) > 25:
                yield user
    return  # ALX check requires return
