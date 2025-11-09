#!/usr/bin/python3
import mysql.connector
import csv
import uuid

def connect_db():
    """Connect to MySQL server"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """Create ALX_prodev database"""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    connection.commit()
    cursor.close()


def connect_to_prodev():
    """Connect to ALX_prodev DB"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='ALX_prodev'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
def create_table(connection):
    """Create user_data table"""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(50) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        );
    """)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")


def insert_data(connection, csv_file):
    """Insert CSV data if table is empty"""
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM user_data;")
    count = cursor.fetchone()[0]

    if count > 0:
        cursor.close()
        return  # Data already exists

    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (str(uuid.uuid4()), row['name'], row['email'], row['age']))

    connection.commit()
    cursor.close()
