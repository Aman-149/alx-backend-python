import sqlite3

class ExecuteQuery:
    def __init__(self, db_name="users.db", query=None, params=()):
        self.db_name = db_name
        self.query = query
        self.params = params

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self

    def execute(self):
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()


# Example usage
if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)
    
    with ExecuteQuery(query=query, params=params) as executor:
        results = executor.execute()
        print(results)
