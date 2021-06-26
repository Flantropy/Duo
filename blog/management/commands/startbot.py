import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from django.core.management.base import BaseCommand
from blog.models import Post
from random import choice


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


def get_random_post_content(update, context):
    random_post = choice(Post.objects.all())
    try:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=random_post.content
        )
    except Exception as e:
        logging.error(f'exception is {e.__class__} | {e}')


def get_all_posts(update, context):
    posts = Post.objects.all()
    message = f'Total of {Post.objects.count()} posts\n\n'
    for i, post in enumerate(posts):
        message += f'{i}. Title: {post.title} | Author: {post.author} | ID: {post.id}\n\n'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message
    )


def get_post_by_id(update, context):
    post = Post.objects.get(pk=context.args[0])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=post.content
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
        random_post_handler = CommandHandler('random', get_random_post_content)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(echo_handler)
        dispatcher.add_handler(random_post_handler)
        dispatcher.add_handler(CommandHandler('getall', get_all_posts))
        dispatcher.add_handler(CommandHandler('post', get_post_by_id))

        updater.start_polling(poll_interval=5)
        updater.idle()
