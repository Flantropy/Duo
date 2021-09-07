import json
import urllib.request
from os import getenv

from telegram import Update
from telegram.constants import PARSEMODE_HTML
from telegram.ext import CallbackContext


def __get_base_url() -> str:
    return 'http://127.0.0.1:8000/' if (getenv('IS_IN_DEBUG') == 'True') else 'https://frootpy.herokuapp.com/'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Here is blog bot')


def get_all_posts(update: Update, context: CallbackContext) -> None:
    base_url = __get_base_url()
    posts_url = f'{base_url}api/posts/'
    response = urllib.request.urlopen(posts_url).read()
    posts = json.loads(response)
    message = ''
    for post in posts:
        post_url = f'{base_url}post/{post["id"]}/'
        message += f'{post["id"]}. <a href="{post_url}">{post["title"]}</a>\n'
    update.message.reply_text(message, parse_mode=PARSEMODE_HTML)


def get_post_by_id(update: Update, context: CallbackContext) -> None:
    base_url = __get_base_url()
    post_url = f'{base_url}api/post/{context.args[0]}/'
    response = urllib.request.urlopen(post_url).read()
    post = json.loads(response)
    web_page_url = f'{base_url}post/{context.args[0]}/'
    update.message.reply_text(
        f'{post["id"]}. <a href="{web_page_url}">{post["title"]}</a>.\n'
        f'By {post["author"]}.'
        f'\n{post["content"]}',
        parse_mode=PARSEMODE_HTML)
