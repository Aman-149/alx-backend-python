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
