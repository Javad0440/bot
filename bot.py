from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
TOKEN='7502748917:AAHGESYvkf6I1dUO9x0k3x7rjuQdWwhCoqc'
def handle_message(update=Update, context=CallbackContext):
    message = update.message.text
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, f"پیامت دریافت شد: {message}")
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
