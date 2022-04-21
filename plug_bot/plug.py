# _*_ coding: utf-8 _*_
# _*_ coding: cp1251 _*_

from telebot import types
import telebot
import json
import time

#Чтение конфига:
with open('config.json', encoding="utf-8") as c:
	botconfig = json.load(c)

#Чтение токена бота и ссылок на файлы:
bottoken = botconfig['bottoken']
answerlink = botconfig['answer']

#Привязка бота:
bot = telebot.TeleBot(bottoken)

#Чтение файла с текстовыми ответами:
with open(answerlink, encoding="utf-8") as a:
	answer = json.load(a)

#Чтение текстов:
helper = answer['helper']
ficha = answer['ficha']

#Старт бота
@bot.message_handler(content_types=['text'])

#Обработка сообщений:
def get_text_messages(message):
	print(message)
	#Фича:
	if message.text == 'Покажи фичу':
		bot.send_message(message.from_user.id, ficha)
	
	#Стандартный ответ:	
	else:
		bot.send_message(message.from_user.id, helper)

while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:

		print(e) 

		time.sleep(15)		
