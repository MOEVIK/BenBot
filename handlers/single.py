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
TARGET_USERNAMES = os.getenv('BENTARGETS')
ADMINSTRATOR = os.getenv('ADMINSTRATORS')
EMOJI_ID = os.getenv('EMOJI_ID')
START_PHRASE = os.getenv('START_PHRASE')
STOP_PHRASE = os.getenv('STOP_PHRASE')

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

# @start_router.message(content_types=types.ContentType.STICKER)
# async def handle_sticker(message: types.Message):
#     sticker_id = message.sticker.file_id
#     await message.reply(f"ID этого стикера: {sticker_id}")

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
        # Sticker(file_id='CAACAgIAAyEFAASG6upCAAIBDGg5xoNd8kwOZDy9hBeUcOt9hfZmAAJTbgACoCI5Sf1BkLKSc9u0NgQ', file_unique_id='AgADU24AAqA...mYAAlNuAAKgIjlJ_UGQspJz27QBAAdtAAM2BA', 'file_unique_id': 'AQADU24AAqAiOUly', 'file_size': 28570, 'width': 320, 'height': 280})
        #stickers = await bot.get_custom_emoji_stickers(["5289947829337353886"])
        #if stickers:
            #sticker = stickers[0].file_id
            #print(f"file_id стикера: {stickers[0].file_id}")
        try:
            await bot.send_sticker(
                chat_id=message.chat.id,
                sticker="CAACAgIAAyEFAASG6upCAAIBDGg5xoNd8kwOZDy9hBeUcOt9hfZmAAJTbgACoCI5Sf1BkLKSc9u0NgQ",
                #message_id=message.message_id,
                reply_to_message_id=message.message_id
            )
            # await bot.send_message(
            #     chat_id=message.chat.id,
            #     text=sticker,
            #     #message_id=message.message_id,
            #     reply_to_message_id=message.message_id
            # )
            await bot.send_sticker

        except Exception as e:
            print(f"Ошибка в тебе: {e}")

    elif message.from_user.full_name in ADMINSTRATOR:
        print(f"Message: {message.text}\nWhen: {datetime.now()}")
        if START_PHRASE in message.text:
            BotConfig.ACTIVE = True
            await message.answer(f"Активация БЭНА!")
        elif STOP_PHRASE in message.text:
            BotConfig.ACTIVE = False
            await message.answer(f"Ну проБЭНишься заходи...")

# Хэндлер для отладки (ловит ВСЕ сообщения в группах)
# @start_router.message()
# async def debug_all_group_messages(message: types.Message):
#     print(f"Групповое сообщение от {message.from_user.id}: {message.text}")