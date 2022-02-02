import telebot
import config

bot = telebot.TeleBot(config.TOKEN) 

@bot.message_handler(commands=['start'])
def hi(message):
	bot.send_message(message.chat.id, f'{message.from_user.first_name} {message.from_user.last_name} " привет, меня зовут «Download_YouTube», и я помогу тебе скачать видео с ютуба"')
	bot.send_message(message.chat.id, 'Как все происходит: Сначала ты ищешь видео, которое тебе нужно скачать, дальше вводишь его сюда, потом тебе бот сбрасывает ссылку, где можно скачать это видео, все очень просто :D')
	bot.send_message(message.chat.id, 'Cкинь ссылку ниже⬇⬇⬇')

@bot.message_handler(content_types=['text'])
def silka(message):
	bot.send_message(message.chat.id, "sfrom.net/" + message.text)

# RUN
bot.polling(none_stop=True)