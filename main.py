
import telebot
import rates
import PostgreSQL
import pymorphy2

with open('start.txt', 'r', encoding='utf-8') as f:
        start_str = f.read()

with open('help.txt', 'r', encoding='utf-8') as f:
        help_str = f.read()

morph = pymorphy2.MorphAnalyzer(lang='ru')
bot = telebot.TeleBot('5401677755:AAHlwp1PkF7mTmU3tV9j90WGqb6j_6EVBMA')


@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, start_str)


@bot.message_handler(commands=["help"])
def help(m, res=False):
        bot.send_message(m.chat.id, help_str)

@bot.message_handler(commands=["rates"])
def rates(m, res=False):
        rates_string = rates.main()
        bot.send_message(m.chat.id,rates_string )

@bot.message_handler(content_types=['text'])
def rate(m, res=False):
        print(m.text)
        answer = PostgreSQL.main(m.text)
        bot.send_message(m.chat.id,answer)




bot.polling(none_stop=True, interval=0)

    
