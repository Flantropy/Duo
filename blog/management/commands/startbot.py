import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from django.core.management.base import BaseCommand


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I will send you posts from djangoblog"
    )


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        auth_token = os.environ.get('BOT_TOKEN')
        updater = Updater(token=auth_token)
        dispatcher = updater.dispatcher

        start_handler = CommandHandler('start', start)
        echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(echo_handler)

        updater.start_polling(poll_interval=5)
        updater.idle()
