import asyncio
from telegram.ext import ApplicationBuilder, CallbackQueryHandler
import config, handlers

async def main():
    app = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()
    app.add_handler(CallbackQueryHandler(handlers.button_callback))
    # раз в 300 сек. шлём новые заказы
    app.job_queue.run_repeating(handlers.notify_masters, interval=300, first=10)
    await app.run_polling()

if __name__=="__main__":
    asyncio.run(main())
