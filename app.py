from flask import Flask, request
import requests
import os
from telegram import Bot, Update

# flask app
app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return 'hi from Python-2022I'
    # get data from request
    elif request.method == 'POST':
        data = request.get_json(force=True)

        # update
        update: Update = Update.de_json(data, bot)

        # get chat_id, text from update
        chat_id = update.message.chat.id
        text = update.message.text

        # sendMessage
        if text != None:
            print(update)
            bot.send_message(chat_id, text)

        return 'ok'