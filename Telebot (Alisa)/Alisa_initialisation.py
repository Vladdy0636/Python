#import telebot
import json
import telebot

#load

def load_bot():
    file_path = "database.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    bot = telebot.TeleBot(data['api'])
    #bot = AsyncTeleBot('token')
    return bot
        
#____
def load_data():
    file_path = "database.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
        
def load_config():
    file_path = "config.json" 
    with open(file_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config
    
def load_logs():
    file_path = "logs.json" 
    with open(file_path, 'r', encoding='utf-8') as file:
        logs = json.load(file)
    return logs
     
def load_log_update():
    file_path = "last_update.json" 
    with open(file_path, 'r', encoding='utf-8') as file:
        logs = json.load(file)
    return logs


        
    
           
           
#save          
           
def save_logs(logs):
    file_path = "logs.json"
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(logs, file, indent=3, ensure_ascii=False)
        
def update_data(data):
    file_path = "database.json"
    with open(file_path, 'w', encoding='utf-8') as data_file:
        json.dump(data, data_file, indent=1, ensure_ascii=False)

def save_log_update(log_update):
    file_path = "last_update.json"
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(log_update, file, indent=3, ensure_ascii=False)
        
def save_config(config):
    file_path = "config.json"
    with open(file_path, 'w') as config_file:
        json.dump(config, config_file, indent=4)