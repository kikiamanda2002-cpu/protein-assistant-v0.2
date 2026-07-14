from datetime import datetime

from app.ai.nutrition_ai import analyze_food
from app.database.db import save_meal


async def handle_food(update, context):

    food_name = update.message.text

    # Analisa makanan sementara
    nutrition = analyze_food(food_name)

    # Tambahkan tanggal
    nutrition["date"] = str(datetime.now())

    # Simpan database
    save_meal(nutrition)

    message = f"""
🍽️ Analisa Makanan

Makanan:
{nutrition['food']}

🔥 Kalori:
{nutrition['calories']} kcal

💪 Protein:
{nutrition['protein']} gram

🍚 Karbohidrat:
{nutrition['carbs']} gram

🥑 Lemak:
{nutrition['fat']} gram

✅ Data sudah disimpan
"""

    await update.message.reply_text(message)