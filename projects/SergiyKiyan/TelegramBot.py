
API_KEY = '6111141908:AAGJ3WNmGnP9JjGv7-o0YYd27rzVFvQishc'
import telebot;
bot = telebot.TeleBot(API_KEY);
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hello":
        bot.send_message(message.from_user.id, "How can I help you?")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Congrats on starting")
    elif message.text == "/help":
            bot.send_message(message.from_user.id, "Write Hello")
    else:
        bot.send_message(message.from_user.id, "I don't understand you /help.")
bot.polling(none_stop=True, interval=0)
