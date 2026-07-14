import sqlite3


DATABASE_NAME = "nutrition.db"


def get_connection():
    conn = sqlite3.connect(
        DATABASE_NAME,
        check_same_thread=False
    )

    return conn



def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        food TEXT,
        calories REAL,
        protein REAL,
        carbs REAL,
        fat REAL
    )
    """)

    conn.commit()
    conn.close()