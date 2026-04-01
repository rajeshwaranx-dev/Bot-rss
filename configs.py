import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

# Telegram
API_ID = int(os.getenv("API_ID", "36633051"))
API_HASH = os.getenv("API_HASH", "ba52b4e3afcebd6f82696308ac5afc42")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7577907574:AAEQpYVEssCUbm8YMXARQFte4NOCr0oLWwA")  # Get from @BotFather

# Web
PORT = int(os.getenv("PORT", "8080"))
URL = os.getenv("URL", "")  # Your VPS IP or Koyeb/Render URL

# MongoDB
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://thanos:thanos2@cluster0.6u52un7.mongodb.net/?appName=Cluster0")
DATABASE_NAME = os.getenv("DATABASE_NAME", "thanos")

# TamilMV settings
TMV_URL = os.getenv("TMV_URL", "https://www.1tamilmv.immo/")
TMV_TORRENT = int(os.getenv("TMV_TORRENT", "-1003800286118"))
TMV_LEECH_GRP = int(os.getenv("TMV_LEECH_GRP", "-1002007085025"))
TMV_MIRROR_GRP = int(os.getenv("TMV_MIRROR_GRP", "0"))
TMV_TORRENT_THUMB = os.getenv("TMV_TORRENT_THUMB", "https://i.ibb.co/7dq7mMLp/photo-2025-10-18-16-42-28-7562603128038621216.jpg")
BOT_TAG = os.getenv("BOT_TAG", "@Askmovies4")

# Internal
PING_INTERVAL = int(os.getenv("PING_INTERVAL", "120"))
SCRAPE_INTERVAL = int(os.getenv("SCRAPE_INTERVAL", "300"))  # 5 min
SIZE_LIMIT_GB = int(os.getenv("SIZE_LIMIT_GB", 50))
