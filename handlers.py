from glob import glob
from random import choice
from utils import get_smile, play_random_numbers, main_keyboard

def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f"Hello, my dear friend {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f"{user_text} {context.user_data['emoji']}", 
    reply_markup=main_keyboard())

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
    update.message.reply_text(message,reply_markup=main_keyboard())

def send_cat_pic(update, context):
    cat_pics_list = glob('images/cat*.jp*g')
    cat_pic_name = choice(cat_pics_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_name, 'rb'), 
    reply_markup=main_keyboard())

def user_location(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"You're location id {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )
