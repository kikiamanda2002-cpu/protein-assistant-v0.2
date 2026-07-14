from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from app.config import TELEGRAM_TOKEN
from app.database.connection import create_tables
from app.handlers.food_handler import handle_food



async def start(update, context):
    await update.message.reply_text(
        """
👋 Selamat datang di Protein Assistant!

Kirim nama makanan kamu.

Contoh:
Ayam bakar nasi
"""
    )



def main():

    print("🚀 Protein Assistant Starting")

    # Membuat tabel database
    create_tables()

    print("✅ Database berhasil dibuat")


    # Membuat aplikasi Telegram
    app = Application.builder().token(
        TELEGRAM_TOKEN
    ).build()


    # Command /start
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    # Pesan makanan
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_food
        )
    )


    print("🤖 Bot Telegram berjalan...")


    app.run_polling()



if __name__ == "__main__":
    main()