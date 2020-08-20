from glob import glob
import os
from random import choice
from utils import get_smile, is_cat, main_keyboard, play_random_numbers

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

def check_user_pic(update, context):
    update.message.reply_text('Process the pic')
    os.makedirs('downloads', exist_ok=True)
    user_pic = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join('downloads', f'{user_pic.file_id}.jpg')
    user_pic.download(file_name)
    update.message.reply_text('Pic is safe!')
    if is_cat(file_name):
        update.message.reply_text('Cat is detected, add to library')
        new_file_name = os.path.join('images', f'cat_{user_pic.file_id}.jpg')
        os.rename(file_name, new_file_name)
    else:
        os.remove(file_name)
        update.message.reply_text('Alarm, cat is not identify!')