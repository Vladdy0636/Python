#універсальний код для бота, можна використовувати замінивши 
import json
import datetime
import telebot
import time
from threading import Thread
import threading

#легше редагувати за допомогою модулів
import Alisa_initialisation
import Alisa_funct
import Alisa_check

#загружаємо бота (т)
bot = Alisa_initialisation.load_bot()
data = Alisa_initialisation.load_data()
config = Alisa_initialisation.load_config()
logs = Alisa_initialisation.load_logs()

id_bot = bot.get_me()

@bot.message_handler(commands=['start'])
def some_one_start(message):
    bot.send_message(message.chat.id, "Привіт, я Аліса, бот якій може виконувати різноманітні функції")

@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    if message.json['new_chat_participant']['id'] == id_bot:
        bot.send_message(message.chat.id, "Всім привіт")
        Alisa_funct.add_new_chat(message, data, config, logs, bot)
    else:
        new_member_name = message.json['new_chat_member']['first_name']
        bot.send_message(message.chat.id, f"Вітаю, {new_member_name}")
        Alisa_funct.add_new_member(message, data, config, logs)
        
@bot.message_handler(commands=['status'])
def check_status(message):
    if Alisa_check.check_is_it_developer(message, data) == True:
        bot.send_message(message.chat.id, "Наразі я працюю")
    else:
        Alisa_funct.save_alarm(message, data, logs)

@bot.message_handler(commands=['ping_all'])
def ping_all(message, data):
    bot.send_message(message.chat.id, "Ось, всі кого я знаю")
    Alisa_funct.ping_all_users(message, data)

#_____
@bot.message_handler(commands=['change_name'])
def fist_step_change_name(message):
    user_id = str(message.from_user.id)
    bot.reply_to(message, "Чудово, надішліть мені ваше ім'я")
    time_send = time.time()
    bot.register_next_step_handler(message, lambda message_1: Alisa_funct.change_custom_name(message, data, config, bot, message_1, time_send, user_id))
    
    
@bot.message_handler(commands=['Add_bad_word'])
def add_bad_word(message):
    time_send = time.time()
    bot.register_next_step_handler(message, lambda message_1: Alisa_funct.update_bad_words(message, message_1, data, logs, time_send, config, bot))
    Alisa_funct.save_messages(message, logs, bot)

@bot.message_handler(commands=['Delete_bad_word'])
def delete_bad_word(message):
    bot.reply_to(message, "Чудово, надішліть мені це слово")
    time_send = time.time()
    bot.register_next_step_handler(message, lambda message_1: Alisa_funct.delete_bad_words(message, message_1, data, logs, time_send, config, bot))
    Alisa_funct.save_messages(message, logs, bot)
    
@bot.message_handler(func=lambda message: True)
def check_words(message):
    print("\n\n", message)
    chat_id = str(message.chat.id)
    
    if str(message.from_user.id) not in data['All_chats'][chat_id]["users"]:
        Alisa_funct.add_new_member(message, data, config, logs)
        
    if Alisa_check.check_any_bad_words(message, data) == True:
        bot.send_message(message.chat.id, "Ай, яй, яй. Так не можна говорити !")
        Alisa_funct.send_perdatel(message, data, config, bot)
        
        
    Alisa_funct.save_messages(message, logs, bot)

# Start the bot's polling
def start_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5) 

bot_thread = Thread(target=start_bot)
bot_thread.start()
