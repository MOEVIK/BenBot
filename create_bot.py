import logging
from aiogram import Bot, Dispatcher
#from aiogram.types import ReactionTypeEmoji
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
#from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
import os

#from db_handler.db_class import PostgresHandler

# Получаем значения
load_dotenv()
TOKEN = os.getenv('TOKEN')  # Вернет 'localhost'
TIMEZONE = os.getenv('TIMEZONE')

#pg_db = PostgresHandler(config('PG_LINK'))
scheduler = AsyncIOScheduler(timezone=TIMEZONE)
#admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())