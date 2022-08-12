
import telebot
from rates import main
import PostgreSQL
import pymorphy2
from data import *

with open('start.txt', 'r', encoding='utf-8') as f: # считываем текст для стартового меню с троку
        start_str = f.read()

with open('help.txt', 'r', encoding='utf-8') as f: # считываем текст для меню /help в строку
        help_str = f.read()

morph = pymorphy2.MorphAnalyzer(lang='ru')
bot = telebot.TeleBot(token=TOKEN) # создаем бота



@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, start_str) # функция для /start


@bot.message_handler(commands=["help"]) # функция для /help
def help(m, res=False):
        bot.send_message(m.chat.id, help_str)

@bot.message_handler(commands=["rates"]) # функция для /rates
def rates(m, res=False):
        rates_string = main()
        bot.send_message(m.chat.id,rates_string )

@bot.message_handler(content_types=['text']) # функция для диалога с ботом
def rate(m, res=False):
        print(m.text)
        answer = PostgreSQL.main(m.text)
        bot.send_message(m.chat.id,answer)


bot.polling(none_stop=True, interval=0) 

    
