from app.database.db import create_table, save_meal
from datetime import datetime


create_table()


meal = {
    "date": str(datetime.now()),
    "food": "Ayam Bakar + Nasi",
    "calories": 450,
    "protein": 35,
    "carbs": 50,
    "fat": 12
}


save_meal(meal)


print("Data berhasil disimpan!")