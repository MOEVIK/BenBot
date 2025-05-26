from datetime import datetime

from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReactionTypeCustomEmoji, ReactionTypeEmoji, InputSticker

# from aiogram.enums import ChatType
# from aiogram.utils.chat_member import ADMINS

from create_bot import bot

from config import BotConfig, Users

from dotenv import load_dotenv
import os

#from db_handler.db_class import PostgresHandler

# Получаем значения
load_dotenv()
# TOKEN = os.getenv('TOKEN')  # Вернет 'localhost'
# TIMEZONE = os.getenv('TIMEZONE')
TARGET_USERNAMES =  os.getenv('BENTARGETS')
ADMINSTRATOR =  os.getenv('ADMINSTRATORS')
EMOJI_ID =  os.getenv('EMOJI_ID')

start_router = Router()


ACTIVE = False

# /start
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Вы Бэн!')

# /id
# @start_router.message(F.text == 'id')
# async def get_user_id(message: types.Message):
#     await message.answer(f"Your ID: {message.from_user.id}")


@start_router.message()
async def react_to_target_user(message: types.Message):
    print(f"Who: {message.from_user.full_name}\nWhen: {datetime.now()}")
    if BotConfig.ACTIVE and (message.from_user.full_name in TARGET_USERNAMES) :
        try:
            await bot.set_message_reaction(
                chat_id=message.chat.id,
                message_id=message.message_id,
                reaction=[ReactionTypeEmoji(emoji="🤡")], #🤡 😐 😁 👎 ☝️ 👉
                #reaction=[ReactionTypeCustomEmoji(custom_emoji_id=EMOJI_ID)],
                #reaction=[CustomEmoji(custom_emoji_id="5289947829337353886")],
                is_big=False
            )
        except Exception as e:
            print(f"Ошибка в тебе: {e}")

        """Ответить кастомным стикером (эмодзи)"""
        # combo_text = f"<tg-emoji emoji-id=\"5289947829337353886\">😐</tg-emoji>👉"
        try:
            await bot.send_sticker(
                chat_id=message.chat.id,
                sticker=InputSticker(

                    sticker=EMOJI_ID,
                    emoji_list=["😐"]  # Можно указать любой эмодзи для отображения
                ),
                reply_to_message_id=message.message_id
            )
        except Exception as e:
            print(f"Ошибка в тебе: {e}")

    elif message.from_user.full_name in ADMINSTRATOR:
        print(f"Message: {message.text}\nWhen: {datetime.now()}")
        if 'БЕЗЗЛОБИЕ' in message.text:
            BotConfig.ACTIVE = True
            await message.answer(f"Активация БЭНА!")
        elif 'ХРЮКОСТЯГ' in message.text:
            BotConfig.ACTIVE = False
            await message.answer(f"Ну проБЭНишься заходи...")

# Хэндлер для отладки (ловит ВСЕ сообщения в группах)
# @start_router.message()
# async def debug_all_group_messages(message: types.Message):
#     print(f"Групповое сообщение от {message.from_user.id}: {message.text}")