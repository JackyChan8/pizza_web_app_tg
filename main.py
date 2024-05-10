import asyncio

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from src.utils.default_commands import set_commands
from src.handlers import user, admin, echo, cancel
from src.config import settings


async def main():
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    await set_commands(bot)

    # Connect Routers
    dp.include_router(user.router)
    dp.include_router(admin.router)
    dp.include_router(cancel.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    print('Bot is Started')
    asyncio.run(main(), debug=False)
