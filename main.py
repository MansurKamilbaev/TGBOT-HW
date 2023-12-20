import telebot

bot = telebot.TeleBot('6717597402:AAFWypDJJJHQ-9Yt1_O1xYY8H5dajbdkbwI')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Привет! Я первый бот юного программиста')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, 'Это простой Telegram-бот. Используйте /start для приветствия.')


bot.infinity_polling()
