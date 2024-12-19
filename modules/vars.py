import os

API_ID    = os.environ.get("API_ID", "23671274")
API_HASH  = os.environ.get("API_HASH", "09b9c07a023f7c13c2164f2b22bd937e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
