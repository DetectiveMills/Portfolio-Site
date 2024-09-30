from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings
from telebot import TeleBot, types
from .models import UserContact

TELEGRAM_TOKEN = '7499401234:AAGwaSFJ0dDf4weRCVv4k5-hU-fqrbVrUWE'
ADMIN_ID = '1306350786'


bot = TeleBot(TELEGRAM_TOKEN, threaded=False)
admin_id = ADMIN_ID

@bot.message_handler(commands=['start'])
def start(message:types.Message):
    # UserContact.objects.get_or_create()
    # bot.delete_message(message.chat.id, message.message_id) 
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")

def get_text(message):
    bot.send_message(admin_id, message)

@bot.message_handler()  
def echo(message:types.Message):
    # bot.delete_message(message.chat.id, message.message_id)  
    bot.send_message(message.chat.id, "Я вас не понял")