from telegram import Update
from telegram.ext import CallbackContext
from os import getenv
import json
import urllib.request


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Here is blog bot')


def get_all_posts(update: Update, context: CallbackContext) -> None:
    BASE_URL = 'http://127.0.0.1:8000/' if (getenv('IS_IN_DEBUG') == 'True') else 'https://frootpy.herokuapp.com'
    response = urllib.request.urlopen(BASE_URL + 'api/posts/').read()
    posts = json.loads(response)
    message = ''
    for post in posts:
        message += f'{post["id"]}. {post["title"]}\n'
    update.message.reply_text(message)
