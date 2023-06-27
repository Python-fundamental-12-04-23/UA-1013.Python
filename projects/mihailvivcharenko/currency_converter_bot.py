import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6280854951:AAEKNaJ9KaZzqJS3rCG2uya-zAjHW1Tnjkk')

currency = CurrencyConverter()

amount = 0


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Hello! Enter an amount.")
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "Wrong format. Try again!")
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        item2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        item3 = types.InlineKeyboardButton('GBP/USD ', callback_data='gbp/usd')
        item4 = types.InlineKeyboardButton('Other... ', callback_data='else')

        markup.add(item1, item2, item3, item4)
        bot.send_message(
            message.chat.id, "Select a currency pair.", reply_markup=markup)
    else:
        bot.send_message(
            message.chat.id, f"Your number {amount} < 0 😬. Try again!")
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"Result: {round(res,2)}.")
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(
            call.message.chat.id, 'Enter both currencies with a slash. For example USD/GBP.')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f"Result: {round(res,2)}.")
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(
            message.chat.id, "Something wrong 🙁. Re-enter the value.")
        bot.register_next_step_handler(message, my_currency)


bot.polling(none_stop=True)
