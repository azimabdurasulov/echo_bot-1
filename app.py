from flask import Flask, request
import requests
import os
from telegram import Bot, Update

# flask app
app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    # get data from request
    data = request.get_json(force=True)

    # update
    update: Update = Update.de_json(data, bot)

    # get chat_id, text from update
    chat_id = 5075065217
    text = update.message.text

    # sendMessage
    bot.send_message(chat_id, text)

    return 'ok'