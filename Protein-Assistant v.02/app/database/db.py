import sqlite3


DATABASE_NAME = "nutrition.db"


def connect_db():
    return sqlite3.connect(DATABASE_NAME)


def create_table():

    conn = connect_db()
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



def save_meal(data):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO meals
    (date, food, calories, protein, carbs, fat)

    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        data["date"],
        data["food"],
        data["calories"],
        data["protein"],
        data["carbs"],
        data["fat"]
    ))

    conn.commit()
    conn.close()