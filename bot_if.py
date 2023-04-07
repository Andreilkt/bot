@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, 'Сколько вам лет?')
    bot.register_next_step_handler(msg, askAge)

def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Возраст должен быть числом, введите ещё раз.')
        bot.register_next_step_handler(msg, askAge) #askSource
        return
    msg = bot.send_message(chat_id, 'Спасибо, я запомнил что вам ' + text + ' лет.')