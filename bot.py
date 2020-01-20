TOKEN = "1010469706:AAGnCju4A6fsfKjo9Ubnoiy9uZeocwT64k4"


import telegram
bot = telegram.Bot(token= str(TOKEN))
print(bot.get_me())

from telegram.ext import Updater
updater = Updater(token= str(TOKEN))
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, testing bot with heroku")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def me(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="tings!")

from telegram.ext import CommandHandler
me_handler = CommandHandler('test', me)
dispatcher.add_handler(me_handler)

def echo(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)
    caps_handler = CommandHandler('caps', caps, pass_args=True)
    dispatcher.add_handler(caps_handler)
           
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

#updater.start_polling()

import os
import logging
if __name__ == "__main__":
    
    TOKEN = "667940096:AAHPD6lVQ1yTxRsZi48HXPilfAhVkO3sYhY"
    NAME = "days10/webhook"

    PORT = os.environ.get('PORT')

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    from telegram.ext import Updater
    updater = Updater(token= str(TOKEN))
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)
    
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    
updater.idle()    
