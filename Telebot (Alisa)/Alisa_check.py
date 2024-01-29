import json
import datetime
import telebot
import time
from threading import Thread

def check_is_it_developer(message, data):
    user_id = str(message.from_user.id)
    
    #if user_id in data['list_of_developers']:
    return True
    #else:
        #return False
    
def check_any_bad_words(message, data):
    chat_id = str(message.chat.id)
    words = message.text.lower().split()
    
    for word in words:
        print(word)
        #if word in data[chat_id]['bad_words']:
        if word in data['Bad_words']:
            return True
        elif word in data['All_chats'][chat_id]['bad_words']:
            return True 
    return False 