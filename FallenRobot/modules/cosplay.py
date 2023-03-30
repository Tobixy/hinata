pip install python-telegram-bot

import requests
import telegram
from telegram.ext import CommandHandler, Updater

def cosplayanime_handler(update, context):
    # Make a request to the API to get a random anime cosplay image
    response = requests.get('https://api.waifu.pics/sfw/cosplay-anime')
    image_url = response.json()['url']

    # Send the image to the user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)

updater = Updater(token='6053431823:AAGvYI8gJvLknY6iTDgyW1Qmo77ILZybUI4', use_context=True)
dispatcher = updater.dispatcher

cosplayanime_handler = CommandHandler('cosplayanime', cosplayanime_handler)
dispatcher.add_handler(cosplayanime_handler)

updater.start_polling()
updater.idle()
