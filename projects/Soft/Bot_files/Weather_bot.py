import telebot
from telebot import types
import requests
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(filename='stats.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

load_dotenv()

bot = telebot.TeleBot(os.getenv('tg_bot_api'))


class WeatherBot:
    def __init__(self):
        self.api_key = os.getenv('open_weather_api')

        self.emoji_dict = {
            'cloud': "Хмарно ☁️",
            'rain': "Дощ 🌧️", 
            'sun': "Сонячно ☀️",
            'snow': "Сніг ❄️",
            'thunderstorm': "Гроза ⛈️",
            'few clouds': "Переважно хмарно 🌤️",
            'clear sky': "Ясно 🌞",
            'mist': "Туман/мгла 🌫️",
            'smoke': "Дим 🌫️",
            'haze': "Мгла/туман 🌫️",
            'dust': "Пил/пилина 🌫️",
            'fog': "Туман/мгла 🌫️",
            'sand': "Піщана буря 🌫️",
            'ash': "Попіл/вулканічний попіл 🌋",
            'squall': "Шквал 💨",
            'tornado': "Торнадо 🌪️"
        }

        self.gif_dict = {
            'cloud': 'cloudy.gif',
            'rain': 'rain.gif',
            'sun': 'sun.gif',
            'snow': 'snow.gif',
            'thunderstorm': 'thunderstorm.gif',
            'few clouds': 'variable cloudiness.gif',
            'clear sky': 'clear sky.gif',
            'mist': 'haze.gif',
            'smoke': 'haze.gif',
            'haze': 'light fog.gif',
            'dust': 'dust.gif',
            'fog': 'mist.gif',
            'sand': 'sandstorm.gif',
            'ash': 'volcanic ash.gif',
            'squall': 'squall.gif',
            'tornado': 'tornado.gif'
        }

    def start(self, message):
        bot.send_message(
            message.chat.id,
            f"Привіт, {message.from_user.first_name}! Хочеш дізнатись погоду в своєму місті?",
            parse_mode='html'
        )
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        answer1 = types.KeyboardButton('Так')
        answer2 = types.KeyboardButton('Ні')
        markup.add(answer1, answer2)
        bot.send_message(message.chat.id, 'Вибери одну з опцій:', reply_markup=markup)

    def handle_message(self, message):
        if message.chat.type == "private":
            if message.text == "Так":
                bot.send_message(message.chat.id, 'Напиши назву міста нижче')
            elif message.text == "Ні":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                exit_button = types.KeyboardButton('Вийти')
                markup.add(exit_button)
                bot.send_message(message.chat.id, "Ну гаразд 😔\nСпишемось пізніше!", reply_markup=markup)
            elif message.text == "Вийти":
                bot.send_message(message.chat.id, "Ви вийшли з меню.", reply_markup=None)
            else:
                self.check_weather(message)

    def check_weather(self, message):
        if message.chat.type == "private":
            if message.text == "":
                bot.send_message(message.chat.id, "Ти не ввів назву міста.")
                return

            self.log_city(message.from_user.id, message.text)

            url = f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&units=metric&appid={self.api_key}"
            response = requests.get(url)
            data = response.json()

            if 'weather' in data:
                weather_description = data['weather'][0]['description']
                temperature = int(data['main']['temp'])
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                emoji = self.get_emoji(weather_description)
                gif_filename = self.get_gif_filename(weather_description)

                if gif_filename:
                    with open(gif_filename, 'rb') as gif_file:
                        bot.send_animation(message.chat.id, gif_file)

                response_message = f"Погода у місті {message.text}:\n\n" \
                                   f"Погодні умови: {emoji}\n" \
                                   f"Температура наразі складає: {temperature}°C\n" \
                                   f"Вологість: {humidity}%\n" \
                                   f"Швидкість вітру: {wind_speed} м/с"
                bot.send_message(message.chat.id, response_message)
            else:
                bot.send_message(message.chat.id, "Такого міста не існує.")

    def get_emoji(self, description):
        description = description.lower()
        for key, value in self.emoji_dict.items():
            if key in description:
                return value
        return ""

    def get_gif_filename(self, description):
        description = description.lower()
        for key, value in self.gif_dict.items():
            if key in description:
                return os.path.join('weather_gif', value)
        return None

    def log_city(self, user_id, city):
        logging.info(f"User {user_id} picked: {city}")


weather_bot = WeatherBot()


@bot.message_handler(commands=['start'])
def start(message):
    weather_bot.start(message)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    weather_bot.handle_message(message)


bot.polling()
