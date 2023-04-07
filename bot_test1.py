import sqlite3
import bs4
import parser
import telebot
#main variables
TOKEN = "1632439641:AAE-WEigKZktbUOtpp4cC8YwLBPRxjm4HeE"
bot = telebot.TeleBot(TOKEN)


conn = sqlite3.connect('bot_base.db', check_same_thread=False)
cursor = conn.cursor()

#handlers
@bot.message_handler(commands=['start', 'go'])
#def start_handler(message):
    #bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить скидки с Али')

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_photo(message.chat.id, "https://i.imgur.com/ofwPfHE.png")


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - парсер скидок.')
    else: bot.send_message(chat_id, 'Что вы хотели')

@bot.message_handler(content_types=['text'])
def text_handler1(message):
    text1 = message.text.lower()
    chat_id = message.chat.id
    if text1 =="Hi":
        bot.send_message(chat_id, 'Привет, я найду Вам выгодные скидки.')


    elif text1 == 'Скидки':
        bot.send_message(chat_id, 'Какие')

    elif text1 == 'горячие':
        bot.send_message(chat_id, 'Сейчас найду')


    elif text1 == 'Распродажи есть':
        bot.send_message(chat_id, 'Растродажи есть')


    else:
        bot.send_message(chat_id, 'Простите, я вас не понял ')

bot.polling()
