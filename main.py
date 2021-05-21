import random as rand
from threading import Thread
import time
import os

import telebot
from telebot import types

import weather
import config
from voice import voice
import consts
import db

token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(token)


def check_user(user_id: int):
    return len(db.get(user_id))


def send_menu(user_id):
    """
    Отправляет меню пользователю
    :param user_id: id пользователя
    """

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    key = types.InlineKeyboardButton(text=consts.menu['voice'])
    keyboard.add(key)
    key = types.InlineKeyboardButton(consts.menu['weather'])
    keyboard.add(key)
    key = types.InlineKeyboardButton(consts.menu['aperture'])
    keyboard.add(key)
    option = consts.menu['unsubscribe'] if check_user(user_id)\
        else consts.menu['subscribe']
    key = types.InlineKeyboardButton(option)
    keyboard.add(key)

    message = rand.choice(consts.hello)
    bot.send_message(user_id, text=message, reply_markup=keyboard)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    """
    Обработчик команд /start и /help
    :param message: Сообщение
    :return:
    """
    send_menu(message.from_user.id)


@bot.message_handler(content_types=['text'])
def main(message):
    """
    Главный обработчик всех сообщений
    :param message: Сообщение
    """

    if message.text == consts.menu['voice']:
        bot.send_message(message.from_user.id, consts.questions[0])
        bot.register_next_step_handler(message, make_voice)
    elif message.text == consts.menu['weather']:
        bot.send_message(message.from_user.id, consts.questions[1])
        bot.register_next_step_handler(message, show_weather)
    elif message.text == consts.menu['aperture']:
        aperture_science(message.from_user.id)
    elif message.text == consts.menu['subscribe']:
        subscribe(message)
    elif message.text == consts.menu['unsubscribe']:
        unsubscribe(message)
    else:
        msg = rand.choice(consts.wrong_answer) + '\n' + consts.start
        bot.send_message(message.from_user.id, msg)


def make_voice(message):
    """
    Сделать голос из аудио
    :param message: Текст
    """

    filename = voice(message.text)
    file = open(filename, 'rb')
    bot.send_voice(message.from_user.id, file)


def show_weather(message):
    """
    Отправить погоду пользователю
    :param message: Сообщение с городом
    """

    try:
        data = weather.get_weather(message.text)
    except Exception:
        bot.send_message(message.from_user.id, consts.errors[0])
        return

    msg = consts.weather.format(
        city=message.text,
        temp=data['temperature'],
        feels=data['feelslike'],
        visibility=data['visibility'],
        weather=data['weather_descriptions'],
        ico=data['ico']
    )
    bot.send_message(message.from_user.id, msg)


def aperture_science(chat_id):
    """
    Отправить лор Portal
    :param chat_id: id пользователя
    """

    msg = rand.choice(consts.aperture)
    bot.send_message(chat_id, msg, parse_mode='Markdown')


def subscribe(message):
    """
    Подписать пользователя на рассылку
    :param message: сообщение от пользователя
    """
    if check_user(message.from_user.id):
        return

    uid = message.from_user.id
    name = message.from_user.first_name
    surname = message.from_user.last_name
    username = message.from_user.username

    db.insert(uid, name, surname, username)
    send_menu(message.from_user.id)


def unsubscribe(message):
    """
    Отписать пользователя от рассылки
    :param message: сообщение от пользователя
    """
    if not check_user(message.from_user.id):
        return

    db.delete(message.from_user.id)
    send_menu(message.from_user.id)


def mailing():
    """
    Рассылка подписчикам
    """
    users = db.get_all()
    for user in users:
        aperture_science(user[1])


def scheduler():
    """
    Производить рассылку с определённым периодом
    """
    while True:
        time.sleep(config.timeToMailing)
        mailing()


th = Thread(target=scheduler)
th.start()

bot.polling(none_stop=True, interval=0)
