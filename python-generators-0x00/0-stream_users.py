#!/usr/bin/python3
import seed

def stream_users_in_batches(batch_size):
    """Generator that yields rows in batches"""
    conn = seed.connect_to_prodev()
    cursor = conn.cursor(dictionary=True)
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
    conn.close()
def batch_processing(batch_size):
    """Process users > 25 years using the above generator"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if int(user['age']) > 25:
                print(user)
