@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет" or "какие сейчас скидки":
        bot.send_message(chat_id, 'Привет, я бот - парсер скидок, сейчас поищу скидки')
    elif text == "какие сейчас скидки"  :
        bot.send_message(chat_id, 'Хорошие')

    elif text == "минутные скидки" or "горящие скидки":
        bot.send_message(chat_id, "Для Вас все есть" )
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')

        if text == "Найди скидку":
            bot.send_message(chat_id, 'Подожди поищу.')
        elif text == "Ну как там":
            bot.send_message(chat_id, 'Пока ищу')
        else:
            bot.send_message(chat_id, 'Простите, я вас не понял :(')
