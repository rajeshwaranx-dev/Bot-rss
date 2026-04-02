import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

# Telegram
API_ID = int(os.getenv("API_ID", "36633051"))
API_HASH = os.getenv("API_HASH", "ba52b4e3afcebd6f82696308ac5afc42")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8728470482:AAEoDmBqEl9eMbyarzpTvLdW4V-CwzOnafE")  # Get from @BotFather

# Web
PORT = int(os.getenv("PORT", "8080"))
URL = os.getenv("URL", "")  # Your VPS IP or Koyeb/Render URL

# MongoDB
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Askrss:Askrssx@cluster0.1mqswlh.mongodb.net/?appName=Cluster0")
DATABASE_NAME = os.getenv("DATABASE_NAME", "Askrss")

# TamilMV settings
TMV_URL = os.getenv("TMV_URL", "https://www.1tamilmv.immo/")
TMV_TORRENT = int(os.getenv("TMV_TORRENT", "-1003498539379"))
TMV_LEECH_GRP = int(os.getenv("TMV_LEECH_GRP", "-1002007085025"))
TMV_MIRROR_GRP = int(os.getenv("TMV_MIRROR_GRP", "0"))
TMV_TORRENT_THUMB = os.getenv("TMV_TORRENT_THUMB", "https://i.ibb.co/ZzkWK8gG/Gemini-Generated-Image-m052bhm052bhm052.png")
BOT_TAG = os.getenv("BOT_TAG", "@AskBotz")

# Internal
PING_INTERVAL = int(os.getenv("PING_INTERVAL", "120"))
SCRAPE_INTERVAL = int(os.getenv("SCRAPE_INTERVAL", "180"))  # 5 min
SIZE_LIMIT_GB = int(os.getenv("SIZE_LIMIT_GB", 50))
