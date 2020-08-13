from emoji import emojize
from glob import glob
import logging
from random import choice, randint
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Hello, my dear friend {context.user_data['emoji']}!")

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f"{user_text} {context.user_data['emoji']}")

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
        message = (f"You're number is {user_number}, mine number is {bot_number} - You're winning!")
    elif user_number == bot_number:
        message = f"You're number is {user_number}, mine number is {bot_number} - Draw!"
    elif user_number < bot_number:
        message = f"You're number is {user_number}, mine number is {bot_number} - Bot is winning!"
    return message

def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
           message = 'Enter the integer number'
    else:
        message = 'What number?'
    update.message.reply_text(message)

def send_cat_pic(update, context):
    cat_pics_list = glob('images/cat*.jp*g')
    cat_pic_name = choice(cat_pics_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_name, 'rb'))

def main():
    mybot = Updater(settings.API_KEY , use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_pic))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot is run')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
