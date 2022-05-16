#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'вставьте свой токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репо")
	item2 = types.KeyboardButton("😋 Написать в личку")
	item3 = types.KeyboardButton("😜 Я на Facebook")
	item4 =	types.KeyboardButton("🤫 Я в Instagram")

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Привет тебе, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репо':
			bot.send_message(message.chat.id, 'https://github.com/evgeniychistykh')
		elif message.text == '😋 Написать в личку':
			bot.send_message(message.chat.id, 'http://t.me/ev_chist')
		elif message.text == '😜 Я на Facebook':
			bot.send_message(message.chat.id, 'https://www.facebook.com/e.chistykh')
		elif message.text == '🤫 Я в Instagram':
			bot.send_message(message.chat.id, 'https://www.instagram.com/evgenij_chistykh')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
