# 502807485 Vitya
# 560220503 Dimon
# 473903880 Kemba
# 467045448 kola
# 1090285304 ya
# 1765371139 sanya

TARGET_USER_ID = 1090285304
TARGET_USERNAMES = {"@Vovak45", "@Kemba7", "@DaimonV17"}

from aiogram import F, types, Router
from aiogram.enums import ChatType
from aiogram.types import ReactionTypeEmoji

# 1. Создаем отдельный роутер ТОЛЬКО для групповых сообщений
group_router = Router()
group_router.message.filter(F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))


# 2. Хэндлер для целевого пользователя в группах
@group_router.message(F.from_user.id == TARGET_USER_ID)
async def react_to_target_user(message: types.Message):
    print(f"Обработка сообщения от {message.from_user.id} в чате {message.chat.id}")

    try:
        await message.bot.set_message_reaction(
            chat_id=message.chat.id,
            message_id=message.message_id,
            reaction=[ReactionTypeEmoji(emoji="👎")],
            is_big=False
        )
    except Exception as e:
        print(f"Ошибка реакции: {e}")
        await message.reply("Не удалось поставить реакцию")


@group_router.message(F.from_user.username.in_(TARGET_USERNAMES))
async def react_by_username(message: types.Message):
    await message.bot.set_message_reaction(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reaction=[ReactionTypeEmoji(emoji="👎")]
    )


