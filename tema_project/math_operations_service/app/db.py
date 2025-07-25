import psycopg2
from flask import g
import time
import os

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('POSTGRES_HOST'),
            port=os.getenv('POSTGRES_PORT')
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    for attempt in range(10):
        try:
            conn = psycopg2.connect(
                host='db',
                dbname='operations_db',
                user='postgres',
                password='postgres'
            )
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS operations (
                    id SERIAL PRIMARY KEY,
                    type TEXT NOT NULL,
                    operand_a REAL NOT NULL, 
                    operand_b REAL,
                    result REAL NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            conn.close()
            print("Database initialized.")
            break
        except psycopg2.OperationalError as e:
            print(f"Attempt {attempt + 1}/10: PostgreSQL not ready, retrying in 3 seconds...")
            time.sleep(3)
    else:
        raise Exception("Failed to connect to the database after multiple attempts.")
