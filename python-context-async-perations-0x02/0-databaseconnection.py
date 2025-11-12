import sqlite3

class DatabaseConnection:
    def __init__(self, db_name="test.db"):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        # Open the database connection
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Commit if no exception, else rollback
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        # Close the connection
        self.conn.close()

