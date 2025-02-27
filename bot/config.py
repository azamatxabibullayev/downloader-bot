import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_SERVER_URL = os.getenv("API_SERVER_URL")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set. Check your .env file.")

if not API_SERVER_URL:
    raise ValueError("API_SERVER_URL is not set. Check your .env file.")
