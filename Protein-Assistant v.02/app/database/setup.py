from app.database.connection import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id TEXT UNIQUE,
        name TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        food TEXT,
        calories REAL,
        protein REAL,
        carbs REAL,
        fat REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        time TEXT,
        active INTEGER DEFAULT 1
    )
    """)


    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database berhasil dibuat")