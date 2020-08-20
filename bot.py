import logging
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from handlers import (greet_user, talk_to_me, 
                      guess_number, send_cat_pic, user_location,
                      check_user_pic)

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_pic))
    dp.add_handler(MessageHandler(
        Filters.regex('^(Give me a cat)$'), send_cat_pic))
    dp.add_handler(MessageHandler(Filters.location, user_location))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.photo, check_user_pic))
    logging.info('Bot is run')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
