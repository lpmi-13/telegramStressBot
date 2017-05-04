from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import logging

from flask import Flask, request, Response

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


@app.route('/', methods=['POST'])
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='send me a sentence and I\'ll send you the stress!')

def echo(bot, update):
#do python parsing and tagging and predicting here

    text = update.message.text
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

updater = Updater(token=os.environ['API-TOKEN'])

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler([Filters.text], echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
