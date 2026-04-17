import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "30012008d",   # ⚠️ временно простой пароль
    "port": 5432
}

def connect():
    return psycopg2.connect(**DB_CONFIG)
