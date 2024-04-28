import asyncio
from aiogram import Bot, Dispatcher

from configurations import load_config, Config
from handlers import user_handlers, text_handlers


async def main() -> None:
    # loading configuration with the func from .env
    config: Config = load_config()

    bot = Bot(config.bot.token)
    dp = Dispatcher()

    dp.include_router(user_handlers.router)

    # don't process old updates
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
