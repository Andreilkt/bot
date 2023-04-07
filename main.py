import telebot;
bot = telebot.TeleBot('%1632439641:AAE-WEigKZktbUOtpp4cC8YwLBPRxjm4HeE%');

#@bot.message_handler(content_types=['text'])
#def get_text_messages(message):

@bot.message_handler(content_types=['text','document', 'audio'])
def get_text_messages(message):
    #bot.polling(none_stop=True, interval=0)
    bot.polling(none_stop=True, interval=0)