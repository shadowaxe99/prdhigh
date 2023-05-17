```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a memory-based SQLite database
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def manage_database():
    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        create_table(conn, UserSchema)
        create_table(conn, TaskSchema)
        create_table(conn, FeedbackSchema)
    else:
        print("Error! cannot create the database connection.")

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

UserSchema = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """

TaskSchema = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    task_type text NOT NULL,
                                    task_status text NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""

FeedbackSchema = """CREATE TABLE IF NOT EXISTS feedback (
                                    id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    feedback text NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""

if __name__ == '__main__':
    manage_database()
```