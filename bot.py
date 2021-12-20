import telebot
from telebot import types
# Название телеграм бота HelpForStudents_RGSU_bot
TOKEN = '5026323173:AAHfiGMC21MAWt_ysuzdbCaX9DuqyzGCS_Q'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['record'])
def handle_text(message):
        bot.send_message(message.chat.id, 'Добро пожаловать в HelpForStudents_RGSU_bot, {0.first_name}! - Все управление ботом осуществляется с помощью кнопок✨- Вы можете посмотреть актуальное расписание преподавателя своей или другой группы ✌️- Актуальное расписание каждые 7 утра ✨- Напоминание о начале пары 🔥- Если что-то произойдет и вы застрянете где-то, то вам в помощь /start' )

@bot.message_handler(commands=['info'])
def text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
     bot.send_message(message.chat.id, 'Выберите группу')
    item1 = types.KeyboardButton('ИН-КОД-2020-2-11')
    item2 = types.KeyboardButton('ИН-КОД-2019-1')
    
    markup.add(item1,item2)
    
    bot.send_message(message.chat.id, 'Приветствую ,{0.first_name}, данный бод является экспериментальной разработкой по записи клиентов в салон через телеграм,! По всем вопросам обращайтесь в лс @jerome0205'.format(message.from_user),reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private':
		if message.text == '💵Прайс и мастера': 
			bot.send_photo(message.chat.id, 'https://wampi.ru/image/RUhWVAr' ) 
			bot.send_photo(message.chat.id, 'https://wampi.ru/image/RUu0nFx' )
			bot.send_message(message.chat.id, 'данные фото были взяты у реальных мастеров с их согласия' )

		if message.text == '📍🗺️Адрес':
			bot.send_message(message.chat.id, ' Г.Москва, Ленинский проспект дом 90 (данный салон больше не работает, взят для примера).')
			bot.send_photo(message.chat.id, 'https://wampi.ru/image/RUu23ef' )
			bot.send_photo(message.chat.id, 'https://wampi.ru/image/RUuNCm7' )
		if message.text == '🕒Время работы':
			bot.send_message(message.chat.id, 'c 10:00 до 22:00' )

bot.polling(none_stop= True)