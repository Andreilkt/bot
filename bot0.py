import bs4
import parser

#main variables
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить  скидки')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - парсер скидок.')
    #elif text == "Как дела":
         #bot.send_message(chat_id, 'Хорошо, а у тебя?')

    elif text == "Какие есть скидки":
         bot.send_message(chat_id, 'Хорошие')

    #elif text == "Есть минутные":
         #bot.send_message(chat_id, 'есть')
    else:
         bot.send_message(chat_id, 'Простите, я вас не понял')

bot.polling()
