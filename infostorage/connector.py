# _*_ coding: utf-8 _*_
# _*_ coding: cp1251 _*_
	

	
import time	
from telebot import types
import telebot
import json
from module.engine import drive
import module.bde
	
	#Чтение конфига:
with open('config.json', encoding="utf-8") as c:
	botconfig = json.load(c)
	
	#Чтение токена бота и ссылок на файлы:
bottoken = botconfig['bottoken']
	
	#Привязка бота:
bot = telebot.TeleBot(bottoken)

	#Старт бота
@bot.message_handler(content_types=['text'])
	
	#Обработка сообщений:
def get_text_messages(message):
		
	#	Определяем команда это, или текст
	mtype = message.json
	mscom = ''
	mst = ''
	if "entities" in mtype:
		mtype = mtype['entities']
		mtype = mtype[0]['type']
		if mtype == 'bot_command':
			mtypecom = True
		else:
			mtypecom = False
	else:
		mtypecom = False
			
	mst = message.text	
			
	#	Берем переменные
	userid = message.chat.id
	print(userid)
	username = message.from_user.username
	fstname = message.from_user.first_name
	msgtime = message.date
		
	mdrive = drive(botconfig, mtypecom, mst, userid, username, fstname, msgtime)
		
	butbit = mdrive.butbit()
		
	if butbit == True:
		keyboard = types.InlineKeyboardMarkup()
			
		butcount = mdrive.butcount()
		butname = mdrive.butname()
		butcom = mdrive.butcom()
		butmess = mdrive.butmess()
			
					
		i = 0
		while i != butcount:
			key = types.InlineKeyboardButton(text=butname[i], callback_data=butcom[i]) #кнопка «Да»
			keyboard.add(key)
			i = i + 1
				
		bot.send_message(message.from_user.id, text=butmess, reply_markup=keyboard)
					
	else:
		mtext = mdrive.text()
		bot.send_message(message.from_user.id, mtext)		
	print(mst)
			
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
		
	mst = call.data
	mtypecom = True
	userid = call.message.chat.id
	print(userid)
	msgtime = call.message.date
		
	bdrive = drive(botconfig, mtypecom, mst, userid, 'bot', 'bot', msgtime)
		
	butbit = bdrive.butbit()
		
	if butbit == True:
		keyboard = types.InlineKeyboardMarkup()
			
		butcount = bdrive.butcount()
		butname = bdrive.butname()
		butcom = bdrive.butcom()
		butmess = bdrive.butmess()
			
					
		i = 0
		while i != butcount:
			key = types.InlineKeyboardButton(text=butname[i], callback_data=butcom[i]) #кнопка «Да»
			keyboard.add(key)
			i = i + 1
				
		bot.send_message(call.message.chat.id, text=butmess, reply_markup=keyboard)
					
	else:
		mtext = bdrive.text()
		bot.send_message(call.message.chat.id, mtext)
	print(call.data)
#	

	
#bot.polling(none_stop=True, interval=0)

while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:

		print(e) 

		time.sleep(15)			
	
