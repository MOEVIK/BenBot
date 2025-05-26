import asyncio
from create_bot import bot, dp

from handlers.single import start_router
#from handlers.group import group_router
from config import BotConfig


async def main():
    #dp.include_router(group_router)
    dp.include_router(start_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    BotConfig.ACTIVE = False
    BotConfig.Users = []
    asyncio.run(main())