import os
import telebot
from flask import Flask, request
import random


TOKEN = '1668076384:AAF4aDoDF6_KqaADNtgGjUIdgykdVAM4qtI'
APP_NAME = 'https://error-bot-check.herokuapp.com/'

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)

testGroup_withOlenka = -579324010
test_group = -1001153348142

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # mes = get_messages()
    mes = 'some text'
    bot.send_message(message.from_user.id, mes)
    # bot.send_message(message.from_user.id, mes)


@bot.message_handler(commands=['send'])
def send_to_group(message):
    mes = 'my message'
    bot.send_message(testGroup_withOlenka, mes)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    for_message = ['пока я туповат и никуя не понимаю', 'я учусь', 'отстань от меня человек', 'ой, всё']
    bot_message_random = random.randrange(0, len(for_message))
    bot_mes = for_message[bot_message_random].capitalize()
    bot.send_message(message.chat.id, bot_mes)



#
# def get_messages():
#     # Функция использует метод getUpdates и возвращает массив объектов
#     result = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates?offset=10').json()
#     return result['result']

# def set_message(chat_id, text):
#     # Функция использует метод sendMessage для отправки текстовых сообщений
#     requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
#
# def check_message(message):
#     # Проверяем текст сообщения отправленное боту
#     if message.lower() in ['привет', 'hello']:
#         return 'Привет :)'
#     else:
#         return 'Я не понимаю('
#
# def run():
#     update_id = get_messages()[-1]['update_id'] # Присваиваем ID последнего отправленного сообщения боту
#     while True:
#         time.sleep(1)
#         messages = get_messages() # Получаем обновления
#         for message in messages:
#             # Если в обновлении есть ID больше чем ID последнего сообщения, значит пришло новое сообщение
#             if update_id < message['update_id']:
#                 update_id = message['update_id'] # Присваиваем ID последнего отправленного сообщения боту
#                 # Отвечаем тому кто прислал сообщение боту
#                 set_message(message['message']['chat']['id'], check_message(message['message']['text']))
#



@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "it works", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_NAME + TOKEN)
    return "it worksssssssss", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


