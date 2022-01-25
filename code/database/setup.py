# Database Setup

from .config import DATABASE, HOST, USER, PASSWORD
from .connect import connect


def setup():
    connection = connect()
    cursor = connection.cursor()

    # Check if users table exists
    command = f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{DATABASE}' AND TABLE_NAME = 'users' LIMIT 1"
    cursor.execute(command)
    results = cursor.fetchone()
    if results[0] != 1:
        # Table doesn't exist, create it
        command = f"CREATE TABLE users (id INT NOT NULL AUTO_INCREMENT, username VARCHAR(20) NOT NULL UNIQUE, password TEXT NOT NULL, PRIMARY KEY (id))"
        cursor.execute(command)
        connection.commit()
    
    # Check if games table exists
    command = f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{DATABASE}' AND TABLE_NAME = 'games' LIMIT 1"
    cursor.execute(command)
    results = cursor.fetchone()
    if results[0] != 1:
        # Table doesn't exist, create one
        command = f"CREATE TABLE games (id INT NOT NULL AUTO_INCREMENT, status VARCHAR(10), user1 VARCHAR(20), user2 VARCHAR(20) DEFAULT '', moves TEXT, result VARCHAR(20) DEFAULT '', PRIMARY KEY (id))"
        cursor.execute(command)
        connection.commit()
