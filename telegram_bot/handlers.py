from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from .crud import list_pending_orders, take_order, cancel_order

async def notify_masters(context: ContextTypes.DEFAULT_TYPE):
    orders = await list_pending_orders()
    for o in orders:
        kb = InlineKeyboardMarkup([[
          InlineKeyboardButton("✔️ Взять", callback_data=f"take:{o['id']}"),
          InlineKeyboardButton("❌ Не беру", callback_data=f"not:{o['id']}")
        ]])
        # здесь нужно перебрать активных мастеров и рассылать им o
        # context.bot.send_message(chat_id=telegram_id, text=..., reply_markup=kb)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    action, oid = data.split(":")
    uid = update.callback_query.from_user.id
    if action=="take":
        await take_order(int(oid), uid)
    else:
        # можно спросить текст комментария через следующий шаг диалога
        await cancel_order(int(oid), uid, "Причина не указана")
    await update.callback_query.answer("Готово")
