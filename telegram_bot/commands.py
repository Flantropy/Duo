import json
import urllib.request
from os import getenv

from telegram import Update
from telegram.ext import CallbackContext
from telegram.constants import PARSEMODE_HTML


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Here is blog bot')


def get_all_posts(update: Update, context: CallbackContext) -> None:
    BASE_URL = 'http://127.0.0.1:8000/' if (getenv('IS_IN_DEBUG') == 'True') else 'https://frootpy.herokuapp.com/'
    response = urllib.request.urlopen(BASE_URL + 'api/posts/').read()
    posts = json.loads(response)
    message = ''
    for post in posts:
        post_url = f'{BASE_URL}post/{post["id"]}/'
        message += f'#{post["id"]}. <a href="{post_url}">{post["title"]}</a>\n'
    update.message.reply_text(message, parse_mode=PARSEMODE_HTML)


def get_post_by_id(update: Update, context: CallbackContext) -> None:
    # TODO: add endpoint in api.views for getting specified post by it's id
    pass
