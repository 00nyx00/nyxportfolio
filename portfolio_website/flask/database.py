import sqlite3
from itertools import groupby
from datetime import datetime

class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        # Establishes a connection to the SQLite database
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Sets the row_factory to retrieve rows as dictionaries
        return conn

    def get_comments(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Executes a SELECT query to retrieve all rows from the "comments" table
            cursor.execute("SELECT name, comment, timestamp FROM comments ORDER BY id DESC")
            return cursor.fetchall()  # Returns all fetched rows as a list of dictionaries

    def add_comments(self, name, comment):
        with self.get_connection() as conn:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Executes an INSERT query to add a new name to the "comments" table
            conn.execute("INSERT INTO comments (name, comment, timestamp) VALUES (?, ?, ?)", (name, comment, timestamp))
