import telebot
from gtts import gTTS

import weather
import config

bot = telebot.TeleBot(config.botToken)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "Погода":
        bot.send_message(message.from_user.id, weather.get_weather('Москва')['temperature'])
    elif message.text == "Озвучь":
        tts = gTTS("Привет кожанный мешок", lang='ru')
        tts.save('temp.mp3')
        voice = open('./temp.mp3', 'rb')
        bot.send_voice(message.from_user.id, voice)


bot.polling(none_stop=True, interval=0)
