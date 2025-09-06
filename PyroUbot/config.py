import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999999999"))

DEVS = list(map(int, os.getenv("DEVS", "8463333178").split()))

API_ID = int(os.getenv("API_ID", "28473241"))

API_HASH = os.getenv("API_HASH", "c3df70b867a0e65eed5419cecdd5a5bd")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8361538579:AAGc-5yshJZIw676SBljk54hh59B2Lj873U")

OWNER_ID = int(os.getenv("OWNER_ID", "8463333178"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002399953106").split()))

RMBG_API = os.getenv("RMBG_API", "twjWqdXoykgR4cKojWMobMjD")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://orkutp87_db_user:ambasing101@cluster0.c6jldnj.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("8463333178"))

USER_GROUP = os.getenv("USER_GROUP", "@rpkaii")
