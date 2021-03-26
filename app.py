import telebot
from flask import Flask, request
import os
import random

TOKEN = '1668076384:AAF4aDoDF6_KqaADNtgGjUIdgykdVAM4qtI'
APP_NAME = 'https://error-bot-check.herokuapp.com/'

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    for_message = ['пока я туповат и никуя не понимаю', 'я учусь', 'отстань от меня человек', 'ой, всё']
    bot_message_random = random.randrange(0, len(for_message))
    bot_mes = for_message[bot_message_random].capitalize()
    bot.send_message(message.chat.id, bot_mes)



@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "it works", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url = APP_NAME + TOKEN)
    return "it worksssssssss", 200


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


