import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

import os
from dotenv import load_dotenv

load_dotenv()


# Folder utama project
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# Lokasi database
DATABASE_PATH = os.path.join(
    BASE_DIR,
    "data",
    "nutrition.db"
)


# API KEY
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
