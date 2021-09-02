import logging
from os import getenv

from telegram.ext import (CommandHandler, Dispatcher, Updater)

from telegram_bot.commands import (
    start
)


def run_bot():
    # Setting up a basic logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Updater and Dispatcher
    updater = Updater(token=getenv('BOT_TOKEN'))
    dispatcher: Dispatcher = updater.dispatcher
    
    # Adding Handlers
    dispatcher.add_handler(CommandHandler('start', start))
    
    # Start Polling
    updater.start_polling(poll_interval=5)
    updater.idle()


if __name__ == '__main__':
    run_bot()
