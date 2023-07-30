```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a memory database for demo purposes
        print(f'successful SQLite connection with id {id(conn)}')
    except Error as e:
        print(e)
    return conn

def manage_database():
    connection = create_connection()
    if connection is not None:
        user_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """
        task_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    task_type text NOT NULL,
                                    task_status text NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""
        feedback_table = """CREATE TABLE IF NOT EXISTS feedback (
                                    id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    task_id integer NOT NULL,
                                    feedback text NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id),
                                    FOREIGN KEY (task_id) REFERENCES tasks (id)
                                );"""
        try:
            cursor = connection.cursor()
            cursor.execute(user_table)
            cursor.execute(task_table)
            cursor.execute(feedback_table)
            print("Tables created successfully")
        except Error as e:
            print(e)
    else:
        print("Error! cannot create the database connection.")

manage_database()
```