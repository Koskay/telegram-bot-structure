from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
BOT_TOKEN = os.getenv('TOKEN')
ADMIN_ID = os.getenv('ADMIN')
