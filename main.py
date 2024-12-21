import telebot
from telebot import types
import requests

TOKEN = '6792505633:AAF9cgC6ZQ7BIBlHNbIVZuf5pDII-RRd6m4'
bot = telebot.TeleBot(TOKEN)
BASE_URL = "https://api.open-meteo.com/v1/forecast"
day = 0
day_in_words = ''
DAYS = {
    'Сегодня': 0,
    'Завтра': 1,
    'Послезавтра': 2
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton('Предоставить доступ✔', request_location=True)
    item1 = types.KeyboardButton('Сегодня')
    item2 = types.KeyboardButton('Завтра')
    item3 = types.KeyboardButton('Послезавтра')
    markup.add(item1, item2, item3)

    bot.send_message(chat_id,
                     'Привет!Выбери день для прогноза погоды:'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def echo_message(message):
    chat_id = message.chat.id
    global day, day_in_words
    if message.text == '🔙Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Сегодня')
        item2 = types.KeyboardButton('Завтра')
        item3 = types.KeyboardButton('Послезавтра')
        markup.add(item1, item2, item3)

        bot.send_message(chat_id,
                         'Выбери день для прогноза погоды:'.format(
                             message.from_user), reply_markup=markup)
    elif message.text == 'Сегодня' or 'Завтра' or 'Послезавтра':
        day = DAYS[message.text]
        day_in_words = message.text.lower()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton('🔙Назад')
        item1 = types.KeyboardButton('Предоставить доступ✔',
                                     request_location=True)
        markup.add(item1, item2)

        bot.send_message(chat_id,
                         'Предоставь,пожалуйста,доступ к геолокации💠.Проверь, чтобы локация была включена в настройках',
                         reply_markup=markup)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    global day, day_in_words
    # print("{0}, {1}".format(message.location.latitude,
    #                         message.location.longitude))
    chat_id = message.chat.id
    latitude = message.location.latitude
    longitude = message.location.longitude
    print(longitude, latitude)
    params = {
        "latitude": latitude,  # широта Краснодара
        "longitude": longitude,  # долгота Краснодара
        "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum",
        # минимальная и максимальная температура, сумма осадков
        "timezone": "Europe/Moscow"  # временная зона для Краснодара
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        # Поскольку индекс 0 представляет собой данные на текущий день, индекс 1 будет представлять данные на завтра
        tomorrow_temp_min = data['daily']['temperature_2m_min'][day]
        tomorrow_temp_max = data['daily']['temperature_2m_max'][day]
        tomorrow_precipitation = data['daily']['precipitation_sum'][day]

        print(f"Прогноз погоды:")
        print(f"Минимальная температура: {tomorrow_temp_min}°C")
        print(f"Максимальная температура: {tomorrow_temp_max}°C")
        print(f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")
        bot.send_message(chat_id, f"Прогноз погоды на завтра:")
        bot.send_message(chat_id,
                         f"Минимальная температура: {tomorrow_temp_min}°C")
        bot.send_message(chat_id,
                         f"Максимальная температура: {tomorrow_temp_max}°C")
        bot.send_message(chat_id,
                         f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")


    else:
        print(f"Ошибка {response.status_code}: {response.text}")


bot.infinity_polling()
