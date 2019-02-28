import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
loggers = logger.setLevel(logging.INFO)

print(logger)
print(loggers)

loggert = logger.setLevel(logging.DEBUG)
print(loggert)

TOKEN = ""

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
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me! or /help /me")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def me(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="me ooonnggg")

from telegram.ext import CommandHandler
me_handler = CommandHandler('me', me)
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

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
def inline(bot, update):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    
from telegram.ext import CommandHandler
inline_handler = CommandHandler('in', inline)
dispatcher.add_handler(inline_handler)



def button(bot, update):
    query = update.callback_query
    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

from telegram.ext import Updater, CallbackQueryHandler
updater.dispatcher.add_handler(CallbackQueryHandler(button))
                       
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

#updater.start_polling()
updater.idle()    
