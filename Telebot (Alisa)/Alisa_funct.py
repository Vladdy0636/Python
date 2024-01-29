#universal code for bots, all that you need, just edit you telegram API in data.json
import json
from telebot.async_telebot import types
import datetime
import threading
import time

import Alisa_initialisation
import Alisa_check

def save_messages(message, logs, bot):
    current_time = str(datetime.datetime.now().time())
    current_date = str(datetime.datetime.now().date())
    user_name = str(message.from_user.username)
    chat_id = str(message.chat.id)
    if current_date not in logs[chat_id]:
        logs[chat_id].update({current_date:{}})
        
    logs[chat_id][current_date].update({current_time:{
        "chat_name": str(message.chat.title),
        "user_name": user_name,
        "user_id": message.from_user.id,
        'name': message.from_user.first_name,
        "message_text": message.text}})
        
    #Alisa_funct.save_last_logs(message, data, config, bot, logs_update)    
    Alisa_initialisation.save_logs(logs)

def send_good_morning():
    #no ready now
    pass

def change_custom_name(message, data, config, bot, message_1, time_send, user_id):
    if time.time() < time_send + 15:
        print("start change user")
        chat_id = str(message.chat.id)
        user_id_1 = str(message_1.from_user.id)
        
        if user_id != user_id_1:
            check_words(message, data, config, bot, message_1, time_send, user_id)
            
        elif user_id_1 == user_id and time.time() < time_send + 15:
            if Alisa_check.check_any_bad_words(message_1, data) == True:
                bot.reply_to(message_1, "Це погане слово, обери інше")
                bot.register_next_step_handler(message, lambda message_1: change_custom_name(message, data, config, bot, message_1, time_send, user_id))
            else:
                print(Alisa_check.check_any_bad_words(message, data))
                data['All_chats'][chat_id]['users'][user_id]["custom_name"] = message.text
                bot.send_message(message.chat.id, "Добре, я змінила ваше ім'я")
                Alisa_initialisation.update_data(data)
    else:
        if time.time() < time_send + 35:
            bot.reply_to(message.chat.id, "Час вийшов")
            
    
def update_bad_words(message, message_1, data, logs, time_send, config, bot):
    while time_send > time.time() + 15:
        user_id = str(message.from_user.id)
        chat_id = str(message.chat.id)
        user_id_1 = str(message_1.from_user.id)
        
        if user_id != user_id_1:
            check_words(message, data, config, bot, message_1, time_send, user_id)
            
        elif user_id_1 == user_id and time.time() < time_send + 15:
            data['All_chats']['bad_words'].update(message_1)
            Alisa_initialisation.update_data(data)
        
        if time_send > time.time() + 15:
            bot.register_next_step_handler(message, lambda message_1: update_bad_words(message, message_1, data, logs, time_send, config, bot))
        

def ping_all_users(message, data, bot):
    message_text = ''    
    entities = []
    length_message = int(0)
    num_users = int(0)
    repeate_cycle = int(0)
    for num in data['All_chats'][str(message.chat.id)]['users']:
        num_users+=1
    
    for users in data['All_chats'][str(message.chat.id)]['users']:
        custom_name = data['All_chats'][str(message.chat.id)]['users'][users]['custom_name']
        name = data['All_chats'][str(message.chat.id)]['users'][users]['name']
        print(custom_name)
        if custom_name is not None:
            user = {'id':users, 'is_bot': False, 'first_name': custom_name}
        else:
            user = {'id':users, 'is_bot': False, 'first_name': name}
        user = json.dumps(user)
        user_dict = json.loads(user)
        message_text += str(user_dict['first_name'])
        length_ping = len(user_dict['first_name'])
        
        entities.append(
           types.MessageEntity(type='text_mention', offset=length_message, length=length_ping, user=json.loads(user))
            )     
        if num_users > repeate_cycle:
            message_text += ', '
            length_message = len(message_text)

        
        repeate_cycle+=1

    bot.send_message(message.chat.id, message_text, entities=entities)
    
def send_perdatel(message, data, config, bot):
    try:
        audio = open('dissapoint.mp3', 'rb')
    except Exception as e:
        print("Error, when opening file")
    else:
        chat_id = message.chat.id
        bot.send_voice(chat_id, audio)
        audio.close() 
        
    bot.delete_message(message.chat.id, message.message_id)

#not the best variant to solve problem   
def check_words(message, data, config, bot, message_1, time_send, user_id):
    chat_id = str(message.chat_id)
    
    if Alisa_check.check_any_bad_words(message, data) == True:
        bot.send_message(message.chat.id, "ай, яй, яй. Так не можна говорити !")
        send_perdatel(message, data, config, bot)
    
def add_new_chat(message, data, config, logs, bot):
    current_time = str(datetime.datetime.now().time())
    current_date = str(datetime.datetime.now().date())
    user_name = str(message.from_user.username)
    chat_id = str(message.chat.id)
    logs.update({chat_id:{}})
    logs[chat_id].update({current_date:{}})
    logs[chat_id][current_date].update({current_time:{}})
    
    message_to_save = {
        "chat_name": str(message.chat.title),
        "user_name": user_name,
        "user_id": message.from_user.id,
        'name': message.from_user.first_name,
        "message_text": message.text}
    logs[chat_id][current_date][current_time].update(message_to_save)
    
    data['All_chats'].update(chat_id)
    data['All_chats'][chat_id].update('users')
    data['All_chats'][chat_id].update('bad_words')
    
    save_messages(message, data, config, logs, bot)  
    
    #Alisa_funct.save_last_logs(message, data, config, bot, logs_update)    
    
    config.update({chat_id:{
        "Agression": False,
        "More_sluty": False,
        "Stop_work": False,
        "Tolerance": True,
        "Da_work": False,
        "send_good_morning": False
    }})
    Alisa_initialisation.save_config(config)

def add_new_member(message, data, config, logs):
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    data['All_chats'][chat_id]['users'].update({user_id: {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'custom_name': None,
            'name': message.from_user.first_name}})
                    
    Alisa_initialisation.update_data(data)

def delete_bad_words(message, message_1, data, logs, time_send, config, bot):
    while time_send > time.time() + 15:
        user_id = str(message.from_user.id)
        chat_id = str(message.chat.id)
        user_id_1 = str(message_1.from_user.id)
        
        if user_id != user_id_1:
            check_words(message, data, config, bot, message_1, time_send, user_id)
            
        elif user_id_1 == user_id and time.time() < time_send + 15:
            if message_1 in data['All_chats'][chat_id]['Bad_words']:
                try:
                    data['All_chats'][chat_id]['Bad_words'].pop(message_1)
                except Exception as e:
                    bot.send_message(message.chat.id, "Ой, щось пішло не так")
                else:
                    bot.send_message(message.chat.id, "Добре, я видалила це слово")
                
        if time_send > time.time() + 15:
            bot.register_next_step_handler(message, lambda message_1: delete_bad_words(message, message_1, data, logs, time_send, config, bot))
        else:
            break
        
        
        
        