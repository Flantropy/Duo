from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Here is blog bot')


def get_all_posts(update: Update, context: CallbackContext) -> None:
    pass
